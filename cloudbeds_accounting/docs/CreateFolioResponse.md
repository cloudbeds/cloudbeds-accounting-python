# CreateFolioResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Created folio ID | 

## Example

```python
from cloudbeds_accounting.models.create_folio_response import CreateFolioResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolioResponse from a JSON string
create_folio_response_instance = CreateFolioResponse.from_json(json)
# print the JSON string representation of the object
print(CreateFolioResponse.to_json())

# convert the object into a dict
create_folio_response_dict = create_folio_response_instance.to_dict()
# create an instance of CreateFolioResponse from a dict
create_folio_response_from_dict = CreateFolioResponse.from_dict(create_folio_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


