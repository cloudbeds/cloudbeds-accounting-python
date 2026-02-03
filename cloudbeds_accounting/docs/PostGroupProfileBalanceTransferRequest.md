# PostGroupProfileBalanceTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folio_id** | **int** | Group profile folio ID | [optional] 

## Example

```python
from cloudbeds_accounting.models.post_group_profile_balance_transfer_request import PostGroupProfileBalanceTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGroupProfileBalanceTransferRequest from a JSON string
post_group_profile_balance_transfer_request_instance = PostGroupProfileBalanceTransferRequest.from_json(json)
# print the JSON string representation of the object
print(PostGroupProfileBalanceTransferRequest.to_json())

# convert the object into a dict
post_group_profile_balance_transfer_request_dict = post_group_profile_balance_transfer_request_instance.to_dict()
# create an instance of PostGroupProfileBalanceTransferRequest from a dict
post_group_profile_balance_transfer_request_from_dict = PostGroupProfileBalanceTransferRequest.from_dict(post_group_profile_balance_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


