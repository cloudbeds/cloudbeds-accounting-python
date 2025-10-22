# SettingValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_consumption** | [**DepositConsumptionEnum**](DepositConsumptionEnum.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.setting_values import SettingValues

# TODO update the JSON string below
json = "{}"
# create an instance of SettingValues from a JSON string
setting_values_instance = SettingValues.from_json(json)
# print the JSON string representation of the object
print(SettingValues.to_json())

# convert the object into a dict
setting_values_dict = setting_values_instance.to_dict()
# create an instance of SettingValues from a dict
setting_values_from_dict = SettingValues.from_dict(setting_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


