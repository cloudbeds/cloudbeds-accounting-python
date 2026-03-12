# FiscalDocumentSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.fiscal_document_summary import FiscalDocumentSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalDocumentSummary from a JSON string
fiscal_document_summary_instance = FiscalDocumentSummary.from_json(json)
# print the JSON string representation of the object
print(FiscalDocumentSummary.to_json())

# convert the object into a dict
fiscal_document_summary_dict = fiscal_document_summary_instance.to_dict()
# create an instance of FiscalDocumentSummary from a dict
fiscal_document_summary_from_dict = FiscalDocumentSummary.from_dict(fiscal_document_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


