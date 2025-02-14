# CustomTransactionCodesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**name** | **str** |  | 
**code** | **str** |  | 
**sku** | **str** |  | [optional] 
**item_group** | **str** |  | [optional] 
**custom_general_ledger_code_id** | **str** |  | [optional] 

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


