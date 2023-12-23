# DiscoveryV1EndpointPort

EndpointPort represents a Port used by an EndpointSlice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_protocol** | **str** | The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol. | [optional] 
**name** | **str** | The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or &#39;-&#39;. * must start and end with an alphanumeric character. Default is empty string. | [optional] 
**port** | **int** | The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer. | [optional] 
**protocol** | **str** | The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP. | [optional] 

## Example

```python
from kubernetes.client.models.discovery_v1_endpoint_port import DiscoveryV1EndpointPort

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryV1EndpointPort from a JSON string
discovery_v1_endpoint_port_instance = DiscoveryV1EndpointPort.from_json(json)
# print the JSON string representation of the object
print DiscoveryV1EndpointPort.to_json()

# convert the object into a dict
discovery_v1_endpoint_port_dict = discovery_v1_endpoint_port_instance.to_dict()
# create an instance of DiscoveryV1EndpointPort from a dict
discovery_v1_endpoint_port_form_dict = discovery_v1_endpoint_port.from_dict(discovery_v1_endpoint_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


