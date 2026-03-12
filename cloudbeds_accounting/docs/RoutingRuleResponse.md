# RoutingRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Routing rule ID | [optional] 
**property_id** | **str** | Property ID | [optional] 
**source_id** | **str** | Source ID (e.g., Group Profile ID) | [optional] 
**source_kind** | [**FolioSourceKind**](FolioSourceKind.md) |  | [optional] 
**enabled** | **bool** | Whether the rule is enabled | [optional] 
**transaction_types** | [**List[RoutingRuleTransactionTypeResponse]**](RoutingRuleTransactionTypeResponse.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.routing_rule_response import RoutingRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingRuleResponse from a JSON string
routing_rule_response_instance = RoutingRuleResponse.from_json(json)
# print the JSON string representation of the object
print(RoutingRuleResponse.to_json())

# convert the object into a dict
routing_rule_response_dict = routing_rule_response_instance.to_dict()
# create an instance of RoutingRuleResponse from a dict
routing_rule_response_from_dict = RoutingRuleResponse.from_dict(routing_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


