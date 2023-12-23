# V1IngressClassSpec

IngressClassSpec provides information about the class of an Ingress.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller** | **str** | Controller refers to the name of the controller that should handle this class. This allows for different \&quot;flavors\&quot; that are controlled by the same controller. For example, you may have different Parameters for the same implementing controller. This should be specified as a domain-prefixed path no more than 250 characters in length, e.g. \&quot;acme.io/ingress-controller\&quot;. This field is immutable. | [optional] 
**parameters** | [**V1IngressClassParametersReference**](V1IngressClassParametersReference.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_ingress_class_spec import V1IngressClassSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1IngressClassSpec from a JSON string
v1_ingress_class_spec_instance = V1IngressClassSpec.from_json(json)
# print the JSON string representation of the object
print V1IngressClassSpec.to_json()

# convert the object into a dict
v1_ingress_class_spec_dict = v1_ingress_class_spec_instance.to_dict()
# create an instance of V1IngressClassSpec from a dict
v1_ingress_class_spec_form_dict = v1_ingress_class_spec.from_dict(v1_ingress_class_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


