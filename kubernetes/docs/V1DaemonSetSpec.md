# V1DaemonSetSpec

DaemonSetSpec is the specification of a daemon set.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_ready_seconds** | **int** | The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready). | [optional] 
**revision_history_limit** | **int** | The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. | [optional] 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | 
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) |  | 
**update_strategy** | [**V1DaemonSetUpdateStrategy**](V1DaemonSetUpdateStrategy.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_daemon_set_spec import V1DaemonSetSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1DaemonSetSpec from a JSON string
v1_daemon_set_spec_instance = V1DaemonSetSpec.from_json(json)
# print the JSON string representation of the object
print V1DaemonSetSpec.to_json()

# convert the object into a dict
v1_daemon_set_spec_dict = v1_daemon_set_spec_instance.to_dict()
# create an instance of V1DaemonSetSpec from a dict
v1_daemon_set_spec_form_dict = v1_daemon_set_spec.from_dict(v1_daemon_set_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


