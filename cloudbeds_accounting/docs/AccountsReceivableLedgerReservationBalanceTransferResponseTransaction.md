# AccountsReceivableLedgerReservationBalanceTransferResponseTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Posted transaction id | [optional] 
**amount** | **float** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.accounts_receivable_ledger_reservation_balance_transfer_response_transaction import AccountsReceivableLedgerReservationBalanceTransferResponseTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsReceivableLedgerReservationBalanceTransferResponseTransaction from a JSON string
accounts_receivable_ledger_reservation_balance_transfer_response_transaction_instance = AccountsReceivableLedgerReservationBalanceTransferResponseTransaction.from_json(json)
# print the JSON string representation of the object
print(AccountsReceivableLedgerReservationBalanceTransferResponseTransaction.to_json())

# convert the object into a dict
accounts_receivable_ledger_reservation_balance_transfer_response_transaction_dict = accounts_receivable_ledger_reservation_balance_transfer_response_transaction_instance.to_dict()
# create an instance of AccountsReceivableLedgerReservationBalanceTransferResponseTransaction from a dict
accounts_receivable_ledger_reservation_balance_transfer_response_transaction_from_dict = AccountsReceivableLedgerReservationBalanceTransferResponseTransaction.from_dict(accounts_receivable_ledger_reservation_balance_transfer_response_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


