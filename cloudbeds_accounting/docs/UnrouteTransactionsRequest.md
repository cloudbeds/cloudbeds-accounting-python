# UnrouteTransactionsRequest

Request to unroute transactions from a group profile back to the original reservation. Only transaction IDs are supported (no transaction types). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | **List[int]** | List of transaction IDs to unroute from the group profile. | 

## Example

```python
from cloudbeds_accounting.models.unroute_transactions_request import UnrouteTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnrouteTransactionsRequest from a JSON string
unroute_transactions_request_instance = UnrouteTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(UnrouteTransactionsRequest.to_json())

# convert the object into a dict
unroute_transactions_request_dict = unroute_transactions_request_instance.to_dict()
# create an instance of UnrouteTransactionsRequest from a dict
unroute_transactions_request_from_dict = UnrouteTransactionsRequest.from_dict(unroute_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


