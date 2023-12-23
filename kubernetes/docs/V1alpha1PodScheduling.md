# V1alpha1PodScheduling

PodScheduling objects hold information that is needed to schedule a Pod with ResourceClaims that use \"WaitForFirstConsumer\" allocation mode.  This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1alpha1PodSchedulingSpec**](V1alpha1PodSchedulingSpec.md) |  | 
**status** | [**V1alpha1PodSchedulingStatus**](V1alpha1PodSchedulingStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_pod_scheduling import V1alpha1PodScheduling

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1PodScheduling from a JSON string
v1alpha1_pod_scheduling_instance = V1alpha1PodScheduling.from_json(json)
# print the JSON string representation of the object
print V1alpha1PodScheduling.to_json()

# convert the object into a dict
v1alpha1_pod_scheduling_dict = v1alpha1_pod_scheduling_instance.to_dict()
# create an instance of V1alpha1PodScheduling from a dict
v1alpha1_pod_scheduling_form_dict = v1alpha1_pod_scheduling.from_dict(v1alpha1_pod_scheduling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


