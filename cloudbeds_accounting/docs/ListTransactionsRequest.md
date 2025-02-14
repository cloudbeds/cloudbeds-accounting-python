# ListTransactionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**Filters**](Filters.md) |  | 
**page_token** | **str** |  | [optional] 
**limit** | **int** | Optional parameter. Default value is 100, maximum value is 1100. | [optional] [default to 100]
**sort** | [**List[Sort]**](Sort.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.list_transactions_request import ListTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsRequest from a JSON string
list_transactions_request_instance = ListTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListTransactionsRequest.to_json())

# convert the object into a dict
list_transactions_request_dict = list_transactions_request_instance.to_dict()
# create an instance of ListTransactionsRequest from a dict
list_transactions_request_from_dict = ListTransactionsRequest.from_dict(list_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


