# ListPendingTransactionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**Filters**](Filters.md) |  | 
**page_token** | **str** |  | [optional] 
**limit** | **int** | Optional parameter. Default value is 100, maximum value is 1100. | [optional] [default to 100]
**sort** | [**List[Sort]**](Sort.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.list_pending_transactions_request import ListPendingTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListPendingTransactionsRequest from a JSON string
list_pending_transactions_request_instance = ListPendingTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListPendingTransactionsRequest.to_json())

# convert the object into a dict
list_pending_transactions_request_dict = list_pending_transactions_request_instance.to_dict()
# create an instance of ListPendingTransactionsRequest from a dict
list_pending_transactions_request_from_dict = ListPendingTransactionsRequest.from_dict(list_pending_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


