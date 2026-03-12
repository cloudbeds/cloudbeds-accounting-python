# FolioConfigurationFolioTransactionTypeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folio_id** | **int** |  | [optional] 
**transaction_type** | **str** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.folio_configuration_folio_transaction_type_data import FolioConfigurationFolioTransactionTypeData

# TODO update the JSON string below
json = "{}"
# create an instance of FolioConfigurationFolioTransactionTypeData from a JSON string
folio_configuration_folio_transaction_type_data_instance = FolioConfigurationFolioTransactionTypeData.from_json(json)
# print the JSON string representation of the object
print(FolioConfigurationFolioTransactionTypeData.to_json())

# convert the object into a dict
folio_configuration_folio_transaction_type_data_dict = folio_configuration_folio_transaction_type_data_instance.to_dict()
# create an instance of FolioConfigurationFolioTransactionTypeData from a dict
folio_configuration_folio_transaction_type_data_from_dict = FolioConfigurationFolioTransactionTypeData.from_dict(folio_configuration_folio_transaction_type_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


