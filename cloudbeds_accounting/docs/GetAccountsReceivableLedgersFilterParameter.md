# GetAccountsReceivableLedgersFilterParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_query** | **str** |  | [optional] 
**created_date_time_from** | **datetime** |  | [optional] 
**created_date_time_to** | **datetime** |  | [optional] 
**balance_from** | **int** |  | [optional] 
**balance_to** | **int** |  | [optional] 
**total_from** | **int** |  | [optional] 
**total_to** | **int** |  | [optional] 
**paid_from** | **int** |  | [optional] 
**paid_to** | **int** |  | [optional] 
**status** | [**List[AccountsReceivableLedgerStatus]**](AccountsReceivableLedgerStatus.md) |  | [optional] 
**sort_by** | **str** | Sort field | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 
**page_token** | **str** |  | [optional] 
**page_size** | **int** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.get_accounts_receivable_ledgers_filter_parameter import GetAccountsReceivableLedgersFilterParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsReceivableLedgersFilterParameter from a JSON string
get_accounts_receivable_ledgers_filter_parameter_instance = GetAccountsReceivableLedgersFilterParameter.from_json(json)
# print the JSON string representation of the object
print(GetAccountsReceivableLedgersFilterParameter.to_json())

# convert the object into a dict
get_accounts_receivable_ledgers_filter_parameter_dict = get_accounts_receivable_ledgers_filter_parameter_instance.to_dict()
# create an instance of GetAccountsReceivableLedgersFilterParameter from a dict
get_accounts_receivable_ledgers_filter_parameter_from_dict = GetAccountsReceivableLedgersFilterParameter.from_dict(get_accounts_receivable_ledgers_filter_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


