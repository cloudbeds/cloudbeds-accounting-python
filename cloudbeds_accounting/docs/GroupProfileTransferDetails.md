# GroupProfileTransferDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Group Profile ID. | [optional] 
**name** | **str** | Group Profile Name. | [optional] 
**code** | **str** | Group Profile Code. | [optional] 

## Example

```python
from cloudbeds_accounting.models.group_profile_transfer_details import GroupProfileTransferDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GroupProfileTransferDetails from a JSON string
group_profile_transfer_details_instance = GroupProfileTransferDetails.from_json(json)
# print the JSON string representation of the object
print(GroupProfileTransferDetails.to_json())

# convert the object into a dict
group_profile_transfer_details_dict = group_profile_transfer_details_instance.to_dict()
# create an instance of GroupProfileTransferDetails from a dict
group_profile_transfer_details_from_dict = GroupProfileTransferDetails.from_dict(group_profile_transfer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


