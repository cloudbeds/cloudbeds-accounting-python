# TransactionItemMappingModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**name** | **str** |  | 
**code** | **str** |  | 
**sku** | **str** |  | [optional] 
**item_group** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.transaction_item_mapping_model import TransactionItemMappingModel

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionItemMappingModel from a JSON string
transaction_item_mapping_model_instance = TransactionItemMappingModel.from_json(json)
# print the JSON string representation of the object
print(TransactionItemMappingModel.to_json())

# convert the object into a dict
transaction_item_mapping_model_dict = transaction_item_mapping_model_instance.to_dict()
# create an instance of TransactionItemMappingModel from a dict
transaction_item_mapping_model_from_dict = TransactionItemMappingModel.from_dict(transaction_item_mapping_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


