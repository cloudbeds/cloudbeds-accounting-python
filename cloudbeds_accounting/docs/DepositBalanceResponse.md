# DepositBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posted_balance** | **float** | Posted balance in smallest unit according to the currency. | [optional] 
**pending_balance** | **float** | Pending balance in smallest unit according to the currency. | [optional] 

## Example

```python
from cloudbeds_accounting.models.deposit_balance_response import DepositBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DepositBalanceResponse from a JSON string
deposit_balance_response_instance = DepositBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(DepositBalanceResponse.to_json())

# convert the object into a dict
deposit_balance_response_dict = deposit_balance_response_instance.to_dict()
# create an instance of DepositBalanceResponse from a dict
deposit_balance_response_from_dict = DepositBalanceResponse.from_dict(deposit_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


