# SourceBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency code (e.g., USD) | [optional] 
**currency_scale** | **int** | Number of decimal places for the currency | [optional] 
**grand_total** | **float** | Grand total amount in smallest currency unit | [optional] 
**subtotal** | **float** | Subtotal amount in smallest currency unit | [optional] 
**additional_items** | **float** | Additional items amount in smallest currency unit | [optional] 
**ar_transfer** | **float** | Accounts receivable transfer amount in smallest currency unit | [optional] 
**amount_paid** | **float** | Amount paid in smallest currency unit | [optional] 
**refund_issued** | **float** | Refund issued amount in smallest currency unit | [optional] 
**upcoming_payments** | **float** | Upcoming payments amount in smallest currency unit | [optional] 
**upcoming_refund** | **float** | Upcoming refund amount in smallest currency unit | [optional] 
**cancellation_fee** | **float** | Cancellation fee amount in smallest currency unit | [optional] 
**no_show_fee** | **float** | No show fee amount in smallest currency unit | [optional] 
**tax_breakdown** | [**List[BalanceBreakdownItem]**](BalanceBreakdownItem.md) | Tax breakdown details as array of items with id and amount | [optional] 
**fee_breakdown** | [**List[BalanceBreakdownItem]**](BalanceBreakdownItem.md) | Fee breakdown details as array of items with id and amount | [optional] 
**balance_due** | **float** | Balance due amount in smallest currency unit | [optional] 
**updated_at** | **datetime** | Timestamp when the balance was last updated (UTC) | [optional] 

## Example

```python
from cloudbeds_accounting.models.source_balance_response import SourceBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SourceBalanceResponse from a JSON string
source_balance_response_instance = SourceBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(SourceBalanceResponse.to_json())

# convert the object into a dict
source_balance_response_dict = source_balance_response_instance.to_dict()
# create an instance of SourceBalanceResponse from a dict
source_balance_response_from_dict = SourceBalanceResponse.from_dict(source_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


