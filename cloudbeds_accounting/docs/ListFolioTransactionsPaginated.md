# ListFolioTransactionsPaginated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**Dict[str, FolioTransactionGroup]**](FolioTransactionGroup.md) | Ordered map of groupKey to group. Key is the string value of the groupBy field (e.g. \&quot;2026-02-25\&quot; for transaction_date). Pagination is applied first, then grouping.  | [optional] 
**next_page_token** | **str** | Token for fetching the next page of results | [optional] 
**totals** | [**FolioTransactionTotals**](FolioTransactionTotals.md) |  | [optional] 
**foreign_currency_totals** | [**ForeignCurrencyTotals**](ForeignCurrencyTotals.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.list_folio_transactions_paginated import ListFolioTransactionsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of ListFolioTransactionsPaginated from a JSON string
list_folio_transactions_paginated_instance = ListFolioTransactionsPaginated.from_json(json)
# print the JSON string representation of the object
print(ListFolioTransactionsPaginated.to_json())

# convert the object into a dict
list_folio_transactions_paginated_dict = list_folio_transactions_paginated_instance.to_dict()
# create an instance of ListFolioTransactionsPaginated from a dict
list_folio_transactions_paginated_from_dict = ListFolioTransactionsPaginated.from_dict(list_folio_transactions_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


