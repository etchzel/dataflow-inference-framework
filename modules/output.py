from apache_beam import DoFn

class Output(DoFn):
  def __init__(self):
    raise NotImplementedError
  
  def setup(self):
    raise NotImplementedError
  
  def process(self, element):
    # write your output logic below
    raise NotImplementedError