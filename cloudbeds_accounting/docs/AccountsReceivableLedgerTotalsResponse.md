# AccountsReceivableLedgerTotalsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | [optional] 
**paid** | **float** |  | [optional] 
**balance** | **float** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.accounts_receivable_ledger_totals_response import AccountsReceivableLedgerTotalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsReceivableLedgerTotalsResponse from a JSON string
accounts_receivable_ledger_totals_response_instance = AccountsReceivableLedgerTotalsResponse.from_json(json)
# print the JSON string representation of the object
print(AccountsReceivableLedgerTotalsResponse.to_json())

# convert the object into a dict
accounts_receivable_ledger_totals_response_dict = accounts_receivable_ledger_totals_response_instance.to_dict()
# create an instance of AccountsReceivableLedgerTotalsResponse from a dict
accounts_receivable_ledger_totals_response_from_dict = AccountsReceivableLedgerTotalsResponse.from_dict(accounts_receivable_ledger_totals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


