def format_output(row):
  output = {
    **dict(row[0]),
    "fraud_inference": row[1].inference
  }
  return output