from apache_beam import DoFn

class Input(DoFn):
  def __init__(self):
    raise NotImplementedError
  
  def setup(self):
    raise NotImplementedError
  
  def process(self, element):
    # write your input logic below
    raise NotImplementedError