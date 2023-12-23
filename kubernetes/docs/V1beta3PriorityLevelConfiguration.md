# V1beta3PriorityLevelConfiguration

PriorityLevelConfiguration represents the configuration of a priority level.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1beta3PriorityLevelConfigurationSpec**](V1beta3PriorityLevelConfigurationSpec.md) |  | [optional] 
**status** | [**V1beta3PriorityLevelConfigurationStatus**](V1beta3PriorityLevelConfigurationStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1beta3_priority_level_configuration import V1beta3PriorityLevelConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta3PriorityLevelConfiguration from a JSON string
v1beta3_priority_level_configuration_instance = V1beta3PriorityLevelConfiguration.from_json(json)
# print the JSON string representation of the object
print V1beta3PriorityLevelConfiguration.to_json()

# convert the object into a dict
v1beta3_priority_level_configuration_dict = v1beta3_priority_level_configuration_instance.to_dict()
# create an instance of V1beta3PriorityLevelConfiguration from a dict
v1beta3_priority_level_configuration_form_dict = v1beta3_priority_level_configuration.from_dict(v1beta3_priority_level_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


