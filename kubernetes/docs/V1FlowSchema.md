# V1FlowSchema

FlowSchema defines the schema of a group of flows. Note that a flow is made up of a set of inbound API requests with similar attributes and is identified by a pair of strings: the name of the FlowSchema and a \"flow distinguisher\".

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1FlowSchemaSpec**](V1FlowSchemaSpec.md) |  | [optional] 
**status** | [**V1FlowSchemaStatus**](V1FlowSchemaStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_flow_schema import V1FlowSchema

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowSchema from a JSON string
v1_flow_schema_instance = V1FlowSchema.from_json(json)
# print the JSON string representation of the object
print V1FlowSchema.to_json()

# convert the object into a dict
v1_flow_schema_dict = v1_flow_schema_instance.to_dict()
# create an instance of V1FlowSchema from a dict
v1_flow_schema_form_dict = v1_flow_schema.from_dict(v1_flow_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


