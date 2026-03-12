# ForeignCurrencyTotals

Multi-currency totals across all matching transactions (all pages).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debit** | **Dict[str, float]** | Map of currency code to total debit amount (e.g. {\&quot;RON\&quot;: 724.82, \&quot;EUR\&quot;: 5}) | [optional] 
**credit** | **Dict[str, float]** | Map of currency code to total credit amount | [optional] 

## Example

```python
from cloudbeds_accounting.models.foreign_currency_totals import ForeignCurrencyTotals

# TODO update the JSON string below
json = "{}"
# create an instance of ForeignCurrencyTotals from a JSON string
foreign_currency_totals_instance = ForeignCurrencyTotals.from_json(json)
# print the JSON string representation of the object
print(ForeignCurrencyTotals.to_json())

# convert the object into a dict
foreign_currency_totals_dict = foreign_currency_totals_instance.to_dict()
# create an instance of ForeignCurrencyTotals from a dict
foreign_currency_totals_from_dict = ForeignCurrencyTotals.from_dict(foreign_currency_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


