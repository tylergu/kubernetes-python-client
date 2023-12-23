# V1ClaimSource

ClaimSource describes a reference to a ResourceClaim.  Exactly one of these fields should be set.  Consumers of this type must treat an empty object as if it has an unknown value.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_claim_name** | **str** | ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod. | [optional] 
**resource_claim_template_name** | **str** | ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.  The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The name of the ResourceClaim will be &lt;pod name&gt;-&lt;resource name&gt;, where &lt;resource name&gt; is the PodResourceClaim.Name. Pod validation will reject the pod if the concatenated name is not valid for a ResourceClaim (e.g. too long).  An existing ResourceClaim with that name that is not owned by the pod will not be used for the pod to avoid using an unrelated resource by mistake. Scheduling and pod startup are then blocked until the unrelated ResourceClaim is removed.  This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim. | [optional] 

## Example

```python
from kubernetes.client.models.v1_claim_source import V1ClaimSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1ClaimSource from a JSON string
v1_claim_source_instance = V1ClaimSource.from_json(json)
# print the JSON string representation of the object
print V1ClaimSource.to_json()

# convert the object into a dict
v1_claim_source_dict = v1_claim_source_instance.to_dict()
# create an instance of V1ClaimSource from a dict
v1_claim_source_form_dict = v1_claim_source.from_dict(v1_claim_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


