# CustomTransactionCodesUpdateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**code** | **str** |  | 
**custom_general_ledger_code_id** | **str** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.custom_transaction_codes_update_model import CustomTransactionCodesUpdateModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTransactionCodesUpdateModel from a JSON string
custom_transaction_codes_update_model_instance = CustomTransactionCodesUpdateModel.from_json(json)
# print the JSON string representation of the object
print(CustomTransactionCodesUpdateModel.to_json())

# convert the object into a dict
custom_transaction_codes_update_model_dict = custom_transaction_codes_update_model_instance.to_dict()
# create an instance of CustomTransactionCodesUpdateModel from a dict
custom_transaction_codes_update_model_from_dict = CustomTransactionCodesUpdateModel.from_dict(custom_transaction_codes_update_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


