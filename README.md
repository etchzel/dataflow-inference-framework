# Dataflow ML Inference Framework

This is the main version of the Dataflow ML Inference Framework.

## Explanation

- `main.py`

  The main building block of the pipeline. Do not modify this file.

- `modules > input.py`

  The module that reads the input/test data from BigQuery. 
  
  The students should try to query their tables from BigQuery with the correct SQL query. 
  
  This is done under the function `process`. Note that after querying, the students should properly iterate over the rows given, and yield the proper input for their model.

  The yielded input should be a tuple with the first element as the row data, second element as the formatted input for inference.

- `modules > options.py`

  The module for defining runtime parameters. Do not modify.

- `modules > output.py`

  The module for formatting the output to be written to BigQuery.

  This module is executed after the inference is done. You should format the output as a dictionary, and match it with the schema given in `schema.py`.

- `modules > schema.py`

  This module defines the schema for the output table / job.
  
  Do not modify unless you know what you are doing, this correlates directly to `output.py`.\

## How to build and execute

Once you finish the coding process, build the template:

```bash
python main.py \
--endpoint_id=YOUR_ENDPOINT_ID \
--project=YOUR_PROJECT \
--region=YOUR_REGION \
--staging_location=YOUR_GCS_STAGING_FOLDER \
--temp_location=YOUR_GCS_TEMP_FOLDER \
--template_location=YOUR_GCS_TEMPLATE_FOLDER
```

Once the template is built, you should create the job following the examples given in Module 3.

In the `ADD PARAMETERS` section, use the following parameters:

```bash
table_name = YOUR_DATASET.YOUR_INPUT_TABLE
target_table = YOUR_DATASET.YOUR_OUTPUT_TABLE
```
