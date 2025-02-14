# TrialBalanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposits_ledger_opening_balance** | **float** |  | 
**accounts_receivable_ledger_opening_balance** | **float** |  | 
**guest_ledger_opening_balance** | **float** |  | 

## Example

```python
from cloudbeds_accounting.models.trial_balance_request import TrialBalanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalanceRequest from a JSON string
trial_balance_request_instance = TrialBalanceRequest.from_json(json)
# print the JSON string representation of the object
print(TrialBalanceRequest.to_json())

# convert the object into a dict
trial_balance_request_dict = trial_balance_request_instance.to_dict()
# create an instance of TrialBalanceRequest from a dict
trial_balance_request_from_dict = TrialBalanceRequest.from_dict(trial_balance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


