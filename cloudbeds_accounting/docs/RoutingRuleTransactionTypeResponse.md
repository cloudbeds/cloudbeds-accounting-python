# RoutingRuleTransactionTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_relation_kind** | [**ExternalRelationKind**](ExternalRelationKind.md) |  | [optional] 
**origin_id** | **str** | Origin ID for the transaction type (e.g., fee ID, tax ID) | [optional] 

## Example

```python
from cloudbeds_accounting.models.routing_rule_transaction_type_response import RoutingRuleTransactionTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingRuleTransactionTypeResponse from a JSON string
routing_rule_transaction_type_response_instance = RoutingRuleTransactionTypeResponse.from_json(json)
# print the JSON string representation of the object
print(RoutingRuleTransactionTypeResponse.to_json())

# convert the object into a dict
routing_rule_transaction_type_response_dict = routing_rule_transaction_type_response_instance.to_dict()
# create an instance of RoutingRuleTransactionTypeResponse from a dict
routing_rule_transaction_type_response_from_dict = RoutingRuleTransactionTypeResponse.from_dict(routing_rule_transaction_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


