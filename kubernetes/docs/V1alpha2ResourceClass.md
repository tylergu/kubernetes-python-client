# V1alpha2ResourceClass

ResourceClass is used by administrators to influence how resources are allocated.  This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**driver_name** | **str** | DriverName defines the name of the dynamic resource driver that is used for allocation of a ResourceClaim that uses this class.  Resource drivers have a unique name in forward domain order (acme.example.com). | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**parameters_ref** | [**V1alpha2ResourceClassParametersReference**](V1alpha2ResourceClassParametersReference.md) |  | [optional] 
**suitable_nodes** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_resource_class import V1alpha2ResourceClass

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceClass from a JSON string
v1alpha2_resource_class_instance = V1alpha2ResourceClass.from_json(json)
# print the JSON string representation of the object
print V1alpha2ResourceClass.to_json()

# convert the object into a dict
v1alpha2_resource_class_dict = v1alpha2_resource_class_instance.to_dict()
# create an instance of V1alpha2ResourceClass from a dict
v1alpha2_resource_class_form_dict = v1alpha2_resource_class.from_dict(v1alpha2_resource_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


