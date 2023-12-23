# V1alpha1ValidatingAdmissionPolicy

ValidatingAdmissionPolicy describes the definition of an admission validation policy that accepts or rejects an object without changing it.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1alpha1ValidatingAdmissionPolicySpec**](V1alpha1ValidatingAdmissionPolicySpec.md) |  | [optional] 
**status** | [**V1alpha1ValidatingAdmissionPolicyStatus**](V1alpha1ValidatingAdmissionPolicyStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_validating_admission_policy import V1alpha1ValidatingAdmissionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ValidatingAdmissionPolicy from a JSON string
v1alpha1_validating_admission_policy_instance = V1alpha1ValidatingAdmissionPolicy.from_json(json)
# print the JSON string representation of the object
print V1alpha1ValidatingAdmissionPolicy.to_json()

# convert the object into a dict
v1alpha1_validating_admission_policy_dict = v1alpha1_validating_admission_policy_instance.to_dict()
# create an instance of V1alpha1ValidatingAdmissionPolicy from a dict
v1alpha1_validating_admission_policy_form_dict = v1alpha1_validating_admission_policy.from_dict(v1alpha1_validating_admission_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


