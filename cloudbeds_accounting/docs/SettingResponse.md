# SettingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**SettingValues**](SettingValues.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.setting_response import SettingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingResponse from a JSON string
setting_response_instance = SettingResponse.from_json(json)
# print the JSON string representation of the object
print(SettingResponse.to_json())

# convert the object into a dict
setting_response_dict = setting_response_instance.to_dict()
# create an instance of SettingResponse from a dict
setting_response_from_dict = SettingResponse.from_dict(setting_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


