# ExtendedTransactionPaginated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[ExtendedTransactionResponse]**](ExtendedTransactionResponse.md) |  | [optional] 
**next_page_token** | **str** | Token for fetching the next page of results | [optional] 

## Example

```python
from cloudbeds_accounting.models.extended_transaction_paginated import ExtendedTransactionPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedTransactionPaginated from a JSON string
extended_transaction_paginated_instance = ExtendedTransactionPaginated.from_json(json)
# print the JSON string representation of the object
print(ExtendedTransactionPaginated.to_json())

# convert the object into a dict
extended_transaction_paginated_dict = extended_transaction_paginated_instance.to_dict()
# create an instance of ExtendedTransactionPaginated from a dict
extended_transaction_paginated_from_dict = ExtendedTransactionPaginated.from_dict(extended_transaction_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


