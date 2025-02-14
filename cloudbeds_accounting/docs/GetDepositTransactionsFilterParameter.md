# GetDepositTransactionsFilterParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_states** | [**List[TransactionState]**](TransactionState.md) | transaction states | [optional] 
**include_inactive** | **bool** | Include inactive transactions (voided, consumed, cancelled, deleted) | [optional] [default to True]
**reservation_id** | **int** |  | [optional] 
**transaction_date_from** | **date** |  | [optional] 
**transaction_date_to** | **date** |  | [optional] 
**checkin_date_from** | **date** |  | [optional] 
**checkin_date_to** | **date** |  | [optional] 
**checkout_date_from** | **date** |  | [optional] 
**checkout_date_to** | **date** |  | [optional] 
**reservation_status** | [**ReservationStatus**](ReservationStatus.md) |  | [optional] 
**user_id** | **List[int]** |  | [optional] 
**sort_by** | **str** | Sort field | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.get_deposit_transactions_filter_parameter import GetDepositTransactionsFilterParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GetDepositTransactionsFilterParameter from a JSON string
get_deposit_transactions_filter_parameter_instance = GetDepositTransactionsFilterParameter.from_json(json)
# print the JSON string representation of the object
print(GetDepositTransactionsFilterParameter.to_json())

# convert the object into a dict
get_deposit_transactions_filter_parameter_dict = get_deposit_transactions_filter_parameter_instance.to_dict()
# create an instance of GetDepositTransactionsFilterParameter from a dict
get_deposit_transactions_filter_parameter_from_dict = GetDepositTransactionsFilterParameter.from_dict(get_deposit_transactions_filter_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


