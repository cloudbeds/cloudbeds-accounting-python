# AccountsReceivableTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the transaction. | [optional] 
**transaction_date** | **datetime** | Date time of the transaction. | [optional] 
**amount** | **float** | amount of the transaction. | [optional] 
**internal_transaction_code** | **str** | Internal Transaction Code | [optional] 
**description** | **str** | Description | [optional] 
**notes** | **str** | Notes | [optional] 
**currency** | **str** | Currency ISO code | [optional] 
**currency_scale** | **int** | Number of decimal places for the currency. | [optional] 
**posted** | **bool** | Flag to mark if transaction is posted | [optional] 
**user** | [**UserModel**](UserModel.md) |  | [optional] 
**actions** | [**List[Action]**](Action.md) | Returns the list of actions available for the transaction | [optional] 
**transfer_details** | [**AccountsReceivableTransactionResponseTransferDetails**](AccountsReceivableTransactionResponseTransferDetails.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.accounts_receivable_transaction_response import AccountsReceivableTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsReceivableTransactionResponse from a JSON string
accounts_receivable_transaction_response_instance = AccountsReceivableTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(AccountsReceivableTransactionResponse.to_json())

# convert the object into a dict
accounts_receivable_transaction_response_dict = accounts_receivable_transaction_response_instance.to_dict()
# create an instance of AccountsReceivableTransactionResponse from a dict
accounts_receivable_transaction_response_from_dict = AccountsReceivableTransactionResponse.from_dict(accounts_receivable_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


