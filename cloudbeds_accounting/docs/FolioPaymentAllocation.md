# FolioPaymentAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**allocated_amount** | **int** | Amount allocated in smallest currency unit | [optional] 
**transaction_id** | **str** | ID of the transaction (invoice/expense) this payment is allocated to | [optional] 
**description** | **str** | Description of the allocated transaction | [optional] 
**total_to_allocate** | **int** | Total amount of the allocated transaction in smallest currency unit | [optional] 

## Example

```python
from cloudbeds_accounting.models.folio_payment_allocation import FolioPaymentAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of FolioPaymentAllocation from a JSON string
folio_payment_allocation_instance = FolioPaymentAllocation.from_json(json)
# print the JSON string representation of the object
print(FolioPaymentAllocation.to_json())

# convert the object into a dict
folio_payment_allocation_dict = folio_payment_allocation_instance.to_dict()
# create an instance of FolioPaymentAllocation from a dict
folio_payment_allocation_from_dict = FolioPaymentAllocation.from_dict(folio_payment_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


