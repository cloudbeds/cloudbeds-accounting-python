# TransactionItemMappingUpdateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.transaction_item_mapping_update_model import TransactionItemMappingUpdateModel

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionItemMappingUpdateModel from a JSON string
transaction_item_mapping_update_model_instance = TransactionItemMappingUpdateModel.from_json(json)
# print the JSON string representation of the object
print(TransactionItemMappingUpdateModel.to_json())

# convert the object into a dict
transaction_item_mapping_update_model_dict = transaction_item_mapping_update_model_instance.to_dict()
# create an instance of TransactionItemMappingUpdateModel from a dict
transaction_item_mapping_update_model_from_dict = TransactionItemMappingUpdateModel.from_dict(transaction_item_mapping_update_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


