# V1alpha1PodSchedulingSpec

PodSchedulingSpec describes where resources for the Pod are needed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**potential_nodes** | **List[str]** | PotentialNodes lists nodes where the Pod might be able to run.  The size of this field is limited to 128. This is large enough for many clusters. Larger clusters may need more attempts to find a node that suits all pending resources. This may get increased in the future, but not reduced. | [optional] 
**selected_node** | **str** | SelectedNode is the node for which allocation of ResourceClaims that are referenced by the Pod and that use \&quot;WaitForFirstConsumer\&quot; allocation is to be attempted. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_pod_scheduling_spec import V1alpha1PodSchedulingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1PodSchedulingSpec from a JSON string
v1alpha1_pod_scheduling_spec_instance = V1alpha1PodSchedulingSpec.from_json(json)
# print the JSON string representation of the object
print V1alpha1PodSchedulingSpec.to_json()

# convert the object into a dict
v1alpha1_pod_scheduling_spec_dict = v1alpha1_pod_scheduling_spec_instance.to_dict()
# create an instance of V1alpha1PodSchedulingSpec from a dict
v1alpha1_pod_scheduling_spec_form_dict = v1alpha1_pod_scheduling_spec.from_dict(v1alpha1_pod_scheduling_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


