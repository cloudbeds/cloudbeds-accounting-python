# SettingPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**SettingValues**](SettingValues.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.setting_patch_request import SettingPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingPatchRequest from a JSON string
setting_patch_request_instance = SettingPatchRequest.from_json(json)
# print the JSON string representation of the object
print(SettingPatchRequest.to_json())

# convert the object into a dict
setting_patch_request_dict = setting_patch_request_instance.to_dict()
# create an instance of SettingPatchRequest from a dict
setting_patch_request_from_dict = SettingPatchRequest.from_dict(setting_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


