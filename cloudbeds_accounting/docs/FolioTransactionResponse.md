# FolioTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**property_id** | **str** |  | [optional] 
**amount** | **float** | Transaction amount in decimal form (e.g. 150.00, not 15000). Sign depends on account type. | [optional] 
**currency** | **str** | Currency ISO code | [optional] 
**currency_scale** | **int** | Number of decimal places for the currency | [optional] 
**description** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**transaction_type** | **str** | UI-facing transaction type. Derived from internalTransactionCode: if code suffix is \&quot;A\&quot; → \&quot;adjustment\&quot;, otherwise mapped from internalCodeGroup. Maps 1:1 to MFD ReservationTransactionType except roomRevenue is split into 3.  | [optional] 
**internal_transaction_code** | **str** | Internal code managed by Cloudbeds (e.g. \&quot;1000\&quot;, \&quot;9000\&quot;) | [optional] 
**internal_code_group** | [**InternalTransactionCodeGroupEnum**](InternalTransactionCodeGroupEnum.md) |  | [optional] 
**custom_transaction_code** | **str** | Custom code managed by Property | [optional] 
**general_ledger_custom_code** | **str** |  | [optional] 
**transaction_datetime** | **datetime** | Transaction datetime (UTC) | [optional] 
**transaction_datetime_property_time** | **datetime** | Transaction datetime in property timezone | [optional] 
**service_date** | **date** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**source_id** | **str** |  | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | [optional] 
**sub_source_id** | **str** | Booking room ID for reservations | [optional] 
**sub_source_identifier** | **str** | Booking room identifier | [optional] 
**source_identifier** | **str** | Reservation identifier or group code | [optional] 
**parent_id** | **str** |  | [optional] 
**root_id** | **str** |  | [optional] 
**origin_id** | **str** |  | [optional] 
**routed_from** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**external_relation_id** | **str** |  | [optional] 
**external_relation_kind** | [**ExternalRelationKind**](ExternalRelationKind.md) |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 
**folio_id** | **str** |  | [optional] 
**posted** | **bool** | Whether the transaction is posted | [optional] 
**state** | **str** |  | [optional] 
**read_only** | **bool** | Whether the transaction is read-only (no void/refund/allocation actions allowed). Computed from reservation status, property config, and transaction state.  | [optional] 
**reservation_name** | **str** |  | [optional] 
**room_name** | **str** | Room name/identifier for the booking room associated with this transaction | [optional] 
**checkin_date** | **date** |  | [optional] 
**checkout_date** | **date** |  | [optional] 
**reservation_status** | [**ReservationStatus**](ReservationStatus.md) |  | [optional] 
**user** | [**UserModel**](UserModel.md) |  | [optional] 
**actions** | [**List[Action]**](Action.md) | Returns the list of actions available for the transaction | [optional] 
**payment_details** | [**PaymentDetails**](PaymentDetails.md) |  | [optional] 
**routing_context** | [**RoutingContext**](RoutingContext.md) |  | [optional] 
**locked** | **bool** | Whether transaction is locked by fiscal documents | [optional] 
**locked_by_fiscal_documents** | [**List[FiscalDocumentSummary]**](FiscalDocumentSummary.md) |  | [optional] 
**allocated_payments** | [**List[FolioPaymentAllocation]**](FolioPaymentAllocation.md) | Payment allocations for payment-type transactions. Only present for PAYMENT transactions. | [optional] 
**foreign_currency** | **str** | Original payment currency code when different from property currency | [optional] 
**foreign_currency_amount** | **float** | Amount in foreign currency | [optional] 

## Example

```python
from cloudbeds_accounting.models.folio_transaction_response import FolioTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FolioTransactionResponse from a JSON string
folio_transaction_response_instance = FolioTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(FolioTransactionResponse.to_json())

# convert the object into a dict
folio_transaction_response_dict = folio_transaction_response_instance.to_dict()
# create an instance of FolioTransactionResponse from a dict
folio_transaction_response_from_dict = FolioTransactionResponse.from_dict(folio_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


