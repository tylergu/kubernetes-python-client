# V1VolumeMount

VolumeMount describes a mounting of a Volume within a container.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_path** | **str** | Path within the container at which the volume should be mounted.  Must not contain &#39;:&#39;. | 
**mount_propagation** | **str** | mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. | [optional] 
**name** | **str** | This must match the Name of a Volume. | 
**read_only** | **bool** | Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. | [optional] 
**sub_path** | **str** | Path within the volume from which the container&#39;s volume should be mounted. Defaults to \&quot;\&quot; (volume&#39;s root). | [optional] 
**sub_path_expr** | **str** | Expanded path within the volume from which the container&#39;s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container&#39;s environment. Defaults to \&quot;\&quot; (volume&#39;s root). SubPathExpr and SubPath are mutually exclusive. | [optional] 

## Example

```python
from kubernetes.client.models.v1_volume_mount import V1VolumeMount

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeMount from a JSON string
v1_volume_mount_instance = V1VolumeMount.from_json(json)
# print the JSON string representation of the object
print V1VolumeMount.to_json()

# convert the object into a dict
v1_volume_mount_dict = v1_volume_mount_instance.to_dict()
# create an instance of V1VolumeMount from a dict
v1_volume_mount_form_dict = v1_volume_mount.from_dict(v1_volume_mount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


