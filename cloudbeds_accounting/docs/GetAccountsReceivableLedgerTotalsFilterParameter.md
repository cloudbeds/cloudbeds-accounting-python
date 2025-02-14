# GetAccountsReceivableLedgerTotalsFilterParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**List[AccountsReceivableLedgerStatus]**](AccountsReceivableLedgerStatus.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.get_accounts_receivable_ledger_totals_filter_parameter import GetAccountsReceivableLedgerTotalsFilterParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsReceivableLedgerTotalsFilterParameter from a JSON string
get_accounts_receivable_ledger_totals_filter_parameter_instance = GetAccountsReceivableLedgerTotalsFilterParameter.from_json(json)
# print the JSON string representation of the object
print(GetAccountsReceivableLedgerTotalsFilterParameter.to_json())

# convert the object into a dict
get_accounts_receivable_ledger_totals_filter_parameter_dict = get_accounts_receivable_ledger_totals_filter_parameter_instance.to_dict()
# create an instance of GetAccountsReceivableLedgerTotalsFilterParameter from a dict
get_accounts_receivable_ledger_totals_filter_parameter_from_dict = GetAccountsReceivableLedgerTotalsFilterParameter.from_dict(get_accounts_receivable_ledger_totals_filter_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


