# UserModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the user. | [optional] 
**first_name** | **str** | The name of the user. | [optional] 
**last_name** | **str** | The last name of the user. | [optional] 
**email** | **str** | User email | [optional] 
**type** | **str** | REAL_USER - user was found, UNKNOWN_USER - user was not found, SYSTEM_USER - user_id &#x3D; 0 OR null | [optional] 

## Example

```python
from cloudbeds_accounting.models.user_model import UserModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserModel from a JSON string
user_model_instance = UserModel.from_json(json)
# print the JSON string representation of the object
print(UserModel.to_json())

# convert the object into a dict
user_model_dict = user_model_instance.to_dict()
# create an instance of UserModel from a dict
user_model_from_dict = UserModel.from_dict(user_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


