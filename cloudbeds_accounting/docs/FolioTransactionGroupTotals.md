# FolioTransactionGroupTotals

Per-group totals for the current page only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**quantity** | **int** | Sum of quantities (product/addon types) | [optional] 
**total_debit** | **float** |  | [optional] 
**total_credit** | **float** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.folio_transaction_group_totals import FolioTransactionGroupTotals

# TODO update the JSON string below
json = "{}"
# create an instance of FolioTransactionGroupTotals from a JSON string
folio_transaction_group_totals_instance = FolioTransactionGroupTotals.from_json(json)
# print the JSON string representation of the object
print(FolioTransactionGroupTotals.to_json())

# convert the object into a dict
folio_transaction_group_totals_dict = folio_transaction_group_totals_instance.to_dict()
# create an instance of FolioTransactionGroupTotals from a dict
folio_transaction_group_totals_from_dict = FolioTransactionGroupTotals.from_dict(folio_transaction_group_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


