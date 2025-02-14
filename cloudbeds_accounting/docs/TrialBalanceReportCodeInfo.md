# TrialBalanceReportCodeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Transaction code | [optional] 
**description** | **str** | Description of the row | [optional] 
**amount** | **float** | Total amount for specific code | [optional] 

## Example

```python
from cloudbeds_accounting.models.trial_balance_report_code_info import TrialBalanceReportCodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalanceReportCodeInfo from a JSON string
trial_balance_report_code_info_instance = TrialBalanceReportCodeInfo.from_json(json)
# print the JSON string representation of the object
print(TrialBalanceReportCodeInfo.to_json())

# convert the object into a dict
trial_balance_report_code_info_dict = trial_balance_report_code_info_instance.to_dict()
# create an instance of TrialBalanceReportCodeInfo from a dict
trial_balance_report_code_info_from_dict = TrialBalanceReportCodeInfo.from_dict(trial_balance_report_code_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


