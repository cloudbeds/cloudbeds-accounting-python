# TrialBalanceReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trial_balance_id** | **str** |  | [optional] 
**summary** | [**TrialBalanceReportSummary**](TrialBalanceReportSummary.md) |  | [optional] 
**ledger_balances** | [**TrialBalanceReportLedgerBalances**](TrialBalanceReportLedgerBalances.md) |  | [optional] 
**guest_ledger** | [**TrialBalanceReportGuestLedger**](TrialBalanceReportGuestLedger.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.trial_balance_report_response import TrialBalanceReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalanceReportResponse from a JSON string
trial_balance_report_response_instance = TrialBalanceReportResponse.from_json(json)
# print the JSON string representation of the object
print(TrialBalanceReportResponse.to_json())

# convert the object into a dict
trial_balance_report_response_dict = trial_balance_report_response_instance.to_dict()
# create an instance of TrialBalanceReportResponse from a dict
trial_balance_report_response_from_dict = TrialBalanceReportResponse.from_dict(trial_balance_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


