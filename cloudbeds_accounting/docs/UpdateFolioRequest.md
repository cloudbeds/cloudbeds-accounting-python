# UpdateFolioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Folio name | [optional] 
**transaction_types** | [**List[TransactionTypeIdentifier]**](TransactionTypeIdentifier.md) | Transaction types to assign to this folio | [optional] 

## Example

```python
from cloudbeds_accounting.models.update_folio_request import UpdateFolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFolioRequest from a JSON string
update_folio_request_instance = UpdateFolioRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFolioRequest.to_json())

# convert the object into a dict
update_folio_request_dict = update_folio_request_instance.to_dict()
# create an instance of UpdateFolioRequest from a dict
update_folio_request_from_dict = UpdateFolioRequest.from_dict(update_folio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


