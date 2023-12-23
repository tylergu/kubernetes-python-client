# V1alpha1ResourceClaimTemplateSpec

ResourceClaimTemplateSpec contains the metadata and fields for a ResourceClaim.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1alpha1ResourceClaimSpec**](V1alpha1ResourceClaimSpec.md) |  | 

## Example

```python
from kubernetes.client.models.v1alpha1_resource_claim_template_spec import V1alpha1ResourceClaimTemplateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ResourceClaimTemplateSpec from a JSON string
v1alpha1_resource_claim_template_spec_instance = V1alpha1ResourceClaimTemplateSpec.from_json(json)
# print the JSON string representation of the object
print V1alpha1ResourceClaimTemplateSpec.to_json()

# convert the object into a dict
v1alpha1_resource_claim_template_spec_dict = v1alpha1_resource_claim_template_spec_instance.to_dict()
# create an instance of V1alpha1ResourceClaimTemplateSpec from a dict
v1alpha1_resource_claim_template_spec_form_dict = v1alpha1_resource_claim_template_spec.from_dict(v1alpha1_resource_claim_template_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


