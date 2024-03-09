from apache_beam import DoFn
from apache_beam.transforms.window import GlobalWindow
from apache_beam.utils.windowed_value import WindowedValue

class Output(DoFn):
  def __init__(self, target_table):
    self.MAX_BATCH_SIZE = 1000
    self.window = GlobalWindow()
    self.target_table = target_table
  
  def setup(self):
    from google.cloud import bigquery
    self.client = bigquery.Client()
    self.job_config = bigquery.LoadJobConfig(
      write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
      create_disposition=bigquery.CreateDisposition.CREATE_IF_NEEDED,
      source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
      autodetect=True
    )

  # for batching
  def start_bundle(self):
    self.batch = []
  
  def process(self, element, window=DoFn.WindowParam):
    self.window = window
    target_table = self.target_table.get()

    # write your output logic below
    # the parameter element is the row data to be processed
    # you can get the inference result by using element[1].inference
    # you can get your original input data by using element[0]
    # to utilize the batching, make sure to collect every element into the batch
    # example: self.batch.append(element)
    # then process the batch with
    # if len(self.batch) >= self.MAX_BATCH_SIZE
    # after processing, reset the batch with self.batch = []

  # for the processing of last/final batch
  def finish_bundle(self):
    if self.batch:
      # write your output logic below

      # comment out or delete pass below after you write your logic
      pass
