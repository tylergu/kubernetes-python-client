# V1EndpointSlice

EndpointSlice represents a subset of the endpoints that implement a service. For a given service there may be multiple EndpointSlice objects, selected by labels, which must be joined to produce the full set of endpoints.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_type** | **str** | addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name. | 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**endpoints** | [**List[V1Endpoint]**](V1Endpoint.md) | endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**ports** | [**List[DiscoveryV1EndpointPort]**](DiscoveryV1EndpointPort.md) | ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates \&quot;all ports\&quot;. Each slice may include a maximum of 100 ports. | [optional] 

## Example

```python
from kubernetes.client.models.v1_endpoint_slice import V1EndpointSlice

# TODO update the JSON string below
json = "{}"
# create an instance of V1EndpointSlice from a JSON string
v1_endpoint_slice_instance = V1EndpointSlice.from_json(json)
# print the JSON string representation of the object
print V1EndpointSlice.to_json()

# convert the object into a dict
v1_endpoint_slice_dict = v1_endpoint_slice_instance.to_dict()
# create an instance of V1EndpointSlice from a dict
v1_endpoint_slice_form_dict = v1_endpoint_slice.from_dict(v1_endpoint_slice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


