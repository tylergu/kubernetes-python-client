# V1alpha1PodSchedulingStatus

PodSchedulingStatus describes where resources for the Pod can be allocated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_claims** | [**List[V1alpha1ResourceClaimSchedulingStatus]**](V1alpha1ResourceClaimSchedulingStatus.md) | ResourceClaims describes resource availability for each pod.spec.resourceClaim entry where the corresponding ResourceClaim uses \&quot;WaitForFirstConsumer\&quot; allocation mode. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_pod_scheduling_status import V1alpha1PodSchedulingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1PodSchedulingStatus from a JSON string
v1alpha1_pod_scheduling_status_instance = V1alpha1PodSchedulingStatus.from_json(json)
# print the JSON string representation of the object
print V1alpha1PodSchedulingStatus.to_json()

# convert the object into a dict
v1alpha1_pod_scheduling_status_dict = v1alpha1_pod_scheduling_status_instance.to_dict()
# create an instance of V1alpha1PodSchedulingStatus from a dict
v1alpha1_pod_scheduling_status_form_dict = v1alpha1_pod_scheduling_status.from_dict(v1alpha1_pod_scheduling_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


