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

from kubernetes.client.models.v1beta1_self_subject_review_status import V1beta1SelfSubjectReviewStatus

class TestV1beta1SelfSubjectReviewStatus(unittest.TestCase):
    """V1beta1SelfSubjectReviewStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1SelfSubjectReviewStatus:
        """Test V1beta1SelfSubjectReviewStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1SelfSubjectReviewStatus`
        """
        model = V1beta1SelfSubjectReviewStatus()
        if include_optional:
            return V1beta1SelfSubjectReviewStatus(
                user_info = kubernetes.client.models.v1/user_info.v1.UserInfo(
                    extra = {
                        'key' : [
                            ''
                            ]
                        }, 
                    groups = [
                        ''
                        ], 
                    uid = '', 
                    username = '', )
            )
        else:
            return V1beta1SelfSubjectReviewStatus(
        )
        """

    def testV1beta1SelfSubjectReviewStatus(self):
        """Test V1beta1SelfSubjectReviewStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
