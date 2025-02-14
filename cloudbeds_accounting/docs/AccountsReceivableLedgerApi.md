# cloudbeds_accounting.AccountsReceivableLedgerApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_accounts_receivable_ledger_reservation_balance_transfer**](AccountsReceivableLedgerApi.md#delete_accounts_receivable_ledger_reservation_balance_transfer) | **DELETE** /accounting/v1.0/accounts-receivable-ledgers/{accountsReceivableLedgerId}/reservation/{reservationId}/balance-transfer | 
[**get_accounts_receivable_ledger_by_id**](AccountsReceivableLedgerApi.md#get_accounts_receivable_ledger_by_id) | **GET** /accounting/v1.0/accounts-receivable-ledgers/{accountsReceivableLedgerId} | 
[**get_accounts_receivable_ledger_reservation_balance_transfer**](AccountsReceivableLedgerApi.md#get_accounts_receivable_ledger_reservation_balance_transfer) | **GET** /accounting/v1.0/accounts-receivable-ledgers/reservation/{reservationId}/balance-transfer | 
[**get_accounts_receivable_ledger_totals**](AccountsReceivableLedgerApi.md#get_accounts_receivable_ledger_totals) | **GET** /accounting/v1.0/accounts-receivable-ledgers/totals | 
[**get_accounts_receivable_ledger_transactions**](AccountsReceivableLedgerApi.md#get_accounts_receivable_ledger_transactions) | **GET** /accounting/v1.0/accounts-receivable-ledgers/{accountsReceivableLedgerId}/transactions | 
[**get_accounts_receivable_ledgers**](AccountsReceivableLedgerApi.md#get_accounts_receivable_ledgers) | **GET** /accounting/v1.0/accounts-receivable-ledgers | 
[**patch_accounts_receivable_ledger**](AccountsReceivableLedgerApi.md#patch_accounts_receivable_ledger) | **PATCH** /accounting/v1.0/accounts-receivable-ledgers | 
[**post_accounts_receivable_ledger**](AccountsReceivableLedgerApi.md#post_accounts_receivable_ledger) | **POST** /accounting/v1.0/accounts-receivable-ledgers | 
[**post_accounts_receivable_ledger_reservation_balance_transfer**](AccountsReceivableLedgerApi.md#post_accounts_receivable_ledger_reservation_balance_transfer) | **POST** /accounting/v1.0/accounts-receivable-ledgers/{accountsReceivableLedgerId}/reservation/{reservationId}/balance-transfer | 


# **delete_accounts_receivable_ledger_reservation_balance_transfer**
> AsyncEventResponse delete_accounts_receivable_ledger_reservation_balance_transfer(x_property_id, accounts_receivable_ledger_id, reservation_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.async_event_response import AsyncEventResponse
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
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Property id
    accounts_receivable_ledger_id = 56 # int | Accounts Receivable ID
    reservation_id = 56 # int | Reservation ID

    try:
        api_response = api_instance.delete_accounts_receivable_ledger_reservation_balance_transfer(x_property_id, accounts_receivable_ledger_id, reservation_id)
        print("The response of AccountsReceivableLedgerApi->delete_accounts_receivable_ledger_reservation_balance_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->delete_accounts_receivable_ledger_reservation_balance_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **accounts_receivable_ledger_id** | **int**| Accounts Receivable ID | 
 **reservation_id** | **int**| Reservation ID | 

### Return type

[**AsyncEventResponse**](AsyncEventResponse.md)

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

# **get_accounts_receivable_ledger_by_id**
> AccountsReceivableLedgerResponse get_accounts_receivable_ledger_by_id(x_property_id, accounts_receivable_ledger_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.accounts_receivable_ledger_response import AccountsReceivableLedgerResponse
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
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Property id
    accounts_receivable_ledger_id = 56 # int | Accounts Receivable ID

    try:
        api_response = api_instance.get_accounts_receivable_ledger_by_id(x_property_id, accounts_receivable_ledger_id)
        print("The response of AccountsReceivableLedgerApi->get_accounts_receivable_ledger_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->get_accounts_receivable_ledger_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **accounts_receivable_ledger_id** | **int**| Accounts Receivable ID | 

### Return type

[**AccountsReceivableLedgerResponse**](AccountsReceivableLedgerResponse.md)

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

# **get_accounts_receivable_ledger_reservation_balance_transfer**
> AccountsReceivableLedgerReservationBalanceTransferResponse get_accounts_receivable_ledger_reservation_balance_transfer(x_property_id, reservation_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.accounts_receivable_ledger_reservation_balance_transfer_response import AccountsReceivableLedgerReservationBalanceTransferResponse
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
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Property id
    reservation_id = 56 # int | Reservation ID

    try:
        api_response = api_instance.get_accounts_receivable_ledger_reservation_balance_transfer(x_property_id, reservation_id)
        print("The response of AccountsReceivableLedgerApi->get_accounts_receivable_ledger_reservation_balance_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->get_accounts_receivable_ledger_reservation_balance_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **reservation_id** | **int**| Reservation ID | 

### Return type

[**AccountsReceivableLedgerReservationBalanceTransferResponse**](AccountsReceivableLedgerReservationBalanceTransferResponse.md)

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

# **get_accounts_receivable_ledger_totals**
> AccountsReceivableLedgerTotalsResponse get_accounts_receivable_ledger_totals(x_property_id, filter=filter)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.accounts_receivable_ledger_totals_response import AccountsReceivableLedgerTotalsResponse
from cloudbeds_accounting.models.get_accounts_receivable_ledger_totals_filter_parameter import GetAccountsReceivableLedgerTotalsFilterParameter
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
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Property id
    filter = cloudbeds_accounting.GetAccountsReceivableLedgerTotalsFilterParameter() # GetAccountsReceivableLedgerTotalsFilterParameter |  (optional)

    try:
        api_response = api_instance.get_accounts_receivable_ledger_totals(x_property_id, filter=filter)
        print("The response of AccountsReceivableLedgerApi->get_accounts_receivable_ledger_totals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->get_accounts_receivable_ledger_totals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **filter** | [**GetAccountsReceivableLedgerTotalsFilterParameter**](.md)|  | [optional] 

### Return type

[**AccountsReceivableLedgerTotalsResponse**](AccountsReceivableLedgerTotalsResponse.md)

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

# **get_accounts_receivable_ledger_transactions**
> ExtendedTransactionPaginated get_accounts_receivable_ledger_transactions(x_property_id, accounts_receivable_ledger_id, page_token=page_token, page_size=page_size, filter=filter)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.extended_transaction_paginated import ExtendedTransactionPaginated
from cloudbeds_accounting.models.get_accounts_receivable_ledger_transactions_filter_parameter import GetAccountsReceivableLedgerTransactionsFilterParameter
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
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Property id
    accounts_receivable_ledger_id = 56 # int | Accounts Receivable ID
    page_token = 'page_token_example' # str | page token (optional)
    page_size = 56 # int | Size of the page (optional)
    filter = cloudbeds_accounting.GetAccountsReceivableLedgerTransactionsFilterParameter() # GetAccountsReceivableLedgerTransactionsFilterParameter |  (optional)

    try:
        api_response = api_instance.get_accounts_receivable_ledger_transactions(x_property_id, accounts_receivable_ledger_id, page_token=page_token, page_size=page_size, filter=filter)
        print("The response of AccountsReceivableLedgerApi->get_accounts_receivable_ledger_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->get_accounts_receivable_ledger_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **accounts_receivable_ledger_id** | **int**| Accounts Receivable ID | 
 **page_token** | **str**| page token | [optional] 
 **page_size** | **int**| Size of the page | [optional] 
 **filter** | [**GetAccountsReceivableLedgerTransactionsFilterParameter**](.md)|  | [optional] 

### Return type

[**ExtendedTransactionPaginated**](ExtendedTransactionPaginated.md)

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

# **get_accounts_receivable_ledgers**
> AccountsReceivableLedgerPaginated get_accounts_receivable_ledgers(x_property_id, filter=filter)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.accounts_receivable_ledger_paginated import AccountsReceivableLedgerPaginated
from cloudbeds_accounting.models.get_accounts_receivable_ledgers_filter_parameter import GetAccountsReceivableLedgersFilterParameter
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
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Property id
    filter = cloudbeds_accounting.GetAccountsReceivableLedgersFilterParameter() # GetAccountsReceivableLedgersFilterParameter |  (optional)

    try:
        api_response = api_instance.get_accounts_receivable_ledgers(x_property_id, filter=filter)
        print("The response of AccountsReceivableLedgerApi->get_accounts_receivable_ledgers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->get_accounts_receivable_ledgers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **filter** | [**GetAccountsReceivableLedgersFilterParameter**](.md)|  | [optional] 

### Return type

[**AccountsReceivableLedgerPaginated**](AccountsReceivableLedgerPaginated.md)

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

# **patch_accounts_receivable_ledger**
> AccountsReceivableLedgerResponse patch_accounts_receivable_ledger(x_property_id, accounts_receivable_ledger_patch_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.accounts_receivable_ledger_patch_request import AccountsReceivableLedgerPatchRequest
from cloudbeds_accounting.models.accounts_receivable_ledger_response import AccountsReceivableLedgerResponse
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
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Property id
    accounts_receivable_ledger_patch_request = cloudbeds_accounting.AccountsReceivableLedgerPatchRequest() # AccountsReceivableLedgerPatchRequest | 

    try:
        api_response = api_instance.patch_accounts_receivable_ledger(x_property_id, accounts_receivable_ledger_patch_request)
        print("The response of AccountsReceivableLedgerApi->patch_accounts_receivable_ledger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->patch_accounts_receivable_ledger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **accounts_receivable_ledger_patch_request** | [**AccountsReceivableLedgerPatchRequest**](AccountsReceivableLedgerPatchRequest.md)|  | 

### Return type

[**AccountsReceivableLedgerResponse**](AccountsReceivableLedgerResponse.md)

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

# **post_accounts_receivable_ledger**
> AccountsReceivableLedgerResponse post_accounts_receivable_ledger(x_property_id, accounts_receivable_ledger_post_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.accounts_receivable_ledger_post_request import AccountsReceivableLedgerPostRequest
from cloudbeds_accounting.models.accounts_receivable_ledger_response import AccountsReceivableLedgerResponse
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
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Property id
    accounts_receivable_ledger_post_request = cloudbeds_accounting.AccountsReceivableLedgerPostRequest() # AccountsReceivableLedgerPostRequest | 

    try:
        api_response = api_instance.post_accounts_receivable_ledger(x_property_id, accounts_receivable_ledger_post_request)
        print("The response of AccountsReceivableLedgerApi->post_accounts_receivable_ledger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->post_accounts_receivable_ledger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **accounts_receivable_ledger_post_request** | [**AccountsReceivableLedgerPostRequest**](AccountsReceivableLedgerPostRequest.md)|  | 

### Return type

[**AccountsReceivableLedgerResponse**](AccountsReceivableLedgerResponse.md)

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

# **post_accounts_receivable_ledger_reservation_balance_transfer**
> AsyncEventResponse post_accounts_receivable_ledger_reservation_balance_transfer(x_property_id, accounts_receivable_ledger_id, reservation_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.async_event_response import AsyncEventResponse
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
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Property id
    accounts_receivable_ledger_id = 56 # int | Accounts Receivable ID
    reservation_id = 56 # int | Reservation ID

    try:
        api_response = api_instance.post_accounts_receivable_ledger_reservation_balance_transfer(x_property_id, accounts_receivable_ledger_id, reservation_id)
        print("The response of AccountsReceivableLedgerApi->post_accounts_receivable_ledger_reservation_balance_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->post_accounts_receivable_ledger_reservation_balance_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **accounts_receivable_ledger_id** | **int**| Accounts Receivable ID | 
 **reservation_id** | **int**| Reservation ID | 

### Return type

[**AsyncEventResponse**](AsyncEventResponse.md)

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

