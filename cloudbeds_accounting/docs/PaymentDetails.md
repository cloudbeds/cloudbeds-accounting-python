# PaymentDetails

Payment-specific fields. Only present on transactions where internalCodeGroup=PAYMENT. Enriched via batch PaymentService lookup. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_type** | **str** | Payment processing transaction type | [optional] 
**payment_method** | **str** | Payment method code (e.g. \&quot;cash\&quot;, \&quot;cards\&quot;, \&quot;terminal\&quot;, \&quot;ebanking\&quot;, \&quot;pay_pal\&quot;, \&quot;oxxo\&quot;) | [optional] 
**gateway** | **str** | Payment gateway identifier (e.g. \&quot;StripeConnectGateway\&quot;, \&quot;AdyenGateway\&quot;) | [optional] 
**credit_card_type** | **str** | Card brand code (e.g. \&quot;visa\&quot;, \&quot;master\&quot;, \&quot;amex\&quot;) | [optional] 
**card_trailing_digits** | **str** | Last 4 digits of the card number | [optional] 
**amount_paid** | **float** | Total captured/paid amount | [optional] 
**amount_refunded** | **float** | Total refunded amount | [optional] 
**processing_status** | **str** | Payment processing status (for scheduled payments) | [optional] 

## Example

```python
from cloudbeds_accounting.models.payment_details import PaymentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDetails from a JSON string
payment_details_instance = PaymentDetails.from_json(json)
# print the JSON string representation of the object
print(PaymentDetails.to_json())

# convert the object into a dict
payment_details_dict = payment_details_instance.to_dict()
# create an instance of PaymentDetails from a dict
payment_details_from_dict = PaymentDetails.from_dict(payment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


