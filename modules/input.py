from apache_beam import DoFn

class Input(DoFn):
  def __init__(self, table_name):
    self.table_name = table_name
  
  def setup(self):
    from google.cloud import bigquery
    self.client = bigquery.Client()
  
  def process(self, element):
    table_name = self.table_name.get()
    
    # write your input logic below

    # to pass your input to the next step in the pipeline, use yield <input-data>

    # yielded input should be a tuple, with the first element as the whole row data
    # and the second element is the formatted input for the inference
    # example: (row, [row[k] for k in row.keys()])
    yield ''