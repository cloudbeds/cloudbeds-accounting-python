# cloudbeds_accounting.SettingsApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings**](SettingsApi.md#get_settings) | **GET** /accounting/v1.0/settings | Get property accounting settings
[**patch_settings**](SettingsApi.md#patch_settings) | **PATCH** /accounting/v1.0/settings | Update property accounting settings


# **get_settings**
> SettingResponse get_settings(x_property_id)

Get property accounting settings

Retrieve the accounting settings for a property. Use this endpoint to check the current configuration, such as the deposit consumption policy. Settings control how certain accounting behaviors work across the property.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.setting_response import SettingResponse
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
    api_instance = cloudbeds_accounting.SettingsApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 

    try:
        # Get property accounting settings
        api_response = api_instance.get_settings(x_property_id)
        print("The response of SettingsApi->get_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 

### Return type

[**SettingResponse**](SettingResponse.md)

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

# **patch_settings**
> SettingResponse patch_settings(x_property_id, setting_patch_request)

Update property accounting settings

Update one or more accounting settings for a property. You only need to include the fields you want to change; unspecified fields remain unchanged. If no settings exist for the property, they are created automatically.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.setting_patch_request import SettingPatchRequest
from cloudbeds_accounting.models.setting_response import SettingResponse
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
    api_instance = cloudbeds_accounting.SettingsApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    setting_patch_request = cloudbeds_accounting.SettingPatchRequest() # SettingPatchRequest | 

    try:
        # Update property accounting settings
        api_response = api_instance.patch_settings(x_property_id, setting_patch_request)
        print("The response of SettingsApi->patch_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->patch_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **setting_patch_request** | [**SettingPatchRequest**](SettingPatchRequest.md)|  | 

### Return type

[**SettingResponse**](SettingResponse.md)

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

