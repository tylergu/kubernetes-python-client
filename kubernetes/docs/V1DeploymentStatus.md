# V1DeploymentStatus

DeploymentStatus is the most recently observed status of the Deployment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_replicas** | **int** | Total number of available pods (ready for at least minReadySeconds) targeted by this deployment. | [optional] 
**collision_count** | **int** | Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet. | [optional] 
**conditions** | [**List[V1DeploymentCondition]**](V1DeploymentCondition.md) | Represents the latest available observations of a deployment&#39;s current state. | [optional] 
**observed_generation** | **int** | The generation observed by the deployment controller. | [optional] 
**ready_replicas** | **int** | readyReplicas is the number of pods targeted by this Deployment with a Ready Condition. | [optional] 
**replicas** | **int** | Total number of non-terminated pods targeted by this deployment (their labels match the selector). | [optional] 
**unavailable_replicas** | **int** | Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created. | [optional] 
**updated_replicas** | **int** | Total number of non-terminated pods targeted by this deployment that have the desired template spec. | [optional] 

## Example

```python
from kubernetes.client.models.v1_deployment_status import V1DeploymentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeploymentStatus from a JSON string
v1_deployment_status_instance = V1DeploymentStatus.from_json(json)
# print the JSON string representation of the object
print V1DeploymentStatus.to_json()

# convert the object into a dict
v1_deployment_status_dict = v1_deployment_status_instance.to_dict()
# create an instance of V1DeploymentStatus from a dict
v1_deployment_status_form_dict = v1_deployment_status.from_dict(v1_deployment_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


