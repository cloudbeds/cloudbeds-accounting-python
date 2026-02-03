# CustomTransactionCodesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**name** | **str** |  | 
**code** | **str** | The custom code assigned by the user. | 
**transaction_item_code** | **str** | The system code that cannot be modified. | [optional] 
**sku** | **str** |  | [optional] 
**item_group** | [**TransactionItemGroup**](TransactionItemGroup.md) |  | [optional] 
**custom_general_ledger_code_id** | **str** |  | [optional] 
**item_id** | **str** | Item ID for items_services group | [optional] 
**pos_item_id** | **str** | POS Item ID for items_services group | [optional] 
**tax_id** | **str** | Tax ID for taxes_fees group (taxes) | [optional] 
**fee_id** | **str** | Fee ID for taxes_fees group (fees) | [optional] 
**payment_id** | **str** | Payment ID for payments group | [optional] 
**space_id** | **str** | Space ID for spaces group | [optional] 

## Example

```python
from cloudbeds_accounting.models.custom_transaction_codes_model import CustomTransactionCodesModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTransactionCodesModel from a JSON string
custom_transaction_codes_model_instance = CustomTransactionCodesModel.from_json(json)
# print the JSON string representation of the object
print(CustomTransactionCodesModel.to_json())

# convert the object into a dict
custom_transaction_codes_model_dict = custom_transaction_codes_model_instance.to_dict()
# create an instance of CustomTransactionCodesModel from a dict
custom_transaction_codes_model_from_dict = CustomTransactionCodesModel.from_dict(custom_transaction_codes_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


