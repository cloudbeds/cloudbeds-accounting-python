# RoutingContext

Routing destination info. Only present when routedFrom is set (transaction was routed from another source). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_profile_id** | **str** |  | [optional] 
**group_profile_name** | **str** |  | [optional] 
**group_profile_identifier** | **str** |  | [optional] 
**reservation_id** | **str** |  | [optional] 
**reservation_name** | **str** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.routing_context import RoutingContext

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingContext from a JSON string
routing_context_instance = RoutingContext.from_json(json)
# print the JSON string representation of the object
print(RoutingContext.to_json())

# convert the object into a dict
routing_context_dict = routing_context_instance.to_dict()
# create an instance of RoutingContext from a dict
routing_context_from_dict = RoutingContext.from_dict(routing_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


