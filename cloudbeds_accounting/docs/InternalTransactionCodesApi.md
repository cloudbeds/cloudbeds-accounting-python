# cloudbeds_accounting.InternalTransactionCodesApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_internal_transaction_codes**](InternalTransactionCodesApi.md#get_internal_transaction_codes) | **GET** /accounting/v1.0/internal-transaction-codes | 


# **get_internal_transaction_codes**
> InternalTransactionCodesListResponse get_internal_transaction_codes()



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.internal_transaction_codes_list_response import InternalTransactionCodesListResponse
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
    api_instance = cloudbeds_accounting.InternalTransactionCodesApi(api_client)

    try:
        api_response = api_instance.get_internal_transaction_codes()
        print("The response of InternalTransactionCodesApi->get_internal_transaction_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalTransactionCodesApi->get_internal_transaction_codes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InternalTransactionCodesListResponse**](InternalTransactionCodesListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

