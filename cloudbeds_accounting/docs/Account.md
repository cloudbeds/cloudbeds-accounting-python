# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of account | [optional] 
**description** | **str** | Description of the account | [optional] 
**name** | **str** | Name of the account | [optional] 
**category** | [**AccountCategory**](AccountCategory.md) |  | [optional] 
**chart_of_account_type** | [**ChartOfAccountType**](ChartOfAccountType.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


