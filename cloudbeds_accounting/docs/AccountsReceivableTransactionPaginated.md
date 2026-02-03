# AccountsReceivableTransactionPaginated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[AccountsReceivableTransactionResponse]**](AccountsReceivableTransactionResponse.md) |  | [optional] 
**next_page_token** | **str** | Token for fetching the next page of results | [optional] 

## Example

```python
from cloudbeds_accounting.models.accounts_receivable_transaction_paginated import AccountsReceivableTransactionPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsReceivableTransactionPaginated from a JSON string
accounts_receivable_transaction_paginated_instance = AccountsReceivableTransactionPaginated.from_json(json)
# print the JSON string representation of the object
print(AccountsReceivableTransactionPaginated.to_json())

# convert the object into a dict
accounts_receivable_transaction_paginated_dict = accounts_receivable_transaction_paginated_instance.to_dict()
# create an instance of AccountsReceivableTransactionPaginated from a dict
accounts_receivable_transaction_paginated_from_dict = AccountsReceivableTransactionPaginated.from_dict(accounts_receivable_transaction_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


