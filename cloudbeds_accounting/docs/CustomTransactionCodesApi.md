# cloudbeds_accounting.CustomTransactionCodesApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_transaction_codes**](CustomTransactionCodesApi.md#get_custom_transaction_codes) | **GET** /accounting/v1.0/custom-transaction-codes | List custom transaction codes
[**initialize_custom_transaction_codes**](CustomTransactionCodesApi.md#initialize_custom_transaction_codes) | **POST** /accounting/v1.0/custom-transaction-codes/initialize | Initialize custom transaction codes
[**put_custom_transaction_codes**](CustomTransactionCodesApi.md#put_custom_transaction_codes) | **PUT** /accounting/v1.0/custom-transaction-codes | Update custom transaction code mappings


# **get_custom_transaction_codes**
> List[CustomTransactionCodesModel] get_custom_transaction_codes(x_property_id)

List custom transaction codes

Retrieve all custom transaction code mappings for a property. Custom transaction codes let you assign your own codes to each Cloudbeds internal transaction type (e.g., room rate, tax, payment method). You must call the initialize endpoint before codes can be retrieved for the first time.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.custom_transaction_codes_model import CustomTransactionCodesModel
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.CustomTransactionCodesApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 

    try:
        # List custom transaction codes
        api_response = api_instance.get_custom_transaction_codes(x_property_id)
        print("The response of CustomTransactionCodesApi->get_custom_transaction_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTransactionCodesApi->get_custom_transaction_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 

### Return type

[**List[CustomTransactionCodesModel]**](CustomTransactionCodesModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_custom_transaction_codes**
> initialize_custom_transaction_codes(x_property_id)

Initialize custom transaction codes

Initialize custom transaction code records for a property. You must call this endpoint before you can retrieve or update custom transaction codes. Initialization creates a record for each internal transaction type with an empty custom code mapping. If codes have already been initialized, this endpoint has no additional effect.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.CustomTransactionCodesApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 

    try:
        # Initialize custom transaction codes
        api_instance.initialize_custom_transaction_codes(x_property_id)
    except Exception as e:
        print("Exception when calling CustomTransactionCodesApi->initialize_custom_transaction_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_custom_transaction_codes**
> put_custom_transaction_codes(x_property_id, custom_transaction_codes_update_request)

Update custom transaction code mappings

Update custom transaction code mappings for a property. For each mapping, provide the record ID and the new custom code value. You can also optionally assign a custom general ledger code to each transaction code. Only the mappings you include in the request are updated; others remain unchanged.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.custom_transaction_codes_update_request import CustomTransactionCodesUpdateRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.CustomTransactionCodesApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    custom_transaction_codes_update_request = cloudbeds_accounting.CustomTransactionCodesUpdateRequest() # CustomTransactionCodesUpdateRequest | 

    try:
        # Update custom transaction code mappings
        api_instance.put_custom_transaction_codes(x_property_id, custom_transaction_codes_update_request)
    except Exception as e:
        print("Exception when calling CustomTransactionCodesApi->put_custom_transaction_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **custom_transaction_codes_update_request** | [**CustomTransactionCodesUpdateRequest**](CustomTransactionCodesUpdateRequest.md)|  | 

### Return type

void (empty response body)

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

