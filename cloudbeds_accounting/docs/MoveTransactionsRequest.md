# MoveTransactionsRequest

Request to move transactions to a target folio. At least one of `transactions` or `transactionTypes` must be provided and non-empty. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_kind** | [**SourceKind**](SourceKind.md) |  | 
**source_id** | **int** | Source ID (reservation ID, group profile ID, etc.) | 
**target_folio_id** | **int** | Target folio ID where transactions will be moved | 
**transactions** | **List[int]** | List of transaction IDs to move. Required if transactionTypes is not provided. | [optional] 
**transaction_types** | [**List[TransactionTypeIdentifier]**](TransactionTypeIdentifier.md) | List of transaction types to move (by origin ID and external relation kind). Required if transactions is not provided. | [optional] 

## Example

```python
from cloudbeds_accounting.models.move_transactions_request import MoveTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MoveTransactionsRequest from a JSON string
move_transactions_request_instance = MoveTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(MoveTransactionsRequest.to_json())

# convert the object into a dict
move_transactions_request_dict = move_transactions_request_instance.to_dict()
# create an instance of MoveTransactionsRequest from a dict
move_transactions_request_from_dict = MoveTransactionsRequest.from_dict(move_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


