# FolioConfigurationSourceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **int** | Booking source ID | [optional] 
**is_root_source** | **bool** |  | [optional] 
**is_hotel_collect_booking** | **bool** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.folio_configuration_source_data import FolioConfigurationSourceData

# TODO update the JSON string below
json = "{}"
# create an instance of FolioConfigurationSourceData from a JSON string
folio_configuration_source_data_instance = FolioConfigurationSourceData.from_json(json)
# print the JSON string representation of the object
print(FolioConfigurationSourceData.to_json())

# convert the object into a dict
folio_configuration_source_data_dict = folio_configuration_source_data_instance.to_dict()
# create an instance of FolioConfigurationSourceData from a dict
folio_configuration_source_data_from_dict = FolioConfigurationSourceData.from_dict(folio_configuration_source_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


