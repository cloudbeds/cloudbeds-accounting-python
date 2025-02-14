# cloudbeds_accounting.CustomGeneralLedgerCodesApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_general_ledger_codes**](CustomGeneralLedgerCodesApi.md#get_custom_general_ledger_codes) | **GET** /accounting/v1.0/custom-general-ledger-codes | 
[**put_custom_general_ledger_codes**](CustomGeneralLedgerCodesApi.md#put_custom_general_ledger_codes) | **PUT** /accounting/v1.0/custom-general-ledger-codes | 


# **get_custom_general_ledger_codes**
> List[CustomGeneralLedgerCodeModel] get_custom_general_ledger_codes(x_property_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.custom_general_ledger_code_model import CustomGeneralLedgerCodeModel
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
    api_instance = cloudbeds_accounting.CustomGeneralLedgerCodesApi(api_client)
    x_property_id = 56 # int | Property id

    try:
        api_response = api_instance.get_custom_general_ledger_codes(x_property_id)
        print("The response of CustomGeneralLedgerCodesApi->get_custom_general_ledger_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomGeneralLedgerCodesApi->get_custom_general_ledger_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 

### Return type

[**List[CustomGeneralLedgerCodeModel]**](CustomGeneralLedgerCodeModel.md)

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

# **put_custom_general_ledger_codes**
> put_custom_general_ledger_codes(x_property_id, custom_general_ledger_codes_update_request)



Create or update General Ledger Codes. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.custom_general_ledger_codes_update_request import CustomGeneralLedgerCodesUpdateRequest
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
    api_instance = cloudbeds_accounting.CustomGeneralLedgerCodesApi(api_client)
    x_property_id = 56 # int | Property id
    custom_general_ledger_codes_update_request = cloudbeds_accounting.CustomGeneralLedgerCodesUpdateRequest() # CustomGeneralLedgerCodesUpdateRequest | 

    try:
        api_instance.put_custom_general_ledger_codes(x_property_id, custom_general_ledger_codes_update_request)
    except Exception as e:
        print("Exception when calling CustomGeneralLedgerCodesApi->put_custom_general_ledger_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **custom_general_ledger_codes_update_request** | [**CustomGeneralLedgerCodesUpdateRequest**](CustomGeneralLedgerCodesUpdateRequest.md)|  | 

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

