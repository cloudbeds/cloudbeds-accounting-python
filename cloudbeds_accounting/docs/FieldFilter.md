# FieldFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**ConditionalOperator**](ConditionalOperator.md) |  | 
**value** | **object** | Can be any of supported OpenApi types. | [optional] 
**var_field** | **str** |  | 

## Example

```python
from cloudbeds_accounting.models.field_filter import FieldFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FieldFilter from a JSON string
field_filter_instance = FieldFilter.from_json(json)
# print the JSON string representation of the object
print(FieldFilter.to_json())

# convert the object into a dict
field_filter_dict = field_filter_instance.to_dict()
# create an instance of FieldFilter from a dict
field_filter_from_dict = FieldFilter.from_dict(field_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


