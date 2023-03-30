
# NikeITPersonasCollectionAndSalesforce

This Yeager Workflow component is responsible for collecting data related to Nike employees in the IT department from multiple trusted data sources and/or public platforms, and sending the extracted data to Salesforce. It processes the data and ensures the integrity of the data before transferring it to the Salesforce platform.


## Initial generation prompt
description: "IOs - - input:\n  - DataSources: List of trusted data sources and/or\
  \ public platforms that contain\n      information related to Nike employees in\
  \ the IT department.\n- output:\n  - SentToSalesforce: A boolean value indicating\
  \ whether the extracted data was successfully\n      sent to Salesforce.\n"
name: NikeITPersonasCollectionAndSalesforce


## Transformer breakdown
- Execute the transform of the AbstractWorkflow
- Prepare the Output BaseModel

## Parameters
[]

        