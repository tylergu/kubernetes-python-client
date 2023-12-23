# V1alpha1ValidatingAdmissionPolicyBindingSpec

ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_resources** | [**V1alpha1MatchResources**](V1alpha1MatchResources.md) |  | [optional] 
**param_ref** | [**V1alpha1ParamRef**](V1alpha1ParamRef.md) |  | [optional] 
**policy_name** | **str** | PolicyName references a ValidatingAdmissionPolicy name which the ValidatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_validating_admission_policy_binding_spec import V1alpha1ValidatingAdmissionPolicyBindingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ValidatingAdmissionPolicyBindingSpec from a JSON string
v1alpha1_validating_admission_policy_binding_spec_instance = V1alpha1ValidatingAdmissionPolicyBindingSpec.from_json(json)
# print the JSON string representation of the object
print V1alpha1ValidatingAdmissionPolicyBindingSpec.to_json()

# convert the object into a dict
v1alpha1_validating_admission_policy_binding_spec_dict = v1alpha1_validating_admission_policy_binding_spec_instance.to_dict()
# create an instance of V1alpha1ValidatingAdmissionPolicyBindingSpec from a dict
v1alpha1_validating_admission_policy_binding_spec_form_dict = v1alpha1_validating_admission_policy_binding_spec.from_dict(v1alpha1_validating_admission_policy_binding_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


