# Filters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AndOrGroupAndInner]**](AndOrGroupAndInner.md) |  | [optional] 
**var_or** | [**List[AndOrGroupAndInner]**](AndOrGroupAndInner.md) |  | [optional] 
**operator** | [**ConditionalOperator**](ConditionalOperator.md) |  | 
**value** | **object** | Can be any of supported OpenApi types. | [optional] 
**var_field** | **str** |  | 

## Example

```python
from cloudbeds_accounting.models.filters import Filters

# TODO update the JSON string below
json = "{}"
# create an instance of Filters from a JSON string
filters_instance = Filters.from_json(json)
# print the JSON string representation of the object
print(Filters.to_json())

# convert the object into a dict
filters_dict = filters_instance.to_dict()
# create an instance of Filters from a dict
filters_from_dict = Filters.from_dict(filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


