# CustomGeneralLedgerCodesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomGeneralLedgerCodeModel]**](CustomGeneralLedgerCodeModel.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.custom_general_ledger_codes_update_request import CustomGeneralLedgerCodesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomGeneralLedgerCodesUpdateRequest from a JSON string
custom_general_ledger_codes_update_request_instance = CustomGeneralLedgerCodesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomGeneralLedgerCodesUpdateRequest.to_json())

# convert the object into a dict
custom_general_ledger_codes_update_request_dict = custom_general_ledger_codes_update_request_instance.to_dict()
# create an instance of CustomGeneralLedgerCodesUpdateRequest from a dict
custom_general_ledger_codes_update_request_from_dict = CustomGeneralLedgerCodesUpdateRequest.from_dict(custom_general_ledger_codes_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


