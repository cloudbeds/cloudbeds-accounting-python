# FolioResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Folio ID | [optional] 
**name** | **str** | Folio name | [optional] 
**property_id** | **str** | Property ID | [optional] 
**folio_configuration_id** | **str** | Folio configuration ID | [optional] 
**parent_id** | **str** | Parent folio ID (null for root folios) | [optional] 
**source_id** | **str** | Source ID (reservation ID, group profile ID, or config ID) | [optional] 
**source_kind** | [**FolioSourceKind**](FolioSourceKind.md) |  | [optional] 
**transaction_types** | [**List[FolioTransactionTypeResponse]**](FolioTransactionTypeResponse.md) | Transaction types assigned to this folio | [optional] 

## Example

```python
from cloudbeds_accounting.models.folio_response import FolioResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FolioResponse from a JSON string
folio_response_instance = FolioResponse.from_json(json)
# print the JSON string representation of the object
print(FolioResponse.to_json())

# convert the object into a dict
folio_response_dict = folio_response_instance.to_dict()
# create an instance of FolioResponse from a dict
folio_response_from_dict = FolioResponse.from_dict(folio_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


