# AccountsReceivableLedgerPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | [**AccountsReceivableLedgerStatus**](AccountsReceivableLedgerStatus.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.accounts_receivable_ledger_patch_request import AccountsReceivableLedgerPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsReceivableLedgerPatchRequest from a JSON string
accounts_receivable_ledger_patch_request_instance = AccountsReceivableLedgerPatchRequest.from_json(json)
# print the JSON string representation of the object
print(AccountsReceivableLedgerPatchRequest.to_json())

# convert the object into a dict
accounts_receivable_ledger_patch_request_dict = accounts_receivable_ledger_patch_request_instance.to_dict()
# create an instance of AccountsReceivableLedgerPatchRequest from a dict
accounts_receivable_ledger_patch_request_from_dict = AccountsReceivableLedgerPatchRequest.from_dict(accounts_receivable_ledger_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


