# TransactionItemMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TransactionItemMappingUpdateModel]**](TransactionItemMappingUpdateModel.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.transaction_item_mapping_request import TransactionItemMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionItemMappingRequest from a JSON string
transaction_item_mapping_request_instance = TransactionItemMappingRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionItemMappingRequest.to_json())

# convert the object into a dict
transaction_item_mapping_request_dict = transaction_item_mapping_request_instance.to_dict()
# create an instance of TransactionItemMappingRequest from a dict
transaction_item_mapping_request_from_dict = TransactionItemMappingRequest.from_dict(transaction_item_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


