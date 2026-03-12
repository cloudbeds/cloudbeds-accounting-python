# FolioConfigurationSaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FolioConfigurationSaveResponseData**](FolioConfigurationSaveResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.folio_configuration_save_response import FolioConfigurationSaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FolioConfigurationSaveResponse from a JSON string
folio_configuration_save_response_instance = FolioConfigurationSaveResponse.from_json(json)
# print the JSON string representation of the object
print(FolioConfigurationSaveResponse.to_json())

# convert the object into a dict
folio_configuration_save_response_dict = folio_configuration_save_response_instance.to_dict()
# create an instance of FolioConfigurationSaveResponse from a dict
folio_configuration_save_response_from_dict = FolioConfigurationSaveResponse.from_dict(folio_configuration_save_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


