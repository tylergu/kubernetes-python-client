# V1alpha1AllocationResult

AllocationResult contains attributed of an allocated resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_on_nodes** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 
**resource_handle** | **str** | ResourceHandle contains arbitrary data returned by the driver after a successful allocation. This is opaque for Kubernetes. Driver documentation may explain to users how to interpret this data if needed.  The maximum size of this field is 16KiB. This may get increased in the future, but not reduced. | [optional] 
**shareable** | **bool** | Shareable determines whether the resource supports more than one consumer at a time. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_allocation_result import V1alpha1AllocationResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1AllocationResult from a JSON string
v1alpha1_allocation_result_instance = V1alpha1AllocationResult.from_json(json)
# print the JSON string representation of the object
print V1alpha1AllocationResult.to_json()

# convert the object into a dict
v1alpha1_allocation_result_dict = v1alpha1_allocation_result_instance.to_dict()
# create an instance of V1alpha1AllocationResult from a dict
v1alpha1_allocation_result_form_dict = v1alpha1_allocation_result.from_dict(v1alpha1_allocation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


