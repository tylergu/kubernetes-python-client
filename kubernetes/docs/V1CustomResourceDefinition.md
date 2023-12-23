# V1CustomResourceDefinition

CustomResourceDefinition represents a resource that should be exposed on the API server.  Its name MUST be in the format <.spec.name>.<.spec.group>.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1CustomResourceDefinitionSpec**](V1CustomResourceDefinitionSpec.md) |  | 
**status** | [**V1CustomResourceDefinitionStatus**](V1CustomResourceDefinitionStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_custom_resource_definition import V1CustomResourceDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of V1CustomResourceDefinition from a JSON string
v1_custom_resource_definition_instance = V1CustomResourceDefinition.from_json(json)
# print the JSON string representation of the object
print V1CustomResourceDefinition.to_json()

# convert the object into a dict
v1_custom_resource_definition_dict = v1_custom_resource_definition_instance.to_dict()
# create an instance of V1CustomResourceDefinition from a dict
v1_custom_resource_definition_form_dict = v1_custom_resource_definition.from_dict(v1_custom_resource_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


