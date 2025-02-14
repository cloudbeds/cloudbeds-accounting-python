# InternalTransactionCodeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**group** | [**InternalTransactionCodeGroupEnum**](InternalTransactionCodeGroupEnum.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.internal_transaction_code_response import InternalTransactionCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransactionCodeResponse from a JSON string
internal_transaction_code_response_instance = InternalTransactionCodeResponse.from_json(json)
# print the JSON string representation of the object
print(InternalTransactionCodeResponse.to_json())

# convert the object into a dict
internal_transaction_code_response_dict = internal_transaction_code_response_instance.to_dict()
# create an instance of InternalTransactionCodeResponse from a dict
internal_transaction_code_response_from_dict = InternalTransactionCodeResponse.from_dict(internal_transaction_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


