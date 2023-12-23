# V1PersistentVolumeClaimSpec

PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **List[str]** | accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 | [optional] 
**data_source** | [**V1TypedLocalObjectReference**](V1TypedLocalObjectReference.md) |  | [optional] 
**data_source_ref** | [**V1TypedObjectReference**](V1TypedObjectReference.md) |  | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 
**storage_class_name** | **str** | storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1 | [optional] 
**volume_mode** | **str** | volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. | [optional] 
**volume_name** | **str** | volumeName is the binding reference to the PersistentVolume backing this claim. | [optional] 

## Example

```python
from kubernetes.client.models.v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1PersistentVolumeClaimSpec from a JSON string
v1_persistent_volume_claim_spec_instance = V1PersistentVolumeClaimSpec.from_json(json)
# print the JSON string representation of the object
print V1PersistentVolumeClaimSpec.to_json()

# convert the object into a dict
v1_persistent_volume_claim_spec_dict = v1_persistent_volume_claim_spec_instance.to_dict()
# create an instance of V1PersistentVolumeClaimSpec from a dict
v1_persistent_volume_claim_spec_form_dict = v1_persistent_volume_claim_spec.from_dict(v1_persistent_volume_claim_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


