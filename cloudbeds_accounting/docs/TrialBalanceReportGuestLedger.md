# TrialBalanceReportGuestLedger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charges** | [**List[TrialBalanceReportCodeInfo]**](TrialBalanceReportCodeInfo.md) |  | [optional] 
**taxes** | [**List[TrialBalanceReportCodeInfo]**](TrialBalanceReportCodeInfo.md) |  | [optional] 
**payments** | [**List[TrialBalanceReportCodeInfo]**](TrialBalanceReportCodeInfo.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.trial_balance_report_guest_ledger import TrialBalanceReportGuestLedger

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalanceReportGuestLedger from a JSON string
trial_balance_report_guest_ledger_instance = TrialBalanceReportGuestLedger.from_json(json)
# print the JSON string representation of the object
print(TrialBalanceReportGuestLedger.to_json())

# convert the object into a dict
trial_balance_report_guest_ledger_dict = trial_balance_report_guest_ledger_instance.to_dict()
# create an instance of TrialBalanceReportGuestLedger from a dict
trial_balance_report_guest_ledger_from_dict = TrialBalanceReportGuestLedger.from_dict(trial_balance_report_guest_ledger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


