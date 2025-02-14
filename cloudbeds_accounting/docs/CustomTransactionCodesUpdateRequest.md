# CustomTransactionCodesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomTransactionCodesUpdateModel]**](CustomTransactionCodesUpdateModel.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.custom_transaction_codes_update_request import CustomTransactionCodesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTransactionCodesUpdateRequest from a JSON string
custom_transaction_codes_update_request_instance = CustomTransactionCodesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomTransactionCodesUpdateRequest.to_json())

# convert the object into a dict
custom_transaction_codes_update_request_dict = custom_transaction_codes_update_request_instance.to_dict()
# create an instance of CustomTransactionCodesUpdateRequest from a dict
custom_transaction_codes_update_request_from_dict = CustomTransactionCodesUpdateRequest.from_dict(custom_transaction_codes_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


