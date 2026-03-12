# cloudbeds_accounting.DepositsApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deposit_balance**](DepositsApi.md#get_deposit_balance) | **GET** /accounting/v1.0/deposits/balance | Get deposit balance
[**get_deposit_transactions**](DepositsApi.md#get_deposit_transactions) | **GET** /accounting/v1.0/deposits/transactions | List deposit transactions
[**post_deposits_transfer**](DepositsApi.md#post_deposits_transfer) | **POST** /accounting/v1.0/deposits/transfer | Transfer deposit transactions


# **get_deposit_balance**
> DepositBalanceResponse get_deposit_balance(x_property_id, source_id=source_id, source_kind=source_kind)

Get deposit balance

Retrieve the deposit balance for a specific source or the entire property. To get the balance for a specific reservation or other source, provide both sourceId and sourceKind. To get the aggregate deposit balance for the whole property, omit both parameters. The response includes the posted balance and pending balance in the smallest currency unit.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.deposit_balance_response import DepositBalanceResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.DepositsApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    source_id = 56 # int | Identifier of the source to get the deposit balance for (e.g., a reservation ID). Omit along with sourceKind to get the property-wide deposit balance.  (optional)
    source_kind = cloudbeds_accounting.SourceKind() # SourceKind | Type of the source entity. Required when sourceId is provided.  (optional)

    try:
        # Get deposit balance
        api_response = api_instance.get_deposit_balance(x_property_id, source_id=source_id, source_kind=source_kind)
        print("The response of DepositsApi->get_deposit_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepositsApi->get_deposit_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **source_id** | **int**| Identifier of the source to get the deposit balance for (e.g., a reservation ID). Omit along with sourceKind to get the property-wide deposit balance.  | [optional] 
 **source_kind** | [**SourceKind**](.md)| Type of the source entity. Required when sourceId is provided.  | [optional] 

### Return type

[**DepositBalanceResponse**](DepositBalanceResponse.md)

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

# **get_deposit_transactions**
> ExtendedTransactionPaginated get_deposit_transactions(x_property_id, page_token=page_token, page_size=page_size, filter=filter)

List deposit transactions

Retrieve a paginated list of deposit transactions for a property. You can filter by transaction state, reservation, date ranges (transaction date, check-in, check-out), reservation status, and user. Use this endpoint to review deposit activity including payments received, transfers, and refunds.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.extended_transaction_paginated import ExtendedTransactionPaginated
from cloudbeds_accounting.models.get_deposit_transactions_filter_parameter import GetDepositTransactionsFilterParameter
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
    api_instance = cloudbeds_accounting.DepositsApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    page_token = 'page_token_example' # str | Opaque token for cursor-based pagination. Pass the `nextPageToken` value from a previous response to retrieve the next page. Omit this parameter (or pass null) for the first page.  (optional)
    page_size = 56 # int | Number of results to return per page. If not specified, the server uses a default page size.  (optional)
    filter = cloudbeds_accounting.GetDepositTransactionsFilterParameter() # GetDepositTransactionsFilterParameter |  (optional)

    try:
        # List deposit transactions
        api_response = api_instance.get_deposit_transactions(x_property_id, page_token=page_token, page_size=page_size, filter=filter)
        print("The response of DepositsApi->get_deposit_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepositsApi->get_deposit_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **page_token** | **str**| Opaque token for cursor-based pagination. Pass the &#x60;nextPageToken&#x60; value from a previous response to retrieve the next page. Omit this parameter (or pass null) for the first page.  | [optional] 
 **page_size** | **int**| Number of results to return per page. If not specified, the server uses a default page size.  | [optional] 
 **filter** | [**GetDepositTransactionsFilterParameter**](.md)|  | [optional] 

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

# **post_deposits_transfer**
> AsyncEventResponse post_deposits_transfer(x_property_id, transfer_deposit_post_request)

Transfer deposit transactions

Transfer one or more deposit transactions to the guest ledger. Provide the transaction IDs of the deposits you want to transfer. This operation is processed asynchronously; the response includes an event ID you can use to track the result.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.async_event_response import AsyncEventResponse
from cloudbeds_accounting.models.transfer_deposit_post_request import TransferDepositPostRequest
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
    api_instance = cloudbeds_accounting.DepositsApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    transfer_deposit_post_request = cloudbeds_accounting.TransferDepositPostRequest() # TransferDepositPostRequest | 

    try:
        # Transfer deposit transactions
        api_response = api_instance.post_deposits_transfer(x_property_id, transfer_deposit_post_request)
        print("The response of DepositsApi->post_deposits_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepositsApi->post_deposits_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **transfer_deposit_post_request** | [**TransferDepositPostRequest**](TransferDepositPostRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

