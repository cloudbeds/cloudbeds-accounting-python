# TransferDepositPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[str]** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.transfer_deposit_post_request import TransferDepositPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferDepositPostRequest from a JSON string
transfer_deposit_post_request_instance = TransferDepositPostRequest.from_json(json)
# print the JSON string representation of the object
print(TransferDepositPostRequest.to_json())

# convert the object into a dict
transfer_deposit_post_request_dict = transfer_deposit_post_request_instance.to_dict()
# create an instance of TransferDepositPostRequest from a dict
transfer_deposit_post_request_from_dict = TransferDepositPostRequest.from_dict(transfer_deposit_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


