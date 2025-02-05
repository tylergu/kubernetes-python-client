# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.29
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from kubernetes.client.models.v1_api_group_list import V1APIGroupList

class TestV1APIGroupList(unittest.TestCase):
    """V1APIGroupList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1APIGroupList:
        """Test V1APIGroupList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1APIGroupList`
        """
        model = V1APIGroupList()
        if include_optional:
            return V1APIGroupList(
                api_version = '',
                groups = [
                    kubernetes.client.models.v1/api_group.v1.APIGroup(
                        api_version = '', 
                        kind = '', 
                        name = '', 
                        preferred_version = kubernetes.client.models.v1/group_version_for_discovery.v1.GroupVersionForDiscovery(
                            group_version = '', 
                            version = '', ), 
                        server_address_by_client_cidrs = [
                            kubernetes.client.models.v1/server_address_by_client_cidr.v1.ServerAddressByClientCIDR(
                                kubernetes.client_cidr = '', 
                                server_address = '', )
                            ], 
                        versions = [
                            kubernetes.client.models.v1/group_version_for_discovery.v1.GroupVersionForDiscovery(
                                group_version = '', 
                                version = '', )
                            ], )
                    ],
                kind = ''
            )
        else:
            return V1APIGroupList(
                groups = [
                    kubernetes.client.models.v1/api_group.v1.APIGroup(
                        api_version = '', 
                        kind = '', 
                        name = '', 
                        preferred_version = kubernetes.client.models.v1/group_version_for_discovery.v1.GroupVersionForDiscovery(
                            group_version = '', 
                            version = '', ), 
                        server_address_by_client_cidrs = [
                            kubernetes.client.models.v1/server_address_by_client_cidr.v1.ServerAddressByClientCIDR(
                                kubernetes.client_cidr = '', 
                                server_address = '', )
                            ], 
                        versions = [
                            kubernetes.client.models.v1/group_version_for_discovery.v1.GroupVersionForDiscovery(
                                group_version = '', 
                                version = '', )
                            ], )
                    ],
        )
        """

    def testV1APIGroupList(self):
        """Test V1APIGroupList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
