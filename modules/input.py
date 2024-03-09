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
      SELECT * FROM `{project_id}.{self.table_name.get()}`
      """
    )

    rows = query_job.result()

    categorical_mapper = {
      "married": 0,
      "others": 1,
      "single": 2,
      "female": 0,
      "male": 1,
      "GradSch": 0,
      "HighSch": 1,
      "Other": 2,
      "Univ": 3
    }

    for row in rows:
      yield (row, [categorical_mapper.get(row[k], row[k]) for k in row.keys() if k != 'ID'])

    