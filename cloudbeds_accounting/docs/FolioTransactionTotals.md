# FolioTransactionTotals

Global totals across all matching transactions (all pages).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of matching transactions | [optional] 
**total_debit** | **float** | Sum of all debit amounts in smallest currency unit | [optional] 
**total_credit** | **float** | Sum of all credit amounts in smallest currency unit | [optional] 
**currency** | **str** | Property currency ISO code | [optional] 
**currency_scale** | **int** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.folio_transaction_totals import FolioTransactionTotals

# TODO update the JSON string below
json = "{}"
# create an instance of FolioTransactionTotals from a JSON string
folio_transaction_totals_instance = FolioTransactionTotals.from_json(json)
# print the JSON string representation of the object
print(FolioTransactionTotals.to_json())

# convert the object into a dict
folio_transaction_totals_dict = folio_transaction_totals_instance.to_dict()
# create an instance of FolioTransactionTotals from a dict
folio_transaction_totals_from_dict = FolioTransactionTotals.from_dict(folio_transaction_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


