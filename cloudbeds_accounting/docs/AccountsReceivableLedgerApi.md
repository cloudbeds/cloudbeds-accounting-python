# cloudbeds_accounting.AccountsReceivableLedgerApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_accounts_receivable_ledger_reservation_balance_transfer**](AccountsReceivableLedgerApi.md#delete_accounts_receivable_ledger_reservation_balance_transfer) | **DELETE** /accounting/v1.0/accounts-receivable-ledgers/{accountsReceivableLedgerId}/reservation/{reservationId}/balance-transfer | Reverse a reservation-to-AR balance transfer
[**get_accounts_receivable_ledger_by_id**](AccountsReceivableLedgerApi.md#get_accounts_receivable_ledger_by_id) | **GET** /accounting/v1.0/accounts-receivable-ledgers/{accountsReceivableLedgerId} | Get an accounts receivable ledger by ID
[**get_accounts_receivable_ledger_reservation_balance_transfer**](AccountsReceivableLedgerApi.md#get_accounts_receivable_ledger_reservation_balance_transfer) | **GET** /accounting/v1.0/accounts-receivable-ledgers/reservation/{reservationId}/balance-transfer | Get AR balance transfer details for a reservation
[**get_accounts_receivable_ledger_totals**](AccountsReceivableLedgerApi.md#get_accounts_receivable_ledger_totals) | **GET** /accounting/v1.0/accounts-receivable-ledgers/totals | Get AR ledger totals
[**get_accounts_receivable_ledger_transactions**](AccountsReceivableLedgerApi.md#get_accounts_receivable_ledger_transactions) | **GET** /accounting/v1.0/accounts-receivable-ledgers/{accountsReceivableLedgerId}/transactions | List transactions for an AR ledger
[**get_accounts_receivable_ledgers**](AccountsReceivableLedgerApi.md#get_accounts_receivable_ledgers) | **GET** /accounting/v1.0/accounts-receivable-ledgers | List accounts receivable ledgers
[**patch_accounts_receivable_ledger**](AccountsReceivableLedgerApi.md#patch_accounts_receivable_ledger) | **PATCH** /accounting/v1.0/accounts-receivable-ledgers | Update an accounts receivable ledger
[**post_accounts_receivable_ledger**](AccountsReceivableLedgerApi.md#post_accounts_receivable_ledger) | **POST** /accounting/v1.0/accounts-receivable-ledgers | Create an accounts receivable ledger
[**post_accounts_receivable_ledger_group_balance_transfer**](AccountsReceivableLedgerApi.md#post_accounts_receivable_ledger_group_balance_transfer) | **POST** /accounting/v1.0/accounts-receivable-ledgers/{accountsReceivableLedgerId}/group-profile/{groupProfileId}/balance-transfer | Transfer a group profile balance to an AR ledger
[**post_accounts_receivable_ledger_reservation_balance_transfer**](AccountsReceivableLedgerApi.md#post_accounts_receivable_ledger_reservation_balance_transfer) | **POST** /accounting/v1.0/accounts-receivable-ledgers/{accountsReceivableLedgerId}/reservation/{reservationId}/balance-transfer | Transfer a reservation balance to an AR ledger


# **delete_accounts_receivable_ledger_reservation_balance_transfer**
> AsyncEventResponse delete_accounts_receivable_ledger_reservation_balance_transfer(x_property_id, accounts_receivable_ledger_id, reservation_id)

Reverse a reservation-to-AR balance transfer

Reverse a previously created balance transfer between a reservation and an accounts receivable (AR) ledger. This moves the transferred balance back to the original reservation. This operation is processed asynchronously; the response includes an event ID you can use to track the result.


### Example

* OAuth Authentication (bearerAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    accounts_receivable_ledger_id = 56 # int | Unique identifier of the accounts receivable ledger.
    reservation_id = 56 # int | Reservation ID

    try:
        # Reverse a reservation-to-AR balance transfer
        api_response = api_instance.delete_accounts_receivable_ledger_reservation_balance_transfer(x_property_id, accounts_receivable_ledger_id, reservation_id)
        print("The response of AccountsReceivableLedgerApi->delete_accounts_receivable_ledger_reservation_balance_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->delete_accounts_receivable_ledger_reservation_balance_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **accounts_receivable_ledger_id** | **int**| Unique identifier of the accounts receivable ledger. | 
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

Get an accounts receivable ledger by ID

Retrieve a single accounts receivable (AR) ledger by its unique identifier. The response includes the ledger name, status, total charges, amount paid, and outstanding balance.


### Example

* OAuth Authentication (bearerAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    accounts_receivable_ledger_id = 56 # int | Unique identifier of the accounts receivable ledger.

    try:
        # Get an accounts receivable ledger by ID
        api_response = api_instance.get_accounts_receivable_ledger_by_id(x_property_id, accounts_receivable_ledger_id)
        print("The response of AccountsReceivableLedgerApi->get_accounts_receivable_ledger_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->get_accounts_receivable_ledger_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **accounts_receivable_ledger_id** | **int**| Unique identifier of the accounts receivable ledger. | 

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

Get AR balance transfer details for a reservation

Retrieve the balance transfer details for a specific reservation. If a balance transfer exists between the reservation and an accounts receivable (AR) ledger, the response includes the transfer transaction ID, amount, and the associated AR ledger ID.


### Example

* OAuth Authentication (bearerAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    reservation_id = 56 # int | Reservation ID

    try:
        # Get AR balance transfer details for a reservation
        api_response = api_instance.get_accounts_receivable_ledger_reservation_balance_transfer(x_property_id, reservation_id)
        print("The response of AccountsReceivableLedgerApi->get_accounts_receivable_ledger_reservation_balance_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->get_accounts_receivable_ledger_reservation_balance_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
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

Get AR ledger totals

Retrieve aggregated totals across all accounts receivable (AR) ledgers for a property. The response includes the combined total charges, amount paid, and outstanding balance. You can optionally filter by ledger status to see totals for only open or closed ledgers.


### Example

* OAuth Authentication (bearerAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    filter = cloudbeds_accounting.GetAccountsReceivableLedgerTotalsFilterParameter() # GetAccountsReceivableLedgerTotalsFilterParameter |  (optional)

    try:
        # Get AR ledger totals
        api_response = api_instance.get_accounts_receivable_ledger_totals(x_property_id, filter=filter)
        print("The response of AccountsReceivableLedgerApi->get_accounts_receivable_ledger_totals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->get_accounts_receivable_ledger_totals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
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
> AccountsReceivableTransactionPaginated get_accounts_receivable_ledger_transactions(x_property_id, accounts_receivable_ledger_id, page_token=page_token, page_size=page_size, filter=filter)

List transactions for an AR ledger

Retrieve a paginated list of transactions belonging to a specific accounts receivable (AR) ledger. You can filter by transaction state (posted or pending), date ranges, transaction type, and more. Use this endpoint to review the detailed financial activity within an AR ledger.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.accounts_receivable_transaction_paginated import AccountsReceivableTransactionPaginated
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    accounts_receivable_ledger_id = 56 # int | Unique identifier of the accounts receivable ledger.
    page_token = 'page_token_example' # str | Opaque token for cursor-based pagination. Pass the `nextPageToken` value from a previous response to retrieve the next page. Omit this parameter (or pass null) for the first page.  (optional)
    page_size = 56 # int | Number of results to return per page. If not specified, the server uses a default page size.  (optional)
    filter = cloudbeds_accounting.GetAccountsReceivableLedgerTransactionsFilterParameter() # GetAccountsReceivableLedgerTransactionsFilterParameter |  (optional)

    try:
        # List transactions for an AR ledger
        api_response = api_instance.get_accounts_receivable_ledger_transactions(x_property_id, accounts_receivable_ledger_id, page_token=page_token, page_size=page_size, filter=filter)
        print("The response of AccountsReceivableLedgerApi->get_accounts_receivable_ledger_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->get_accounts_receivable_ledger_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **accounts_receivable_ledger_id** | **int**| Unique identifier of the accounts receivable ledger. | 
 **page_token** | **str**| Opaque token for cursor-based pagination. Pass the &#x60;nextPageToken&#x60; value from a previous response to retrieve the next page. Omit this parameter (or pass null) for the first page.  | [optional] 
 **page_size** | **int**| Number of results to return per page. If not specified, the server uses a default page size.  | [optional] 
 **filter** | [**GetAccountsReceivableLedgerTransactionsFilterParameter**](.md)|  | [optional] 

### Return type

[**AccountsReceivableTransactionPaginated**](AccountsReceivableTransactionPaginated.md)

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

List accounts receivable ledgers

Retrieve a paginated list of accounts receivable (AR) ledgers for a property. You can filter by status, date range, balance range, profile, and search query. Use AR ledgers to track balances that have been transferred from reservations or group profiles for later collection.


### Example

* OAuth Authentication (bearerAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    filter = cloudbeds_accounting.GetAccountsReceivableLedgersFilterParameter() # GetAccountsReceivableLedgersFilterParameter |  (optional)

    try:
        # List accounts receivable ledgers
        api_response = api_instance.get_accounts_receivable_ledgers(x_property_id, filter=filter)
        print("The response of AccountsReceivableLedgerApi->get_accounts_receivable_ledgers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->get_accounts_receivable_ledgers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
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

Update an accounts receivable ledger

Update an existing accounts receivable (AR) ledger. You can change the name, description, linked profile, or status. Only include the fields you want to update. To close a ledger, set the status to CLOSED; note that a ledger can only be closed when its balance is zero.


### Example

* OAuth Authentication (bearerAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    accounts_receivable_ledger_patch_request = cloudbeds_accounting.AccountsReceivableLedgerPatchRequest() # AccountsReceivableLedgerPatchRequest | 

    try:
        # Update an accounts receivable ledger
        api_response = api_instance.patch_accounts_receivable_ledger(x_property_id, accounts_receivable_ledger_patch_request)
        print("The response of AccountsReceivableLedgerApi->patch_accounts_receivable_ledger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->patch_accounts_receivable_ledger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
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

Create an accounts receivable ledger

Create a new accounts receivable (AR) ledger for a property. An AR ledger provides a way to track outstanding balances outside of a reservation, such as invoices sent to a corporate client. You must provide a name, and can optionally link the ledger to a profile.


### Example

* OAuth Authentication (bearerAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    accounts_receivable_ledger_post_request = cloudbeds_accounting.AccountsReceivableLedgerPostRequest() # AccountsReceivableLedgerPostRequest | 

    try:
        # Create an accounts receivable ledger
        api_response = api_instance.post_accounts_receivable_ledger(x_property_id, accounts_receivable_ledger_post_request)
        print("The response of AccountsReceivableLedgerApi->post_accounts_receivable_ledger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->post_accounts_receivable_ledger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
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

# **post_accounts_receivable_ledger_group_balance_transfer**
> AsyncEventResponse post_accounts_receivable_ledger_group_balance_transfer(x_property_id, accounts_receivable_ledger_id, group_profile_id, post_group_profile_balance_transfer_request=post_group_profile_balance_transfer_request)

Transfer a group profile balance to an AR ledger

Transfer the outstanding balance of a group profile to an accounts receivable (AR) ledger. You can optionally specify a folio ID to transfer the balance from a specific folio within the group profile. This operation is processed asynchronously; the response includes an event ID you can use to track the result.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.async_event_response import AsyncEventResponse
from cloudbeds_accounting.models.post_group_profile_balance_transfer_request import PostGroupProfileBalanceTransferRequest
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
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    accounts_receivable_ledger_id = 56 # int | Unique identifier of the accounts receivable ledger.
    group_profile_id = 56 # int | Group Profile ID
    post_group_profile_balance_transfer_request = cloudbeds_accounting.PostGroupProfileBalanceTransferRequest() # PostGroupProfileBalanceTransferRequest |  (optional)

    try:
        # Transfer a group profile balance to an AR ledger
        api_response = api_instance.post_accounts_receivable_ledger_group_balance_transfer(x_property_id, accounts_receivable_ledger_id, group_profile_id, post_group_profile_balance_transfer_request=post_group_profile_balance_transfer_request)
        print("The response of AccountsReceivableLedgerApi->post_accounts_receivable_ledger_group_balance_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->post_accounts_receivable_ledger_group_balance_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **accounts_receivable_ledger_id** | **int**| Unique identifier of the accounts receivable ledger. | 
 **group_profile_id** | **int**| Group Profile ID | 
 **post_group_profile_balance_transfer_request** | [**PostGroupProfileBalanceTransferRequest**](PostGroupProfileBalanceTransferRequest.md)|  | [optional] 

### Return type

[**AsyncEventResponse**](AsyncEventResponse.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_accounts_receivable_ledger_reservation_balance_transfer**
> AsyncEventResponse post_accounts_receivable_ledger_reservation_balance_transfer(x_property_id, accounts_receivable_ledger_id, reservation_id)

Transfer a reservation balance to an AR ledger

Transfer the outstanding balance of a reservation to an accounts receivable (AR) ledger. This creates a transfer transaction that moves the balance from the reservation to the specified AR ledger for later collection. This operation is processed asynchronously; the response includes an event ID you can use to track the result.


### Example

* OAuth Authentication (bearerAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.AccountsReceivableLedgerApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    accounts_receivable_ledger_id = 56 # int | Unique identifier of the accounts receivable ledger.
    reservation_id = 56 # int | Reservation ID

    try:
        # Transfer a reservation balance to an AR ledger
        api_response = api_instance.post_accounts_receivable_ledger_reservation_balance_transfer(x_property_id, accounts_receivable_ledger_id, reservation_id)
        print("The response of AccountsReceivableLedgerApi->post_accounts_receivable_ledger_reservation_balance_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsReceivableLedgerApi->post_accounts_receivable_ledger_reservation_balance_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **accounts_receivable_ledger_id** | **int**| Unique identifier of the accounts receivable ledger. | 
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

