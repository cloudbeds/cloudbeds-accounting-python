# ListTransactionsPaginated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[TransactionResponse]**](TransactionResponse.md) |  | [optional] 
**next_page_token** | **str** | Token for fetching the next page of results | [optional] 

## Example

```python
from cloudbeds_accounting.models.list_transactions_paginated import ListTransactionsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsPaginated from a JSON string
list_transactions_paginated_instance = ListTransactionsPaginated.from_json(json)
# print the JSON string representation of the object
print(ListTransactionsPaginated.to_json())

# convert the object into a dict
list_transactions_paginated_dict = list_transactions_paginated_instance.to_dict()
# create an instance of ListTransactionsPaginated from a dict
list_transactions_paginated_from_dict = ListTransactionsPaginated.from_dict(list_transactions_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


