# AccountsReceivableLedgerPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.accounts_receivable_ledger_post_request import AccountsReceivableLedgerPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsReceivableLedgerPostRequest from a JSON string
accounts_receivable_ledger_post_request_instance = AccountsReceivableLedgerPostRequest.from_json(json)
# print the JSON string representation of the object
print(AccountsReceivableLedgerPostRequest.to_json())

# convert the object into a dict
accounts_receivable_ledger_post_request_dict = accounts_receivable_ledger_post_request_instance.to_dict()
# create an instance of AccountsReceivableLedgerPostRequest from a dict
accounts_receivable_ledger_post_request_from_dict = AccountsReceivableLedgerPostRequest.from_dict(accounts_receivable_ledger_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


