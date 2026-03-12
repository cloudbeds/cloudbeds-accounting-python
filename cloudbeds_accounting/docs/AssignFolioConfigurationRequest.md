# AssignFolioConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **int** | Folio configuration ID to assign | 
**source_id** | **int** | Source ID (reservation ID, group profile ID, etc.) | 
**source_kind** | [**FolioSourceKind**](FolioSourceKind.md) |  | 

## Example

```python
from cloudbeds_accounting.models.assign_folio_configuration_request import AssignFolioConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignFolioConfigurationRequest from a JSON string
assign_folio_configuration_request_instance = AssignFolioConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(AssignFolioConfigurationRequest.to_json())

# convert the object into a dict
assign_folio_configuration_request_dict = assign_folio_configuration_request_instance.to_dict()
# create an instance of AssignFolioConfigurationRequest from a dict
assign_folio_configuration_request_from_dict = AssignFolioConfigurationRequest.from_dict(assign_folio_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


