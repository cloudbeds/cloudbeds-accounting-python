# TrialBalanceConfigurationStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configured_at** | **str** | Configured datetime (ISO 8601) in UTC | [optional] 
**configured** | **bool** | True if this property has configured trial balance.  | [optional] 

## Example

```python
from cloudbeds_accounting.models.trial_balance_configuration_status_response import TrialBalanceConfigurationStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalanceConfigurationStatusResponse from a JSON string
trial_balance_configuration_status_response_instance = TrialBalanceConfigurationStatusResponse.from_json(json)
# print the JSON string representation of the object
print(TrialBalanceConfigurationStatusResponse.to_json())

# convert the object into a dict
trial_balance_configuration_status_response_dict = trial_balance_configuration_status_response_instance.to_dict()
# create an instance of TrialBalanceConfigurationStatusResponse from a dict
trial_balance_configuration_status_response_from_dict = TrialBalanceConfigurationStatusResponse.from_dict(trial_balance_configuration_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


