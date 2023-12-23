# V1beta2PriorityLevelConfigurationStatus

PriorityLevelConfigurationStatus represents the current state of a \"request-priority\".

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1beta2PriorityLevelConfigurationCondition]**](V1beta2PriorityLevelConfigurationCondition.md) | &#x60;conditions&#x60; is the current state of \&quot;request-priority\&quot;. | [optional] 

## Example

```python
from kubernetes.client.models.v1beta2_priority_level_configuration_status import V1beta2PriorityLevelConfigurationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2PriorityLevelConfigurationStatus from a JSON string
v1beta2_priority_level_configuration_status_instance = V1beta2PriorityLevelConfigurationStatus.from_json(json)
# print the JSON string representation of the object
print V1beta2PriorityLevelConfigurationStatus.to_json()

# convert the object into a dict
v1beta2_priority_level_configuration_status_dict = v1beta2_priority_level_configuration_status_instance.to_dict()
# create an instance of V1beta2PriorityLevelConfigurationStatus from a dict
v1beta2_priority_level_configuration_status_form_dict = v1beta2_priority_level_configuration_status.from_dict(v1beta2_priority_level_configuration_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


