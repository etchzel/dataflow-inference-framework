from apache_beam import DoFn
from apache_beam.transforms.window import GlobalWindow
from apache_beam.utils.windowed_value import WindowedValue

class Output(DoFn):
  def __init__(self, target_table):
    raise Exception("This class is deprecated")
    self.MAX_BATCH_SIZE = 1000
    self.window = GlobalWindow()
    self.target_table = target_table
  
  def setup(self):
    raise Exception("This class is deprecated")
    from google.cloud import bigquery
    self.client = bigquery.Client()
    self.job_config = bigquery.LoadJobConfig(
      write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
      create_disposition=bigquery.CreateDisposition.CREATE_IF_NEEDED,
      source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
      autodetect=True
    )

  def start_bundle(self):
    raise Exception("This class is deprecated")
    self.batch = []
  
  def process(self, element, window=DoFn.WindowParam):
    raise Exception("This class is deprecated")
    self.window = window

    # write your output logic below
    output = {
      **dict(element[0]),
      'TARGET_INFERENCE': element[1].inference
    }

    self.batch.append(output)
    if len(self.batch) >= self.MAX_BATCH_SIZE:
      job = self.client.load_table_from_json(
        json_rows=self.batch,
        destination=f"{self.client.project}.{self.target_table.get()}",
        job_config=self.job_config
      )
      job.result()
      self.batch = []

  def finish_bundle(self):
    raise Exception("This class is deprecated")
    if self.batch:
      job = self.client.load_table_from_json(
        json_rows=self.batch,
        destination=f"{self.client.project}.{self.target_table.get()}",
        job_config=self.job_config
      )
      job.result()