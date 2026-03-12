# FolioConfigurationFolioData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**folio_name** | **str** |  | [optional] 
**link_type** | **int** | Converted to SourceKind | [optional] 
**transaction_types** | [**List[FolioConfigurationFolioTransactionTypeData]**](FolioConfigurationFolioTransactionTypeData.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.folio_configuration_folio_data import FolioConfigurationFolioData

# TODO update the JSON string below
json = "{}"
# create an instance of FolioConfigurationFolioData from a JSON string
folio_configuration_folio_data_instance = FolioConfigurationFolioData.from_json(json)
# print the JSON string representation of the object
print(FolioConfigurationFolioData.to_json())

# convert the object into a dict
folio_configuration_folio_data_dict = folio_configuration_folio_data_instance.to_dict()
# create an instance of FolioConfigurationFolioData from a dict
folio_configuration_folio_data_from_dict = FolioConfigurationFolioData.from_dict(folio_configuration_folio_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


