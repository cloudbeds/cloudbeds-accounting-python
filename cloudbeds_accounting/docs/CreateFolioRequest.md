# CreateFolioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Folio name | 
**folio_configuration_id** | **int** | Folio configuration ID | [optional] 
**parent_id** | **int** | Parent folio ID (for sub-folios) | [optional] 
**source_id** | **int** | Source ID (reservation ID, group profile ID, or house account ID) | 
**source_kind** | [**FolioSourceKind**](FolioSourceKind.md) |  | 
**transaction_types** | [**List[TransactionTypeIdentifier]**](TransactionTypeIdentifier.md) | Transaction types to assign to this folio | 

## Example

```python
from cloudbeds_accounting.models.create_folio_request import CreateFolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolioRequest from a JSON string
create_folio_request_instance = CreateFolioRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFolioRequest.to_json())

# convert the object into a dict
create_folio_request_dict = create_folio_request_instance.to_dict()
# create an instance of CreateFolioRequest from a dict
create_folio_request_from_dict = CreateFolioRequest.from_dict(create_folio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


