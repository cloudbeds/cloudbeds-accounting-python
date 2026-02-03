# AccountsReceivableTransactionResponseTransferDetails

Reservation or Group Profile details for which the transfer was made.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation** | [**ReservationTransferDetails**](ReservationTransferDetails.md) |  | [optional] 
**group_profile** | [**GroupProfileTransferDetails**](GroupProfileTransferDetails.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.accounts_receivable_transaction_response_transfer_details import AccountsReceivableTransactionResponseTransferDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsReceivableTransactionResponseTransferDetails from a JSON string
accounts_receivable_transaction_response_transfer_details_instance = AccountsReceivableTransactionResponseTransferDetails.from_json(json)
# print the JSON string representation of the object
print(AccountsReceivableTransactionResponseTransferDetails.to_json())

# convert the object into a dict
accounts_receivable_transaction_response_transfer_details_dict = accounts_receivable_transaction_response_transfer_details_instance.to_dict()
# create an instance of AccountsReceivableTransactionResponseTransferDetails from a dict
accounts_receivable_transaction_response_transfer_details_from_dict = AccountsReceivableTransactionResponseTransferDetails.from_dict(accounts_receivable_transaction_response_transfer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


