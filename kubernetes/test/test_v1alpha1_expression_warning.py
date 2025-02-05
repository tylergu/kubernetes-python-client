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

from kubernetes.client.models.v1alpha1_expression_warning import V1alpha1ExpressionWarning

class TestV1alpha1ExpressionWarning(unittest.TestCase):
    """V1alpha1ExpressionWarning unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha1ExpressionWarning:
        """Test V1alpha1ExpressionWarning
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha1ExpressionWarning`
        """
        model = V1alpha1ExpressionWarning()
        if include_optional:
            return V1alpha1ExpressionWarning(
                field_ref = '',
                warning = ''
            )
        else:
            return V1alpha1ExpressionWarning(
                field_ref = '',
                warning = '',
        )
        """

    def testV1alpha1ExpressionWarning(self):
        """Test V1alpha1ExpressionWarning"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
