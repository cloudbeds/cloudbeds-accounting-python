# GetAccountsReceivableLedgerTransactionsFilterParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_states** | [**List[TransactionState]**](TransactionState.md) | transaction states | [optional] 
**search_query** | **str** |  | [optional] 
**transaction_date_from** | **date** |  | [optional] 
**transaction_date_to** | **date** |  | [optional] 
**checkin_date_from** | **date** |  | [optional] 
**checkin_date_to** | **date** |  | [optional] 
**checkout_date_from** | **date** |  | [optional] 
**checkout_date_to** | **date** |  | [optional] 
**transaction_type** | **List[str]** |  | [optional] 
**user_id** | **List[int]** |  | [optional] 
**sort_by** | **str** | Sort field | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.get_accounts_receivable_ledger_transactions_filter_parameter import GetAccountsReceivableLedgerTransactionsFilterParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsReceivableLedgerTransactionsFilterParameter from a JSON string
get_accounts_receivable_ledger_transactions_filter_parameter_instance = GetAccountsReceivableLedgerTransactionsFilterParameter.from_json(json)
# print the JSON string representation of the object
print(GetAccountsReceivableLedgerTransactionsFilterParameter.to_json())

# convert the object into a dict
get_accounts_receivable_ledger_transactions_filter_parameter_dict = get_accounts_receivable_ledger_transactions_filter_parameter_instance.to_dict()
# create an instance of GetAccountsReceivableLedgerTransactionsFilterParameter from a dict
get_accounts_receivable_ledger_transactions_filter_parameter_from_dict = GetAccountsReceivableLedgerTransactionsFilterParameter.from_dict(get_accounts_receivable_ledger_transactions_filter_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


