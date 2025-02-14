# AndOrGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AndOrGroupAndInner]**](AndOrGroupAndInner.md) |  | [optional] 
**var_or** | [**List[AndOrGroupAndInner]**](AndOrGroupAndInner.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.and_or_group import AndOrGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AndOrGroup from a JSON string
and_or_group_instance = AndOrGroup.from_json(json)
# print the JSON string representation of the object
print(AndOrGroup.to_json())

# convert the object into a dict
and_or_group_dict = and_or_group_instance.to_dict()
# create an instance of AndOrGroup from a dict
and_or_group_from_dict = AndOrGroup.from_dict(and_or_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


