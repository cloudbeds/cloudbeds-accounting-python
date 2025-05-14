# ExtendedTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the transaction. | [optional] 
**transaction_date** | **datetime** | Date time of the transaction. | [optional] 
**reservation_name** | **str** | reservation name. | [optional] 
**checkin_date** | **date** | Check in date. | [optional] 
**checkout_date** | **date** | Check out date. | [optional] 
**amount** | **float** | amount of the transaction. | [optional] 
**reservation_id** | **str** | Id of reservation | [optional] 
**reservation_identifier** | **str** | Identifier of reservation | [optional] 
**internal_transaction_code** | **str** | Internal Transaction Code | [optional] 
**description** | **str** | Description | [optional] 
**notes** | **str** | Notes | [optional] 
**folio_id** | **str** | Folio ID | [optional] 
**state** | **str** |  | [optional] 
**currency** | **str** | Currency ISO code | [optional] 
**currency_scale** | **int** | Number of decimal places for the currency. | [optional] 
**reservation_status** | [**ReservationStatus**](ReservationStatus.md) |  | [optional] 
**posted** | **bool** | Flag to mark if transaction is posted | [optional] 
**user** | [**UserModel**](UserModel.md) |  | [optional] 
**actions** | [**List[Action]**](Action.md) | Returns the list of actions available for the transaction | [optional] 

## Example

```python
from cloudbeds_accounting.models.extended_transaction_response import ExtendedTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedTransactionResponse from a JSON string
extended_transaction_response_instance = ExtendedTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(ExtendedTransactionResponse.to_json())

# convert the object into a dict
extended_transaction_response_dict = extended_transaction_response_instance.to_dict()
# create an instance of ExtendedTransactionResponse from a dict
extended_transaction_response_from_dict = ExtendedTransactionResponse.from_dict(extended_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


