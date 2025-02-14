# TrialBalanceReportSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opening_balance** | **float** |  | [optional] 
**transactions_total_amount** | **float** |  | [optional] 
**deposit_activity** | **float** |  | [optional] 
**ar_payments** | **float** |  | [optional] 
**closing_balance** | **float** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.trial_balance_report_summary import TrialBalanceReportSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalanceReportSummary from a JSON string
trial_balance_report_summary_instance = TrialBalanceReportSummary.from_json(json)
# print the JSON string representation of the object
print(TrialBalanceReportSummary.to_json())

# convert the object into a dict
trial_balance_report_summary_dict = trial_balance_report_summary_instance.to_dict()
# create an instance of TrialBalanceReportSummary from a dict
trial_balance_report_summary_from_dict = TrialBalanceReportSummary.from_dict(trial_balance_report_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


