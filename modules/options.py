from apache_beam.options.pipeline_options import PipelineOptions

class UserOptions(PipelineOptions):
  @classmethod
  def _add_argparse_args(cls, parser):
    # add runtime argument below
    # some examples
    parser.add_value_provider_argument('--table_name', help='Name of the input table in the format of dataset.table_name')
    parser.add_value_provider_argument('--target_table', help='Name of the target table in the format of dataset.table_name')