# PageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** |  | [optional] 
**number** | **int** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.page_details import PageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PageDetails from a JSON string
page_details_instance = PageDetails.from_json(json)
# print the JSON string representation of the object
print(PageDetails.to_json())

# convert the object into a dict
page_details_dict = page_details_instance.to_dict()
# create an instance of PageDetails from a dict
page_details_from_dict = PageDetails.from_dict(page_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


