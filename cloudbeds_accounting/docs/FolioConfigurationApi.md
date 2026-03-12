# cloudbeds_accounting.FolioConfigurationApi

All URIs are relative to *https://api.cloudbeds-stage.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_folio_configuration_to_source**](FolioConfigurationApi.md#assign_folio_configuration_to_source) | **PUT** /accounting/v1.0/folios/configurations/sources | 
[**delete_folio_configuration**](FolioConfigurationApi.md#delete_folio_configuration) | **DELETE** /accounting/v1.0/folios/configurations/{id} | Delete a folio configuration
[**get_folio_configuration**](FolioConfigurationApi.md#get_folio_configuration) | **GET** /accounting/v1.0/folios/configurations/{id} | 
[**get_folio_configuration_source**](FolioConfigurationApi.md#get_folio_configuration_source) | **GET** /accounting/v1.0/folios/configurations/sources | 
[**get_folio_configurations**](FolioConfigurationApi.md#get_folio_configurations) | **GET** /accounting/v1.0/folios/configurations | 
[**get_routing_rules**](FolioConfigurationApi.md#get_routing_rules) | **GET** /accounting/v1.0/folios/rules | Get autorouting rules
[**save_folio_configuration**](FolioConfigurationApi.md#save_folio_configuration) | **PUT** /accounting/v1.0/folios/configurations | Create or update a folio configuration
[**set_folio_configuration_default**](FolioConfigurationApi.md#set_folio_configuration_default) | **POST** /accounting/v1.0/folios/configurations/{id}/set-default | Set the default folio configuration


# **assign_folio_configuration_to_source**
> FolioConfigurationToSourceResponse assign_folio_configuration_to_source(x_property_id, assign_folio_configuration_request)

Assign a folio configuration to a source, replacing existing folios

### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.assign_folio_configuration_request import AssignFolioConfigurationRequest
from cloudbeds_accounting.models.folio_configuration_to_source_response import FolioConfigurationToSourceResponse
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
    api_instance = cloudbeds_accounting.FolioConfigurationApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    assign_folio_configuration_request = cloudbeds_accounting.AssignFolioConfigurationRequest() # AssignFolioConfigurationRequest | 

    try:
        api_response = api_instance.assign_folio_configuration_to_source(x_property_id, assign_folio_configuration_request)
        print("The response of FolioConfigurationApi->assign_folio_configuration_to_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolioConfigurationApi->assign_folio_configuration_to_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **assign_folio_configuration_request** | [**AssignFolioConfigurationRequest**](AssignFolioConfigurationRequest.md)|  | 

### Return type

[**FolioConfigurationToSourceResponse**](FolioConfigurationToSourceResponse.md)

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

# **delete_folio_configuration**
> delete_folio_configuration(x_property_id, id)

Delete a folio configuration

Delete a folio configuration by its ID. This removes the configuration template from the property. Existing folios that were created from this configuration are not affected.


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
    api_instance = cloudbeds_accounting.FolioConfigurationApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    id = 56 # int | ID of the folio configuration

    try:
        # Delete a folio configuration
        api_instance.delete_folio_configuration(x_property_id, id)
    except Exception as e:
        print("Exception when calling FolioConfigurationApi->delete_folio_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **id** | **int**| ID of the folio configuration | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folio_configuration**
> FolioConfigurationData get_folio_configuration(x_property_id, id, include_folios=include_folios)

Get a folio configuration by ID

### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.folio_configuration_data import FolioConfigurationData
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
    api_instance = cloudbeds_accounting.FolioConfigurationApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    id = 56 # int | ID of the folio configuration
    include_folios = False # bool | Whether to include folios and their transaction types (optional) (default to False)

    try:
        api_response = api_instance.get_folio_configuration(x_property_id, id, include_folios=include_folios)
        print("The response of FolioConfigurationApi->get_folio_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolioConfigurationApi->get_folio_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **id** | **int**| ID of the folio configuration | 
 **include_folios** | **bool**| Whether to include folios and their transaction types | [optional] [default to False]

### Return type

[**FolioConfigurationData**](FolioConfigurationData.md)

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

# **get_folio_configuration_source**
> FolioConfigurationToSourceResponse get_folio_configuration_source(x_property_id, source_id, source_kind)

Get which folio configuration is assigned to a source

### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.folio_configuration_to_source_response import FolioConfigurationToSourceResponse
from cloudbeds_accounting.models.folio_source_kind import FolioSourceKind
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
    api_instance = cloudbeds_accounting.FolioConfigurationApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    source_id = 56 # int | Source ID (e.g., Reservation ID, Group Profile ID)
    source_kind = cloudbeds_accounting.FolioSourceKind() # FolioSourceKind | 

    try:
        api_response = api_instance.get_folio_configuration_source(x_property_id, source_id, source_kind)
        print("The response of FolioConfigurationApi->get_folio_configuration_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolioConfigurationApi->get_folio_configuration_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **source_id** | **int**| Source ID (e.g., Reservation ID, Group Profile ID) | 
 **source_kind** | [**FolioSourceKind**](.md)|  | 

### Return type

[**FolioConfigurationToSourceResponse**](FolioConfigurationToSourceResponse.md)

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

# **get_folio_configurations**
> List[FolioConfigurationData] get_folio_configurations(x_property_id, include_folios=include_folios)

Get all folio configurations for a property

### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.folio_configuration_data import FolioConfigurationData
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
    api_instance = cloudbeds_accounting.FolioConfigurationApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    include_folios = False # bool | Whether to include folios and their transaction types (optional) (default to False)

    try:
        api_response = api_instance.get_folio_configurations(x_property_id, include_folios=include_folios)
        print("The response of FolioConfigurationApi->get_folio_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolioConfigurationApi->get_folio_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **include_folios** | **bool**| Whether to include folios and their transaction types | [optional] [default to False]

### Return type

[**List[FolioConfigurationData]**](FolioConfigurationData.md)

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

# **get_routing_rules**
> List[RoutingRuleResponse] get_routing_rules(x_property_id, source_id, source_kind)

Get autorouting rules

Retrieve the autorouting rules configured for a specific source, such as a group profile. Autorouting rules define which transaction types are automatically routed from reservations to a group profile folio. Both sourceId and sourceKind are required.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.folio_source_kind import FolioSourceKind
from cloudbeds_accounting.models.routing_rule_response import RoutingRuleResponse
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
    api_instance = cloudbeds_accounting.FolioConfigurationApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    source_id = 56 # int | Source ID (e.g., Group Profile ID)
    source_kind = cloudbeds_accounting.FolioSourceKind() # FolioSourceKind | 

    try:
        # Get autorouting rules
        api_response = api_instance.get_routing_rules(x_property_id, source_id, source_kind)
        print("The response of FolioConfigurationApi->get_routing_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolioConfigurationApi->get_routing_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **source_id** | **int**| Source ID (e.g., Group Profile ID) | 
 **source_kind** | [**FolioSourceKind**](.md)|  | 

### Return type

[**List[RoutingRuleResponse]**](RoutingRuleResponse.md)

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

# **save_folio_configuration**
> FolioConfigurationSaveResponse save_folio_configuration(x_property_id, folio_configuration_data)

Create or update a folio configuration

Create a new folio configuration or update an existing one for a property. A folio configuration defines a template for how folios are structured, including which booking sources are included and which transaction types are assigned to each folio. To update an existing configuration, include its ID in the request body.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.folio_configuration_data import FolioConfigurationData
from cloudbeds_accounting.models.folio_configuration_save_response import FolioConfigurationSaveResponse
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
    api_instance = cloudbeds_accounting.FolioConfigurationApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    folio_configuration_data = cloudbeds_accounting.FolioConfigurationData() # FolioConfigurationData | 

    try:
        # Create or update a folio configuration
        api_response = api_instance.save_folio_configuration(x_property_id, folio_configuration_data)
        print("The response of FolioConfigurationApi->save_folio_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolioConfigurationApi->save_folio_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **folio_configuration_data** | [**FolioConfigurationData**](FolioConfigurationData.md)|  | 

### Return type

[**FolioConfigurationSaveResponse**](FolioConfigurationSaveResponse.md)

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

# **set_folio_configuration_default**
> FolioConfigurationSaveResponse set_folio_configuration_default(x_property_id, id)

Set the default folio configuration

Set a folio configuration as the default for the property. The default configuration is automatically applied when new reservations or other sources are created. Only one configuration can be the default at a time; setting a new default removes the previous one.


### Example

* OAuth Authentication (bearerAuth):

```python
import cloudbeds_accounting
from cloudbeds_accounting.models.folio_configuration_save_response import FolioConfigurationSaveResponse
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
    api_instance = cloudbeds_accounting.FolioConfigurationApi(api_client)
    x_property_id = 56 # int | Unique identifier of the property. Required for all requests to scope data to a specific property. 
    id = 56 # int | ID of the folio configuration

    try:
        # Set the default folio configuration
        api_response = api_instance.set_folio_configuration_default(x_property_id, id)
        print("The response of FolioConfigurationApi->set_folio_configuration_default:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolioConfigurationApi->set_folio_configuration_default: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **int**| Unique identifier of the property. Required for all requests to scope data to a specific property.  | 
 **id** | **int**| ID of the folio configuration | 

### Return type

[**FolioConfigurationSaveResponse**](FolioConfigurationSaveResponse.md)

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

