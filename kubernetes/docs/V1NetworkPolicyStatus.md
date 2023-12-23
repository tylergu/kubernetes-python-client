# V1NetworkPolicyStatus

NetworkPolicyStatus describe the current state of the NetworkPolicy.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1Condition]**](V1Condition.md) | Conditions holds an array of metav1.Condition that describe the state of the NetworkPolicy. Current service state | [optional] 

## Example

```python
from kubernetes.client.models.v1_network_policy_status import V1NetworkPolicyStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1NetworkPolicyStatus from a JSON string
v1_network_policy_status_instance = V1NetworkPolicyStatus.from_json(json)
# print the JSON string representation of the object
print V1NetworkPolicyStatus.to_json()

# convert the object into a dict
v1_network_policy_status_dict = v1_network_policy_status_instance.to_dict()
# create an instance of V1NetworkPolicyStatus from a dict
v1_network_policy_status_form_dict = v1_network_policy_status.from_dict(v1_network_policy_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


