from apache_beam import DoFn

class Input(DoFn):
  def __init__(self, table_name):
    self.table_name = table_name
  
  def setup(self):
    from google.cloud import bigquery
    self.client = bigquery.Client()
  
  def process(self, element):
    # write your input logic below
    project_id = self.client.project

    query_job = self.client.query(
      f"""
      SELECT * FROM `{project_id}.{self.table_name.get()}` LIMIT 5000;
      """
    )

    rows = query_job.result()

    for row in rows:
      yield (row, [row[k] for k in row.keys() if k != 'fraud'])

    