# ListFolioTransactionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **int** | Source ID (reservation ID, group profile ID, house account ID) | 
**source_kind** | [**SourceKind**](SourceKind.md) |  | 
**folio_id** | **int** | Filter by specific folio | [optional] 
**posted** | **bool** | Filter by posted status. Omit to include both posted and pending. | [optional] 
**description_filters** | **List[str]** | Filter by transaction description identifiers. Accepts composite identifiers in the format: \&quot;{type}_{originId}\&quot; for item-level filtering (e.g. \&quot;product_123\&quot;, \&quot;tax_456\&quot;, \&quot;addon_789\&quot;, \&quot;fee_101\&quot;, \&quot;custom_item_202\&quot;, \&quot;bookable_resource_303\&quot;), literal group names for room revenue (\&quot;rate\&quot;, \&quot;roomRevenue_manual\&quot;, \&quot;roomRevenue_cancellation\&quot;, \&quot;roomRevenue_no_show\&quot;, \&quot;accountsReceivable\&quot;), or payment method codes (\&quot;cash\&quot;, \&quot;ebanking\&quot;, \&quot;cards_visa\&quot;, \&quot;cards_master\&quot;, \&quot;pay_pal\&quot;). Server translates these to internalTransactionCode group + originId query conditions.  | [optional] 
**transaction_date_from** | **datetime** | Filter transactions from this datetime (UTC, inclusive) | [optional] 
**transaction_date_to** | **datetime** | Filter transactions to this datetime (UTC, inclusive) | [optional] 
**service_date_from** | **date** | Filter by service date from (inclusive) | [optional] 
**service_date_to** | **date** | Filter by service date to (inclusive) | [optional] 
**sub_source_ids** | **List[int]** | Filter by sub-source IDs (booking room IDs for reservations) | [optional] 
**search_query** | **str** | Free text search on transaction description | [optional] 
**group_by** | [**FolioTransactionGroupByField**](FolioTransactionGroupByField.md) |  | [optional] 
**sort** | [**List[Sort]**](Sort.md) |  | [optional] 
**page_token** | **str** |  | [optional] 
**limit** | **int** | Page size. Default 100, max 1100. | [optional] [default to 100]
**include_voided** | **bool** | Include voided transactions. When false, both void transactions and the original transactions they voided are excluded (full chain removal via rootId matching).  | [optional] [default to True]
**include_total** | **bool** | Include totals in response. On first page, totals are computed and cached in Redis. Subsequent pages return cached totals. When no filters are applied, total amount is read from the pre-computed source balance.  | [optional] [default to False]

## Example

```python
from cloudbeds_accounting.models.list_folio_transactions_request import ListFolioTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListFolioTransactionsRequest from a JSON string
list_folio_transactions_request_instance = ListFolioTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListFolioTransactionsRequest.to_json())

# convert the object into a dict
list_folio_transactions_request_dict = list_folio_transactions_request_instance.to_dict()
# create an instance of ListFolioTransactionsRequest from a dict
list_folio_transactions_request_from_dict = ListFolioTransactionsRequest.from_dict(list_folio_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


