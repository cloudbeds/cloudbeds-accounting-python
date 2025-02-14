# TrialBalanceReportLedgerBalances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_ledger** | [**List[TrialBalanceReportCodeInfo]**](TrialBalanceReportCodeInfo.md) |  | [optional] 
**guest_ledger** | [**List[TrialBalanceReportCodeInfo]**](TrialBalanceReportCodeInfo.md) |  | [optional] 
**accounts_receivable** | [**List[TrialBalanceReportCodeInfo]**](TrialBalanceReportCodeInfo.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.trial_balance_report_ledger_balances import TrialBalanceReportLedgerBalances

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalanceReportLedgerBalances from a JSON string
trial_balance_report_ledger_balances_instance = TrialBalanceReportLedgerBalances.from_json(json)
# print the JSON string representation of the object
print(TrialBalanceReportLedgerBalances.to_json())

# convert the object into a dict
trial_balance_report_ledger_balances_dict = trial_balance_report_ledger_balances_instance.to_dict()
# create an instance of TrialBalanceReportLedgerBalances from a dict
trial_balance_report_ledger_balances_from_dict = TrialBalanceReportLedgerBalances.from_dict(trial_balance_report_ledger_balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


