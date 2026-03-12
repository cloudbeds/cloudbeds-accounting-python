# cloudbeds_accounting.TrialBalanceApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_trial_balance**](TrialBalanceApi.md#calculate_trial_balance) | **POST** /accounting/v1.0/trial-balance/configuration/calculate | Calculate initial trial balance
[**get_trial_balance_configuration**](TrialBalanceApi.md#get_trial_balance_configuration) | **GET** /accounting/v1.0/trial-balance/configuration | Get trial balance configuration
[**get_trial_balance_report**](TrialBalanceApi.md#get_trial_balance_report) | **GET** /accounting/v1.0/trial-balance/report | Get trial balance report
[**is_trial_balance_configured**](TrialBalanceApi.md#is_trial_balance_configured) | **GET** /accounting/v1.0/trial-balance/configuration/status | Check trial balance configuration status
[**set_trial_balance**](TrialBalanceApi.md#set_trial_balance) | **POST** /accounting/v1.0/trial-balance/configuration | Configure trial balance


# **calculate_trial_balance**
> TrialBalanceResponse calculate_trial_balance(x_property_id)

Calculate initial trial balance

Calculate the initial trial balance for a property based on all historical transaction records up to the end of yesterday (in property local time). Use this endpoint to preview the opening balances before committing the trial balance configuration. The response contains the computed deposit ledger, accounts receivable ledger, and guest ledger opening balances.


### Example

* OAuth Authentication (bearerAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.TrialBalanceApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 

    try:
        # Calculate initial trial balance
        api_response = api_instance.calculate_trial_balance(x_property_id)
        print("The response of TrialBalanceApi->calculate_trial_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrialBalanceApi->calculate_trial_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 

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

Get trial balance configuration

Retrieve the saved trial balance configuration for a property, including the configured opening balances for the deposit ledger, accounts receivable ledger, and guest ledger. Returns the configuration date and the opening balance values that were set when the trial balance was initialized.


### Example

* OAuth Authentication (bearerAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.TrialBalanceApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 

    try:
        # Get trial balance configuration
        api_response = api_instance.get_trial_balance_configuration(x_property_id)
        print("The response of TrialBalanceApi->get_trial_balance_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrialBalanceApi->get_trial_balance_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 

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

Get trial balance report

Retrieve the trial balance report for a specific date. The report provides a daily financial reconciliation showing opening and closing balances, ledger activity, deposit and AR transfers, and a detailed breakdown of guest ledger charges, taxes, and payments by transaction code. The property must have a configured trial balance before reports can be generated.


### Example

* OAuth Authentication (bearerAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.TrialBalanceApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    var_date = 'Sun Jul 21 00:00:00 UTC 2024' # date | 

    try:
        # Get trial balance report
        api_response = api_instance.get_trial_balance_report(x_property_id, var_date)
        print("The response of TrialBalanceApi->get_trial_balance_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrialBalanceApi->get_trial_balance_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
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

Check trial balance configuration status

Check whether a property has configured its trial balance. The response indicates whether the trial balance is configured and, if so, the date it was set up. You must configure the trial balance before you can generate daily reports.


### Example

* OAuth Authentication (bearerAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.TrialBalanceApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 

    try:
        # Check trial balance configuration status
        api_response = api_instance.is_trial_balance_configured(x_property_id)
        print("The response of TrialBalanceApi->is_trial_balance_configured:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrialBalanceApi->is_trial_balance_configured: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 

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

Configure trial balance

Configure the trial balance for a property by saving the opening balances as of today. You must provide opening balances for the deposit ledger, accounts receivable ledger, and guest ledger. This operation can only be performed once per property; it returns an error if a trial balance configuration already exists. Use the calculate endpoint first to preview the recommended opening balance values.


### Example

* OAuth Authentication (bearerAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_accounting.TrialBalanceApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    trial_balance_request = cloudbeds_accounting.TrialBalanceRequest() # TrialBalanceRequest |  (optional)

    try:
        # Configure trial balance
        api_instance.set_trial_balance(x_property_id, trial_balance_request=trial_balance_request)
    except Exception as e:
        print("Exception when calling TrialBalanceApi->set_trial_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
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

