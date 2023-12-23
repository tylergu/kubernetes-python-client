# V1alpha1ResourceClaimStatus

ResourceClaimStatus tracks whether the resource has been allocated and what the resulting attributes are.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation** | [**V1alpha1AllocationResult**](V1alpha1AllocationResult.md) |  | [optional] 
**deallocation_requested** | **bool** | DeallocationRequested indicates that a ResourceClaim is to be deallocated.  The driver then must deallocate this claim and reset the field together with clearing the Allocation field.  While DeallocationRequested is set, no new consumers may be added to ReservedFor. | [optional] 
**driver_name** | **str** | DriverName is a copy of the driver name from the ResourceClass at the time when allocation started. | [optional] 
**reserved_for** | [**List[V1alpha1ResourceClaimConsumerReference]**](V1alpha1ResourceClaimConsumerReference.md) | ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started.  There can be at most 32 such reservations. This may get increased in the future, but not reduced. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_resource_claim_status import V1alpha1ResourceClaimStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ResourceClaimStatus from a JSON string
v1alpha1_resource_claim_status_instance = V1alpha1ResourceClaimStatus.from_json(json)
# print the JSON string representation of the object
print V1alpha1ResourceClaimStatus.to_json()

# convert the object into a dict
v1alpha1_resource_claim_status_dict = v1alpha1_resource_claim_status_instance.to_dict()
# create an instance of V1alpha1ResourceClaimStatus from a dict
v1alpha1_resource_claim_status_form_dict = v1alpha1_resource_claim_status.from_dict(v1alpha1_resource_claim_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


