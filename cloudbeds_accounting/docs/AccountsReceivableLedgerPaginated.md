# AccountsReceivableLedgerPaginated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[AccountsReceivableLedgerResponse]**](AccountsReceivableLedgerResponse.md) |  | [optional] 
**next_page_token** | **str** | Token for fetching the next page of results | [optional] 

## Example

```python
from cloudbeds_accounting.models.accounts_receivable_ledger_paginated import AccountsReceivableLedgerPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsReceivableLedgerPaginated from a JSON string
accounts_receivable_ledger_paginated_instance = AccountsReceivableLedgerPaginated.from_json(json)
# print the JSON string representation of the object
print(AccountsReceivableLedgerPaginated.to_json())

# convert the object into a dict
accounts_receivable_ledger_paginated_dict = accounts_receivable_ledger_paginated_instance.to_dict()
# create an instance of AccountsReceivableLedgerPaginated from a dict
accounts_receivable_ledger_paginated_from_dict = AccountsReceivableLedgerPaginated.from_dict(accounts_receivable_ledger_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


