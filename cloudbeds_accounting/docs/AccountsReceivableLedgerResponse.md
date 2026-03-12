# AccountsReceivableLedgerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | [**AccountsReceivableLedgerStatus**](AccountsReceivableLedgerStatus.md) |  | [optional] 
**property_id** | **str** |  | [optional] 
**profile_id** | **str** | Profile ID associated with this accounts receivable ledger | [optional] 
**total** | **float** | Total amount of all charges transferred to this AR ledger, in the smallest currency unit. | [optional] 
**paid** | **float** | Total amount of payments applied to this AR ledger, in the smallest currency unit. | [optional] 
**balance** | **float** | Outstanding balance (total minus paid), in the smallest currency unit. | [optional] 
**created_at** | **str** | Created datetime (ISO 8601) in UTC | [optional] 
**updated_at** | **str** | Updated datetime (ISO 8601) in UTC | [optional] 

## Example

```python
from cloudbeds_accounting.models.accounts_receivable_ledger_response import AccountsReceivableLedgerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsReceivableLedgerResponse from a JSON string
accounts_receivable_ledger_response_instance = AccountsReceivableLedgerResponse.from_json(json)
# print the JSON string representation of the object
print(AccountsReceivableLedgerResponse.to_json())

# convert the object into a dict
accounts_receivable_ledger_response_dict = accounts_receivable_ledger_response_instance.to_dict()
# create an instance of AccountsReceivableLedgerResponse from a dict
accounts_receivable_ledger_response_from_dict = AccountsReceivableLedgerResponse.from_dict(accounts_receivable_ledger_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


