# GetFoliosFilterParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **int** | Filter by source ID | 
**source_kind** | [**FolioSourceKind**](FolioSourceKind.md) |  | 

## Example

```python
from cloudbeds_accounting.models.get_folios_filter_parameter import GetFoliosFilterParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GetFoliosFilterParameter from a JSON string
get_folios_filter_parameter_instance = GetFoliosFilterParameter.from_json(json)
# print the JSON string representation of the object
print(GetFoliosFilterParameter.to_json())

# convert the object into a dict
get_folios_filter_parameter_dict = get_folios_filter_parameter_instance.to_dict()
# create an instance of GetFoliosFilterParameter from a dict
get_folios_filter_parameter_from_dict = GetFoliosFilterParameter.from_dict(get_folios_filter_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


