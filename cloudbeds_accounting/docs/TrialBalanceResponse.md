# TrialBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date of the trial balance. | [optional] 
**deposits_ledger_opening_balance** | **int** |  | [optional] 
**accounts_receivable_ledger_opening_balance** | **int** |  | [optional] 
**guest_ledger_opening_balance** | **int** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.trial_balance_response import TrialBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalanceResponse from a JSON string
trial_balance_response_instance = TrialBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(TrialBalanceResponse.to_json())

# convert the object into a dict
trial_balance_response_dict = trial_balance_response_instance.to_dict()
# create an instance of TrialBalanceResponse from a dict
trial_balance_response_from_dict = TrialBalanceResponse.from_dict(trial_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


