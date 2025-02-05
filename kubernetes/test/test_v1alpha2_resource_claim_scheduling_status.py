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

from kubernetes.client.models.v1alpha2_resource_claim_scheduling_status import V1alpha2ResourceClaimSchedulingStatus

class TestV1alpha2ResourceClaimSchedulingStatus(unittest.TestCase):
    """V1alpha2ResourceClaimSchedulingStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha2ResourceClaimSchedulingStatus:
        """Test V1alpha2ResourceClaimSchedulingStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha2ResourceClaimSchedulingStatus`
        """
        model = V1alpha2ResourceClaimSchedulingStatus()
        if include_optional:
            return V1alpha2ResourceClaimSchedulingStatus(
                name = '',
                unsuitable_nodes = [
                    ''
                    ]
            )
        else:
            return V1alpha2ResourceClaimSchedulingStatus(
        )
        """

    def testV1alpha2ResourceClaimSchedulingStatus(self):
        """Test V1alpha2ResourceClaimSchedulingStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
