# InternalTransactionCodesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[InternalTransactionCodeResponse]**](InternalTransactionCodeResponse.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.internal_transaction_codes_list_response import InternalTransactionCodesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransactionCodesListResponse from a JSON string
internal_transaction_codes_list_response_instance = InternalTransactionCodesListResponse.from_json(json)
# print the JSON string representation of the object
print(InternalTransactionCodesListResponse.to_json())

# convert the object into a dict
internal_transaction_codes_list_response_dict = internal_transaction_codes_list_response_instance.to_dict()
# create an instance of InternalTransactionCodesListResponse from a dict
internal_transaction_codes_list_response_from_dict = InternalTransactionCodesListResponse.from_dict(internal_transaction_codes_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


