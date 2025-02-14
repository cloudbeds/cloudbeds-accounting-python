# AsyncEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Id of event which will be processed asynchronous. | [optional] 

## Example

```python
from cloudbeds_accounting.models.async_event_response import AsyncEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncEventResponse from a JSON string
async_event_response_instance = AsyncEventResponse.from_json(json)
# print the JSON string representation of the object
print(AsyncEventResponse.to_json())

# convert the object into a dict
async_event_response_dict = async_event_response_instance.to_dict()
# create an instance of AsyncEventResponse from a dict
async_event_response_from_dict = AsyncEventResponse.from_dict(async_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


