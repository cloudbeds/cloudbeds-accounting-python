# cloudbeds_accounting.SourceBalanceApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_source_balance_by_source**](SourceBalanceApi.md#get_source_balance_by_source) | **GET** /accounting/v1.0/source-balances/{sourceKind}/{sourceId} | 


# **get_source_balance_by_source**
> SourceBalanceResponse get_source_balance_by_source(x_property_id, source_kind, source_id, accept_language=accept_language)



Get source balance information for a reservation / house account / group profile / accounts receivable ledger

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.source_balance_response import SourceBalanceResponse
from cloudbeds_accounting.models.source_kind import SourceKind
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
    api_instance = cloudbeds_accounting.SourceBalanceApi(api_client)
    x_property_id = 56 # int | Property id
    source_kind = cloudbeds_accounting.SourceKind() # SourceKind | 
    source_id = 56 # int | Reservation ID | House Account ID | Group Profile ID | Accounts Receivable Ledger ID
    accept_language = en-US # str | Language preference for localized tax/fee names. Supports: en-US (English US), es-ES (Spanish Spain), es-MX (Spanish Mexico),  fr-FR (French), de-DE (German), it-IT (Italian), pt-PT (Portuguese Portugal), pt-BR (Portuguese Brazil). Defaults to en-US if not provided or unsupported language is specified.  (optional) (default to en-US)

    try:
        api_response = api_instance.get_source_balance_by_source(x_property_id, source_kind, source_id, accept_language=accept_language)
        print("The response of SourceBalanceApi->get_source_balance_by_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceBalanceApi->get_source_balance_by_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **source_kind** | [**SourceKind**](.md)|  | 
 **source_id** | **int**| Reservation ID | House Account ID | Group Profile ID | Accounts Receivable Ledger ID | 
 **accept_language** | **str**| Language preference for localized tax/fee names. Supports: en-US (English US), es-ES (Spanish Spain), es-MX (Spanish Mexico),  fr-FR (French), de-DE (German), it-IT (Italian), pt-PT (Portuguese Portugal), pt-BR (Portuguese Brazil). Defaults to en-US if not provided or unsupported language is specified.  | [optional] [default to en-US]

### Return type

[**SourceBalanceResponse**](SourceBalanceResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

