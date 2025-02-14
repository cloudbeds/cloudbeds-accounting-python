# ApiAccountingError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**error_code** | [**ApiErrorCode**](ApiErrorCode.md) |  | [optional] 
**error_details** | **str** |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.api_accounting_error import ApiAccountingError

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAccountingError from a JSON string
api_accounting_error_instance = ApiAccountingError.from_json(json)
# print the JSON string representation of the object
print(ApiAccountingError.to_json())

# convert the object into a dict
api_accounting_error_dict = api_accounting_error_instance.to_dict()
# create an instance of ApiAccountingError from a dict
api_accounting_error_from_dict = ApiAccountingError.from_dict(api_accounting_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


