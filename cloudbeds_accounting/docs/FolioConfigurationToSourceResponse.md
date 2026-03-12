# FolioConfigurationToSourceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | Source ID | [optional] 
**source_kind** | [**FolioSourceKind**](FolioSourceKind.md) |  | [optional] 
**folio_configuration_id** | **str** | Folio configuration ID | [optional] 

## Example

```python
from cloudbeds_accounting.models.folio_configuration_to_source_response import FolioConfigurationToSourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FolioConfigurationToSourceResponse from a JSON string
folio_configuration_to_source_response_instance = FolioConfigurationToSourceResponse.from_json(json)
# print the JSON string representation of the object
print(FolioConfigurationToSourceResponse.to_json())

# convert the object into a dict
folio_configuration_to_source_response_dict = folio_configuration_to_source_response_instance.to_dict()
# create an instance of FolioConfigurationToSourceResponse from a dict
folio_configuration_to_source_response_from_dict = FolioConfigurationToSourceResponse.from_dict(folio_configuration_to_source_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


