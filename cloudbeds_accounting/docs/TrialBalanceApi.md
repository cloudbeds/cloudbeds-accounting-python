# cloudbeds_accounting.TrialBalanceApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_trial_balance**](TrialBalanceApi.md#calculate_trial_balance) | **POST** /accounting/v1.0/trial-balance/configuration/calculate | 
[**get_trial_balance_configuration**](TrialBalanceApi.md#get_trial_balance_configuration) | **GET** /accounting/v1.0/trial-balance/configuration | 
[**get_trial_balance_report**](TrialBalanceApi.md#get_trial_balance_report) | **GET** /accounting/v1.0/trial-balance/report | 
[**is_trial_balance_configured**](TrialBalanceApi.md#is_trial_balance_configured) | **GET** /accounting/v1.0/trial-balance/configuration/status | 
[**set_trial_balance**](TrialBalanceApi.md#set_trial_balance) | **POST** /accounting/v1.0/trial-balance/configuration | 


# **calculate_trial_balance**
> TrialBalanceResponse calculate_trial_balance(x_property_id)



Get initial Trial Balance based transaction records (till end of yesterday in property time) 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.trial_balance_response import TrialBalanceResponse
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
    api_instance = cloudbeds_accounting.TrialBalanceApi(api_client)
    x_property_id = 56 # int | Property id

    try:
        api_response = api_instance.calculate_trial_balance(x_property_id)
        print("The response of TrialBalanceApi->calculate_trial_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrialBalanceApi->calculate_trial_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 

### Return type

[**TrialBalanceResponse**](TrialBalanceResponse.md)

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

# **get_trial_balance_configuration**
> TrialBalanceResponse get_trial_balance_configuration(x_property_id)



Get configured trial balance. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.trial_balance_response import TrialBalanceResponse
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
    api_instance = cloudbeds_accounting.TrialBalanceApi(api_client)
    x_property_id = 56 # int | Property id

    try:
        api_response = api_instance.get_trial_balance_configuration(x_property_id)
        print("The response of TrialBalanceApi->get_trial_balance_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrialBalanceApi->get_trial_balance_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 

### Return type

[**TrialBalanceResponse**](TrialBalanceResponse.md)

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

# **get_trial_balance_report**
> TrialBalanceReportResponse get_trial_balance_report(x_property_id, var_date)



Get Trial Balance Report for specific date 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.trial_balance_report_response import TrialBalanceReportResponse
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
    api_instance = cloudbeds_accounting.TrialBalanceApi(api_client)
    x_property_id = 56 # int | Property id
    var_date = 'Sun Jul 21 02:00:00 CEST 2024' # date | 

    try:
        api_response = api_instance.get_trial_balance_report(x_property_id, var_date)
        print("The response of TrialBalanceApi->get_trial_balance_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrialBalanceApi->get_trial_balance_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **var_date** | **date**|  | 

### Return type

[**TrialBalanceReportResponse**](TrialBalanceReportResponse.md)

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

# **is_trial_balance_configured**
> TrialBalanceConfigurationStatusResponse is_trial_balance_configured(x_property_id)



Returns information if property has configured trial balance report. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.trial_balance_configuration_status_response import TrialBalanceConfigurationStatusResponse
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
    api_instance = cloudbeds_accounting.TrialBalanceApi(api_client)
    x_property_id = 56 # int | Property id

    try:
        api_response = api_instance.is_trial_balance_configured(x_property_id)
        print("The response of TrialBalanceApi->is_trial_balance_configured:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrialBalanceApi->is_trial_balance_configured: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 

### Return type

[**TrialBalanceConfigurationStatusResponse**](TrialBalanceConfigurationStatusResponse.md)

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

# **set_trial_balance**
> set_trial_balance(x_property_id, trial_balance_request=trial_balance_request)



Configure trial balance for property by saving opening balances for today. Fail if trial balance configuration already exists. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.trial_balance_request import TrialBalanceRequest
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
    api_instance = cloudbeds_accounting.TrialBalanceApi(api_client)
    x_property_id = 56 # int | Property id
    trial_balance_request = cloudbeds_accounting.TrialBalanceRequest() # TrialBalanceRequest |  (optional)

    try:
        api_instance.set_trial_balance(x_property_id, trial_balance_request=trial_balance_request)
    except Exception as e:
        print("Exception when calling TrialBalanceApi->set_trial_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Property id | 
 **trial_balance_request** | [**TrialBalanceRequest**](TrialBalanceRequest.md)|  | [optional] 

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

