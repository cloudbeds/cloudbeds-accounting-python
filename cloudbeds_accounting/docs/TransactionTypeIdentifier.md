# TransactionTypeIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin_id** | **str** | Origin ID of the transaction type | 
**external_relation_kind** | [**ExternalRelationKind**](ExternalRelationKind.md) |  | 

## Example

```python
from cloudbeds_accounting.models.transaction_type_identifier import TransactionTypeIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTypeIdentifier from a JSON string
transaction_type_identifier_instance = TransactionTypeIdentifier.from_json(json)
# print the JSON string representation of the object
print(TransactionTypeIdentifier.to_json())

# convert the object into a dict
transaction_type_identifier_dict = transaction_type_identifier_instance.to_dict()
# create an instance of TransactionTypeIdentifier from a dict
transaction_type_identifier_from_dict = TransactionTypeIdentifier.from_dict(transaction_type_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


