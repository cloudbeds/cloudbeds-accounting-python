# RouteTransactionsRequest

Request to route reservation transactions to a group profile folio. At least one of `transactions` or `transactionTypes` must be provided and non-empty. Route operation binds reservation transactions to a group profile. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **int** | Reservation ID (source of the transactions to route) | 
**group_profile_id** | **int** | Group profile ID (target of the routing) | 
**target_folio_id** | **int** | Target folio ID where transactions will be assigned | 
**transactions** | **List[int]** | List of transaction IDs to route. Required if transactionTypes is not provided. | [optional] 
**transaction_types** | [**List[TransactionTypeIdentifier]**](TransactionTypeIdentifier.md) | List of transaction types to route (by origin ID and external relation kind). Required if transactions is not provided. | [optional] 

## Example

```python
from cloudbeds_accounting.models.route_transactions_request import RouteTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTransactionsRequest from a JSON string
route_transactions_request_instance = RouteTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(RouteTransactionsRequest.to_json())

# convert the object into a dict
route_transactions_request_dict = route_transactions_request_instance.to_dict()
# create an instance of RouteTransactionsRequest from a dict
route_transactions_request_from_dict = RouteTransactionsRequest.from_dict(route_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


