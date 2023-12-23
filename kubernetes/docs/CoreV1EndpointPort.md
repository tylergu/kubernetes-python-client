# CoreV1EndpointPort

EndpointPort is a tuple that describes a single port.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_protocol** | **str** | The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol. | [optional] 
**name** | **str** | The name of this port.  This must match the &#39;name&#39; field in the corresponding ServicePort. Must be a DNS_LABEL. Optional only if one port is defined. | [optional] 
**port** | **int** | The port number of the endpoint. | 
**protocol** | **str** | The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.   | [optional] 

## Example

```python
from kubernetes.client.models.core_v1_endpoint_port import CoreV1EndpointPort

# TODO update the JSON string below
json = "{}"
# create an instance of CoreV1EndpointPort from a JSON string
core_v1_endpoint_port_instance = CoreV1EndpointPort.from_json(json)
# print the JSON string representation of the object
print CoreV1EndpointPort.to_json()

# convert the object into a dict
core_v1_endpoint_port_dict = core_v1_endpoint_port_instance.to_dict()
# create an instance of CoreV1EndpointPort from a dict
core_v1_endpoint_port_form_dict = core_v1_endpoint_port.from_dict(core_v1_endpoint_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


