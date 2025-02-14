# CustomGeneralLedgerCodeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**name** | **str** |  | 
**code** | **str** |  | 
**group** | **str** |  | [optional] 
**archived** | **bool** |  | [optional] [default to False]

## Example

```python
from cloudbeds_accounting.models.custom_general_ledger_code_model import CustomGeneralLedgerCodeModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomGeneralLedgerCodeModel from a JSON string
custom_general_ledger_code_model_instance = CustomGeneralLedgerCodeModel.from_json(json)
# print the JSON string representation of the object
print(CustomGeneralLedgerCodeModel.to_json())

# convert the object into a dict
custom_general_ledger_code_model_dict = custom_general_ledger_code_model_instance.to_dict()
# create an instance of CustomGeneralLedgerCodeModel from a dict
custom_general_ledger_code_model_from_dict = CustomGeneralLedgerCodeModel.from_dict(custom_general_ledger_code_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


