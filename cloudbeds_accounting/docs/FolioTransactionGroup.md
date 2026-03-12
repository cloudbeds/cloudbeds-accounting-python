# FolioTransactionGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[FolioTransactionResponse]**](FolioTransactionResponse.md) |  | [optional] 
**totals** | [**FolioTransactionGroupTotals**](FolioTransactionGroupTotals.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.folio_transaction_group import FolioTransactionGroup

# TODO update the JSON string below
json = "{}"
# create an instance of FolioTransactionGroup from a JSON string
folio_transaction_group_instance = FolioTransactionGroup.from_json(json)
# print the JSON string representation of the object
print(FolioTransactionGroup.to_json())

# convert the object into a dict
folio_transaction_group_dict = folio_transaction_group_instance.to_dict()
# create an instance of FolioTransactionGroup from a dict
folio_transaction_group_from_dict = FolioTransactionGroup.from_dict(folio_transaction_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


