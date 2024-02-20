import argparse
import logging
import sys
import apache_beam as beam
from modules.options import UserOptions
from modules.input import Input
from modules.output import Output
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.ml.inference.base import RunInference
from apache_beam.ml.inference.vertex_ai_inference import VertexAIModelHandlerJSON
  
def main(known_args, pipeline_args):
  runner = known_args.runner
  pipeline_options = PipelineOptions(pipeline_args, streaming=False, runner=runner)

  model_handler = VertexAIModelHandlerJSON(
    endpoint_id=known_args.endpoint_id,
    project=known_args.project,
    location=known_args.region
  )
  with beam.Pipeline(options=pipeline_options) as pipeline:
    user_options = pipeline_options.view_as(UserOptions)
    predict = (
      pipeline
      | "Initialize" >> beam.Create(['init'])
      | "Input" >> beam.ParDo(Input())
      | "Inference" >> RunInference(model_handler=model_handler)
      | "Output" >> beam.ParDo(Output())
      | "Print Result" >> beam.Map(print)
    )

if __name__ == "__main__":
  # Configure logging
  log = logging.getLogger()
  log.setLevel(logging.INFO)
  stream_handler = logging.StreamHandler(sys.stdout)
  stream_handler.setLevel(logging.INFO)
  log.addHandler(stream_handler)

  # Use arguments
  parser = argparse.ArgumentParser()

  # required args
  parser.add_argument(
    "--endpoint_id", required=True
  )
  parser.add_argument(
    "--project", required=True                  # example: engineering-training-413102
  )
  parser.add_argument(
    "--region", required=True                   # example: us-central1
  )
  parser.add_argument(
    "--staging_location", required=True         # example: gs://trainer_gcs_001/dataflow/staging
  )
  parser.add_argument(
    "--temp_location", required=True            # example: gs://trainer_gcs_001/dataflow/temp
  )
  parser.add_argument(
    "--template_location", required=True        # example: gs://trainer_gcs_001/dataflow/templates/batch-online-predict
  )

  # defaulted args
  parser.add_argument(
    "--runner", default="DataflowRunner"
  )
  parser.add_argument(
    "--requirements_file", default='requirements.txt'
  )
  parser.add_argument(
    "--setup_file", default="./setup.py"
  )
  known_args, pipeline_args = parser.parse_known_args()

  # dataflow args
  if known_args.runner=="DataflowRunner":
    pipeline_args.extend(
      ["--staging_location="+known_args.staging_location]
    )
    pipeline_args.extend(
      ["--temp_location="+known_args.temp_location]
    )
    pipeline_args.extend(
      ["--template_location="+known_args.template_location]
    )
    pipeline_args.extend(
      ["--requirements_file="+known_args.requirements_file]
    )
    pipeline_args.extend(
      ["--setup_file="+known_args.setup_file]
    )
    pipeline_args.extend(
      ["--region="+known_args.region]
    )
    pipeline_args.extend(
      ["--project="+known_args.project]
    )
  main(known_args, pipeline_args)