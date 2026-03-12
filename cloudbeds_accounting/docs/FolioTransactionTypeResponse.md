# FolioTransactionTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin_id** | **str** | Origin ID of the transaction type | [optional] 
**external_relation_kind** | [**ExternalRelationKind**](ExternalRelationKind.md) |  | [optional] 

## Example

```python
from cloudbeds_accounting.models.folio_transaction_type_response import FolioTransactionTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FolioTransactionTypeResponse from a JSON string
folio_transaction_type_response_instance = FolioTransactionTypeResponse.from_json(json)
# print the JSON string representation of the object
print(FolioTransactionTypeResponse.to_json())

# convert the object into a dict
folio_transaction_type_response_dict = folio_transaction_type_response_instance.to_dict()
# create an instance of FolioTransactionTypeResponse from a dict
folio_transaction_type_response_from_dict = FolioTransactionTypeResponse.from_dict(folio_transaction_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


