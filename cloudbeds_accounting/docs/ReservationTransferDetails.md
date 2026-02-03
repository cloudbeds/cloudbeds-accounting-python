# ReservationTransferDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reservation ID. | [optional] 
**identifier** | **str** | Reservation Identifier. | [optional] 
**guest_name** | **str** | Guest Name. | [optional] 
**status** | [**ReservationStatus**](ReservationStatus.md) |  | [optional] 
**checkin_date** | **date** | Check in date. | [optional] 
**checkout_date** | **date** | Checkout in date. | [optional] 

## Example

```python
from cloudbeds_accounting.models.reservation_transfer_details import ReservationTransferDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationTransferDetails from a JSON string
reservation_transfer_details_instance = ReservationTransferDetails.from_json(json)
# print the JSON string representation of the object
print(ReservationTransferDetails.to_json())

# convert the object into a dict
reservation_transfer_details_dict = reservation_transfer_details_instance.to_dict()
# create an instance of ReservationTransferDetails from a dict
reservation_transfer_details_from_dict = ReservationTransferDetails.from_dict(reservation_transfer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


