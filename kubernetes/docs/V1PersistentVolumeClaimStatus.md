# V1PersistentVolumeClaimStatus

PersistentVolumeClaimStatus is the current status of a persistent volume claim.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **List[str]** | accessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 | [optional] 
**allocated_resources** | **Dict[str, str]** | allocatedResources is the storage resource within AllocatedResources tracks the capacity allocated to a PVC. It may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity. This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature. | [optional] 
**capacity** | **Dict[str, str]** | capacity represents the actual resources of the underlying volume. | [optional] 
**conditions** | [**List[V1PersistentVolumeClaimCondition]**](V1PersistentVolumeClaimCondition.md) | conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to &#39;ResizeStarted&#39;. | [optional] 
**phase** | **str** | phase represents the current phase of PersistentVolumeClaim.   | [optional] 
**resize_status** | **str** | resizeStatus stores status of resize operation. ResizeStatus is not set by default but when expansion is complete resizeStatus is set to empty string by resize controller or kubelet. This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature. | [optional] 

## Example

```python
from kubernetes.client.models.v1_persistent_volume_claim_status import V1PersistentVolumeClaimStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1PersistentVolumeClaimStatus from a JSON string
v1_persistent_volume_claim_status_instance = V1PersistentVolumeClaimStatus.from_json(json)
# print the JSON string representation of the object
print V1PersistentVolumeClaimStatus.to_json()

# convert the object into a dict
v1_persistent_volume_claim_status_dict = v1_persistent_volume_claim_status_instance.to_dict()
# create an instance of V1PersistentVolumeClaimStatus from a dict
v1_persistent_volume_claim_status_form_dict = v1_persistent_volume_claim_status.from_dict(v1_persistent_volume_claim_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


