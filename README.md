# Dataflow ML Inference Framework

This is the test run version. To build the template:

```bash
python main.py \
--endpoint_id=YOUR_ENDPOINT_ID \
--project=YOUR_PROJECT \
--region=YOUR_REGION \
--staging_location=YOUR_GCS_STAGING_FOLDER \
--temp_location=YOUR_GCS_TEMP_FOLDER \
--template_location=YOUR_GCS_TEMPLATE_FOLDER
```

To run the template, follow the instruction on module 3, use the following parameters for the `ADD PARAMETER` section:

```bash
table_name = YOUR_DATASET.YOUR_INPUT_TABLE
target_table = YOUR_DATASET.YOUR_OUTPUT_TABLE
```
