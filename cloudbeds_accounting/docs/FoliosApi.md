# cloudbeds_accounting.FoliosApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_folio**](FoliosApi.md#create_folio) | **POST** /accounting/v1.0/folios | Create a folio
[**delete_folio**](FoliosApi.md#delete_folio) | **DELETE** /accounting/v1.0/folios/{id} | Delete a folio
[**get_folios**](FoliosApi.md#get_folios) | **GET** /accounting/v1.0/folios | List folios for a source
[**list_folio_transactions**](FoliosApi.md#list_folio_transactions) | **POST** /accounting/v1.0/folios/transactions | Search folio transactions
[**move_transactions**](FoliosApi.md#move_transactions) | **POST** /accounting/v1.0/folios/transactions/move | Move transactions between folios
[**route_transactions**](FoliosApi.md#route_transactions) | **POST** /accounting/v1.0/folios/transactions/route | Route transactions to a group profile
[**unroute_transactions**](FoliosApi.md#unroute_transactions) | **POST** /accounting/v1.0/folios/transactions/unroute | Unroute transactions from a group profile
[**update_folio**](FoliosApi.md#update_folio) | **PUT** /accounting/v1.0/folios/{id} | Update a folio


# **create_folio**
> CreateFolioResponse create_folio(x_property_id, create_folio_request)

Create a folio

Create a new folio for a source (reservation, group profile, or house account). You must provide a name, the folio configuration ID, and the source details. You can optionally specify a parent folio ID to create a sub-folio within an existing folio hierarchy.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.create_folio_request import CreateFolioRequest
from cloudbeds_accounting.models.create_folio_response import CreateFolioResponse
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
    api_instance = cloudbeds_accounting.FoliosApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    create_folio_request = cloudbeds_accounting.CreateFolioRequest() # CreateFolioRequest | 

    try:
        # Create a folio
        api_response = api_instance.create_folio(x_property_id, create_folio_request)
        print("The response of FoliosApi->create_folio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoliosApi->create_folio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **create_folio_request** | [**CreateFolioRequest**](CreateFolioRequest.md)|  | 

### Return type

[**CreateFolioResponse**](CreateFolioResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Access denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folio**
> delete_folio(x_property_id, id)

Delete a folio

Delete a folio. The folio is soft-deleted and will no longer appear in listings. You cannot delete a folio that still has transactions assigned to it; move or unroute all transactions before deleting.


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
    api_instance = cloudbeds_accounting.FoliosApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    id = 56 # int | Folio ID

    try:
        # Delete a folio
        api_instance.delete_folio(x_property_id, id)
    except Exception as e:
        print("Exception when calling FoliosApi->delete_folio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **id** | **int**| Folio ID | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Access denied |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folios**
> List[FolioResponse] get_folios(x_property_id, filter)

List folios for a source

Retrieve all folios for a given source (reservation, group profile, or house account). Folios organize transactions into logical groups, such as separating room charges from incidentals. The filter requires both a sourceId and sourceKind to identify the source.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.folio_response import FolioResponse
from cloudbeds_accounting.models.get_folios_filter_parameter import GetFoliosFilterParameter
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
    api_instance = cloudbeds_accounting.FoliosApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    filter = cloudbeds_accounting.GetFoliosFilterParameter() # GetFoliosFilterParameter | 

    try:
        # List folios for a source
        api_response = api_instance.get_folios(x_property_id, filter)
        print("The response of FoliosApi->get_folios:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoliosApi->get_folios: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **filter** | [**GetFoliosFilterParameter**](.md)|  | 

### Return type

[**List[FolioResponse]**](FolioResponse.md)

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

# **list_folio_transactions**
> ListFolioTransactionsPaginated list_folio_transactions(x_property_id, list_folio_transactions_request)

Search folio transactions

Search and retrieve both posted and pending transactions for a source (reservation, group profile, or house account), merged into a single response. This endpoint uses POST (instead of GET) to support complex filter and grouping criteria in the request body. Results can be grouped by date, transaction type, folio, or other fields.

Results are always wrapped in groups. When groupBy is specified, transactions are grouped by that field. When omitted, all transactions are placed in a single group with key "default". Pagination is applied first (cursor-based on flat transactions), then grouping is applied to the page results. Groups at page boundaries may be partial.

When includeTotal is true, totals and foreign currency totals are computed on the first page and cached in Redis. Subsequent pages return cached totals. When no filters are applied, the total amount is read from the pre-computed source balance for optimal performance.

Supported filter fields: folioId, posted, descriptionFilters, transactionDate range, serviceDate range, subSourceIds, searchQuery.

Supported sort fields: transaction_datetime, service_date, id, internal_code.

Supported groupBy fields: transaction_date, service_date, internal_code_group, description, sub_source_identifier, folio_id, user_id.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.list_folio_transactions_paginated import ListFolioTransactionsPaginated
from cloudbeds_accounting.models.list_folio_transactions_request import ListFolioTransactionsRequest
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
    api_instance = cloudbeds_accounting.FoliosApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    list_folio_transactions_request = cloudbeds_accounting.ListFolioTransactionsRequest() # ListFolioTransactionsRequest | 

    try:
        # Search folio transactions
        api_response = api_instance.list_folio_transactions(x_property_id, list_folio_transactions_request)
        print("The response of FoliosApi->list_folio_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoliosApi->list_folio_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **list_folio_transactions_request** | [**ListFolioTransactionsRequest**](ListFolioTransactionsRequest.md)|  | 

### Return type

[**ListFolioTransactionsPaginated**](ListFolioTransactionsPaginated.md)

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

# **move_transactions**
> move_transactions(x_property_id, move_transactions_request)

Move transactions between folios

Move transactions to a different folio within the same source. You can specify individual transaction IDs or transaction types (by origin ID and external relation kind) to move all matching transactions at once. At least one of `transactions` or `transactionTypes` must be provided.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.move_transactions_request import MoveTransactionsRequest
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
    api_instance = cloudbeds_accounting.FoliosApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    move_transactions_request = cloudbeds_accounting.MoveTransactionsRequest() # MoveTransactionsRequest | 

    try:
        # Move transactions between folios
        api_instance.move_transactions(x_property_id, move_transactions_request)
    except Exception as e:
        print("Exception when calling FoliosApi->move_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **move_transactions_request** | [**MoveTransactionsRequest**](MoveTransactionsRequest.md)|  | 

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_transactions**
> route_transactions(x_property_id, route_transactions_request)

Route transactions to a group profile

Route reservation transactions to a group profile folio. Routing binds reservation transactions to a group profile and assigns them to the specified folio. You can specify individual transaction IDs or transaction types (by origin ID and external relation kind) to route all matching transactions at once. At least one of `transactions` or `transactionTypes` must be provided.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.route_transactions_request import RouteTransactionsRequest
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
    api_instance = cloudbeds_accounting.FoliosApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    route_transactions_request = cloudbeds_accounting.RouteTransactionsRequest() # RouteTransactionsRequest | 

    try:
        # Route transactions to a group profile
        api_instance.route_transactions(x_property_id, route_transactions_request)
    except Exception as e:
        print("Exception when calling FoliosApi->route_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **route_transactions_request** | [**RouteTransactionsRequest**](RouteTransactionsRequest.md)|  | 

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unroute_transactions**
> unroute_transactions(x_property_id, unroute_transactions_request)

Unroute transactions from a group profile

Unroute transactions from a group profile back to the original reservation. This reverses a previous routing operation, removing the transactions from the group profile and returning them to the reservation they originated from. Unlike move and route operations, only individual transaction IDs are supported (transaction types are not accepted).


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.unroute_transactions_request import UnrouteTransactionsRequest
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
    api_instance = cloudbeds_accounting.FoliosApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    unroute_transactions_request = cloudbeds_accounting.UnrouteTransactionsRequest() # UnrouteTransactionsRequest | 

    try:
        # Unroute transactions from a group profile
        api_instance.unroute_transactions(x_property_id, unroute_transactions_request)
    except Exception as e:
        print("Exception when calling FoliosApi->unroute_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **unroute_transactions_request** | [**UnrouteTransactionsRequest**](UnrouteTransactionsRequest.md)|  | 

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folio**
> update_folio(x_property_id, id, update_folio_request)

Update a folio

Update an existing folio. You can change the folio name and the transaction types assigned to it. Transaction types control which kinds of transactions are automatically routed to this folio. Other folio properties (source, configuration, parent) cannot be changed after creation.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.update_folio_request import UpdateFolioRequest
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
    api_instance = cloudbeds_accounting.FoliosApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    id = 56 # int | Folio ID
    update_folio_request = cloudbeds_accounting.UpdateFolioRequest() # UpdateFolioRequest | 

    try:
        # Update a folio
        api_instance.update_folio(x_property_id, id, update_folio_request)
    except Exception as e:
        print("Exception when calling FoliosApi->update_folio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **id** | **int**| Folio ID | 
 **update_folio_request** | [**UpdateFolioRequest**](UpdateFolioRequest.md)|  | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Access denied |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

