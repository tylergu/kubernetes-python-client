# V1HorizontalPodAutoscaler

configuration of a horizontal pod autoscaler.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1HorizontalPodAutoscalerSpec**](V1HorizontalPodAutoscalerSpec.md) |  | [optional] 
**status** | [**V1HorizontalPodAutoscalerStatus**](V1HorizontalPodAutoscalerStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_horizontal_pod_autoscaler import V1HorizontalPodAutoscaler

# TODO update the JSON string below
json = "{}"
# create an instance of V1HorizontalPodAutoscaler from a JSON string
v1_horizontal_pod_autoscaler_instance = V1HorizontalPodAutoscaler.from_json(json)
# print the JSON string representation of the object
print V1HorizontalPodAutoscaler.to_json()

# convert the object into a dict
v1_horizontal_pod_autoscaler_dict = v1_horizontal_pod_autoscaler_instance.to_dict()
# create an instance of V1HorizontalPodAutoscaler from a dict
v1_horizontal_pod_autoscaler_form_dict = v1_horizontal_pod_autoscaler.from_dict(v1_horizontal_pod_autoscaler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


