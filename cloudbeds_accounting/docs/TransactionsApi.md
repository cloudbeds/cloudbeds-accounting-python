# cloudbeds_accounting.TransactionsApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_transactions**](TransactionsApi.md#list_transactions) | **POST** /accounting/v1.0/transactions | 


# **list_transactions**
> ListTransactionsPaginated list_transactions(x_property_id, list_transactions_request)



Supported fields for filtering:   - account_category   - chart_of_account_type   - created_at - Same as `transaction_datetime`   - customer_id   - custom_code   - external_relation_id   - external_relation_kind   - folio_id   - id   - internal_code   - origin_id   - parent_id   - routed_from   - source_id   - source_identifier   - source_kind   - transaction_datetime   - trial_balance_id  Supported fields for sorting:   - created_at - Same as `transaction_datetime`   - id   - internal_code   - source_id   - transaction_datetime  Example request: ```   {     \"filters\": {       \"and\": [         {           \"operator\": \"greater_than_or_equal\",           \"value\": \"2019-01-11t08:59:00Z\",           \"field\": \"transaction_datetime\"         },         {           \"operator\": \"equals\",           \"value\": \"123\",           \"field\": \"source_id\"         },         {           \"operator\": \"equals\",           \"value\": \"RESERVATION\",           \"field\": \"source_kind\"         },         {           \"or\": [             {               \"operator\": \"in\",               \"value\": [\"1\", \"2\", \"3\"],               \"field\": \"customer_id\"             },             {               \"operator\": \"equals\",               \"value\": \"9000\",               \"field\": \"internal_code\"             }           ]         }       ]     },     \"pageToken\": null,     \"limit\": 10,     \"sort\": [       {         \"field\": \"transaction_datetime\",         \"direction\": \"asc\"       }     ]   }  The API has certain constraints for filters so that the system is able to efficiently query the data. Filters must include on of the following:   - filter by 'id' with condition 'equals' or 'in'   - filter by both 'source_id' and 'source_kind'   - filter by both 'external_relation_id' and 'external_relation_kind'   - filter by transaction_datetime ``` 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.list_transactions_paginated import ListTransactionsPaginated
from cloudbeds_accounting.models.list_transactions_request import ListTransactionsRequest
from cloudbeds_accounting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds-stage.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_accounting.Configuration(
    host = "https://api.cloudbeds-stage.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_accounting.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.TransactionsApi(api_client)
    x_property_id = 56 # int | Property id
    list_transactions_request = cloudbeds_accounting.ListTransactionsRequest() # ListTransactionsRequest | 

    try:
        api_response = api_instance.list_transactions(x_property_id, list_transactions_request)
        print("The response of TransactionsApi->list_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **list_transactions_request** | [**ListTransactionsRequest**](ListTransactionsRequest.md)|  | 

### Return type

[**ListTransactionsPaginated**](ListTransactionsPaginated.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

