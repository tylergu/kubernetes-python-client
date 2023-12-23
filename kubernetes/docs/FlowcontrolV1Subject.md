# FlowcontrolV1Subject

Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**V1GroupSubject**](V1GroupSubject.md) |  | [optional] 
**kind** | **str** | &#x60;kind&#x60; indicates which one of the other fields is non-empty. Required | 
**service_account** | [**V1ServiceAccountSubject**](V1ServiceAccountSubject.md) |  | [optional] 
**user** | [**V1UserSubject**](V1UserSubject.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.flowcontrol_v1_subject import FlowcontrolV1Subject

# TODO update the JSON string below
json = "{}"
# create an instance of FlowcontrolV1Subject from a JSON string
flowcontrol_v1_subject_instance = FlowcontrolV1Subject.from_json(json)
# print the JSON string representation of the object
print FlowcontrolV1Subject.to_json()

# convert the object into a dict
flowcontrol_v1_subject_dict = flowcontrol_v1_subject_instance.to_dict()
# create an instance of FlowcontrolV1Subject from a dict
flowcontrol_v1_subject_form_dict = flowcontrol_v1_subject.from_dict(flowcontrol_v1_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


