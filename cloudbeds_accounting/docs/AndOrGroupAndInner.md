# AndOrGroupAndInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AndOrGroupAndInner]**](AndOrGroupAndInner.md) |  | [optional] 
**var_or** | [**List[AndOrGroupAndInner]**](AndOrGroupAndInner.md) |  | [optional] 
**operator** | [**ConditionalOperator**](ConditionalOperator.md) |  | 
**value** | **object** |  | [optional] 
**var_field** | **str** |  | 

## Example

```python
from cloudbeds_accounting.models.and_or_group_and_inner import AndOrGroupAndInner

# TODO update the JSON string below
json = "{}"
# create an instance of AndOrGroupAndInner from a JSON string
and_or_group_and_inner_instance = AndOrGroupAndInner.from_json(json)
# print the JSON string representation of the object
print(AndOrGroupAndInner.to_json())

# convert the object into a dict
and_or_group_and_inner_dict = and_or_group_and_inner_instance.to_dict()
# create an instance of AndOrGroupAndInner from a dict
and_or_group_and_inner_from_dict = AndOrGroupAndInner.from_dict(and_or_group_and_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


