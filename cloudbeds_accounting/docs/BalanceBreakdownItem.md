# BalanceBreakdownItem

Breakdown item with name and amount for tax or fee breakdown

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the breakdown item (e.g., tax name, fee name) | 
**amount** | **float** | The amount in the smallest currency unit (e.g., cents for USD) | 

## Example

```python
from cloudbeds_accounting.models.balance_breakdown_item import BalanceBreakdownItem

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceBreakdownItem from a JSON string
balance_breakdown_item_instance = BalanceBreakdownItem.from_json(json)
# print the JSON string representation of the object
print(BalanceBreakdownItem.to_json())

# convert the object into a dict
balance_breakdown_item_dict = balance_breakdown_item_instance.to_dict()
# create an instance of BalanceBreakdownItem from a dict
balance_breakdown_item_from_dict = BalanceBreakdownItem.from_dict(balance_breakdown_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


