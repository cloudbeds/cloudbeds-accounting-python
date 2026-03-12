# FolioConfigurationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**sources** | [**List[FolioConfigurationSourceData]**](FolioConfigurationSourceData.md) |  | [optional] 
**folios** | [**List[FolioConfigurationFolioData]**](FolioConfigurationFolioData.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.folio_configuration_data import FolioConfigurationData

# TODO update the JSON string below
json = "{}"
# create an instance of FolioConfigurationData from a JSON string
folio_configuration_data_instance = FolioConfigurationData.from_json(json)
# print the JSON string representation of the object
print(FolioConfigurationData.to_json())

# convert the object into a dict
folio_configuration_data_dict = folio_configuration_data_instance.to_dict()
# create an instance of FolioConfigurationData from a dict
folio_configuration_data_from_dict = FolioConfigurationData.from_dict(folio_configuration_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


