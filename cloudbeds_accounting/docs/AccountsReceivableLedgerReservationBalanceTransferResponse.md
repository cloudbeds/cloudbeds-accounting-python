# AccountsReceivableLedgerReservationBalanceTransferResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**AccountsReceivableLedgerReservationBalanceTransferResponseTransaction**](AccountsReceivableLedgerReservationBalanceTransferResponseTransaction.md) |  | [optional] 
**accounts_receivable_id** | **str** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.accounts_receivable_ledger_reservation_balance_transfer_response import AccountsReceivableLedgerReservationBalanceTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsReceivableLedgerReservationBalanceTransferResponse from a JSON string
accounts_receivable_ledger_reservation_balance_transfer_response_instance = AccountsReceivableLedgerReservationBalanceTransferResponse.from_json(json)
# print the JSON string representation of the object
print(AccountsReceivableLedgerReservationBalanceTransferResponse.to_json())

# convert the object into a dict
accounts_receivable_ledger_reservation_balance_transfer_response_dict = accounts_receivable_ledger_reservation_balance_transfer_response_instance.to_dict()
# create an instance of AccountsReceivableLedgerReservationBalanceTransferResponse from a dict
accounts_receivable_ledger_reservation_balance_transfer_response_from_dict = AccountsReceivableLedgerReservationBalanceTransferResponse.from_dict(accounts_receivable_ledger_reservation_balance_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


