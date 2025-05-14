# TransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the transaction. | [optional] 
**property_id** | **str** | Property ID where the transaction was created. | [optional] 
**internal_transaction_code** | **str** | Internal code for the transaction, managed by Cloudbeds. | [optional] 
**custom_transaction_code** | **str** | Custom code for the transaction, managed by Property. | [optional] 
**general_ledger_custom_code** | **str** | Custom code for general ledger, managed by Property. | [optional] 
**amount** | **float** | Amount of the transaction. | [optional] 
**currency_scale** | **int** | Number of decimal places for the currency. | [optional] 
**currency** | **str** | Currency (ISO code) applied to the amount of the transaction. | [optional] 
**customer_id** | **str** | Id of the user who perform the transaction, also know as guest id. | [optional] 
**root_id** | **str** | Root Id of the transaction, it contains the id of the transaction that is related to it. | [optional] 
**parent_id** | **str** | Id of the transaction that is parent of this one. For example Tax on top of a rate, tax on top of a fee, etc. | [optional] 
**source_id** | **str** | Id of the source. It is related with the source_kind, so if sourceKind is RESERVATION, is the reservation id. | [optional] 
**sub_source_id** | **str** | Id of the sub source. At the moment only for reservations that is the booking_room_id. | [optional] 
**source_kind** | [**SourceKind**](SourceKind.md) |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 
**external_relation_id** | **str** | External relation id, for example if the transaction is a payment it will contain payment id. | [optional] 
**external_relation_kind** | **str** | Kind of the external relation id, for example if transaction is a payment it will contain PAYMENT. | [optional] 
**origin_id** | **str** | Id of origin of the transaction. For example if the transaction is created based on a rate, is the rate id. | [optional] 
**routed_from** | **str** | Id of the transaction that was routed from. It can be null. | [optional] 
**quantity** | **int** | Amount of items purchased. | [optional] 
**description** | **str** | Description of the transaction. | [optional] 
**user_id** | **str** | ID of the user who created the transaction | [optional] 
**source_datetime** | **datetime** | Date time the source was created. (ISO 8601) in UTC | [optional] 
**transaction_datetime** | **datetime** | Date time when the transaction should be created at. (ISO 8601) in UTC | [optional] 
**transaction_datetime_property_time** | **datetime** | Date time when the transaction should be created at base on the property timezone. | [optional] 
**service_date** | **date** | Date when the posted transaction was created (property time). | [optional] 
**created_at** | **datetime** | Date time when the transaction was inserted on the database. (ISO 8601) in UTC | [optional] 
**source_identifier** | **str** | If source_kind &#x3D; RESERVATION, this field will contain a reservation identifier. For a transaction with source_kind &#x3D; GROUP_PROFILE, this field will contain a group code. For source_king &#x3D; HOUSE_ACCOUNT it will be null. | [optional] 
**sub_source_identifier** | **str** | identifier of a booking room | [optional] 

## Example

```python
from cloudbeds_accounting.models.transaction_response import TransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponse from a JSON string
transaction_response_instance = TransactionResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionResponse.to_json())

# convert the object into a dict
transaction_response_dict = transaction_response_instance.to_dict()
# create an instance of TransactionResponse from a dict
transaction_response_from_dict = TransactionResponse.from_dict(transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


