# V1alpha1ParamRef

ParamRef references a parameter resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the resource being referenced. | [optional] 
**namespace** | **str** | Namespace of the referenced resource. Should be empty for the cluster-scoped resources | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_param_ref import V1alpha1ParamRef

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ParamRef from a JSON string
v1alpha1_param_ref_instance = V1alpha1ParamRef.from_json(json)
# print the JSON string representation of the object
print V1alpha1ParamRef.to_json()

# convert the object into a dict
v1alpha1_param_ref_dict = v1alpha1_param_ref_instance.to_dict()
# create an instance of V1alpha1ParamRef from a dict
v1alpha1_param_ref_form_dict = v1alpha1_param_ref.from_dict(v1alpha1_param_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


