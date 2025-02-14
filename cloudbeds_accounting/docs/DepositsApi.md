# cloudbeds_accounting.DepositsApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deposit_balance**](DepositsApi.md#get_deposit_balance) | **GET** /accounting/v1.0/deposits/balance | 
[**get_deposit_transactions**](DepositsApi.md#get_deposit_transactions) | **GET** /accounting/v1.0/deposits/transactions | 
[**post_deposits_transfer**](DepositsApi.md#post_deposits_transfer) | **POST** /accounting/v1.0/deposits/transfer | 


# **get_deposit_balance**
> DepositBalanceResponse get_deposit_balance(x_property_id, source_id=source_id, source_kind=source_kind)



Get Deposit Balance For Source or Property 

### Example

* Bearer (JWT) Authentication (bearerAuth):

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_accounting.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.DepositsApi(api_client)
    x_property_id = 56 # int | Property id
    source_id = 56 # int |  (optional)
    source_kind = cloudbeds_accounting.SourceKind() # SourceKind |  (optional)

    try:
        api_response = api_instance.get_deposit_balance(x_property_id, source_id=source_id, source_kind=source_kind)
        print("The response of DepositsApi->get_deposit_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepositsApi->get_deposit_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **source_id** | **int**|  | [optional] 
 **source_kind** | [**SourceKind**](.md)|  | [optional] 

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



Get Deposit Transactions 

### Example

* Bearer (JWT) Authentication (bearerAuth):

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_accounting.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.DepositsApi(api_client)
    x_property_id = 56 # int | Property id
    page_token = 'page_token_example' # str | page token (optional)
    page_size = 56 # int | Size of the page (optional)
    filter = cloudbeds_accounting.GetDepositTransactionsFilterParameter() # GetDepositTransactionsFilterParameter |  (optional)

    try:
        api_response = api_instance.get_deposit_transactions(x_property_id, page_token=page_token, page_size=page_size, filter=filter)
        print("The response of DepositsApi->get_deposit_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepositsApi->get_deposit_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **page_token** | **str**| page token | [optional] 
 **page_size** | **int**| Size of the page | [optional] 
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



### Example

* Bearer (JWT) Authentication (bearerAuth):

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = cloudbeds_accounting.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.DepositsApi(api_client)
    x_property_id = 56 # int | Property id
    transfer_deposit_post_request = cloudbeds_accounting.TransferDepositPostRequest() # TransferDepositPostRequest | 

    try:
        api_response = api_instance.post_deposits_transfer(x_property_id, transfer_deposit_post_request)
        print("The response of DepositsApi->post_deposits_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepositsApi->post_deposits_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
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

