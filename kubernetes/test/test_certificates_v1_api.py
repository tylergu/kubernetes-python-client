# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.29
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.api.certificates_v1_api import CertificatesV1Api


class TestCertificatesV1Api(unittest.TestCase):
    """CertificatesV1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = CertificatesV1Api()

    def tearDown(self) -> None:
        pass

    def test_create_certificate_signing_request(self) -> None:
        """Test case for create_certificate_signing_request

        """
        pass

    def test_delete_certificate_signing_request(self) -> None:
        """Test case for delete_certificate_signing_request

        """
        pass

    def test_delete_collection_certificate_signing_request(self) -> None:
        """Test case for delete_collection_certificate_signing_request

        """
        pass

    def test_get_api_resources(self) -> None:
        """Test case for get_api_resources

        """
        pass

    def test_list_certificate_signing_request(self) -> None:
        """Test case for list_certificate_signing_request

        """
        pass

    def test_patch_certificate_signing_request(self) -> None:
        """Test case for patch_certificate_signing_request

        """
        pass

    def test_patch_certificate_signing_request_approval(self) -> None:
        """Test case for patch_certificate_signing_request_approval

        """
        pass

    def test_patch_certificate_signing_request_status(self) -> None:
        """Test case for patch_certificate_signing_request_status

        """
        pass

    def test_read_certificate_signing_request(self) -> None:
        """Test case for read_certificate_signing_request

        """
        pass

    def test_read_certificate_signing_request_approval(self) -> None:
        """Test case for read_certificate_signing_request_approval

        """
        pass

    def test_read_certificate_signing_request_status(self) -> None:
        """Test case for read_certificate_signing_request_status

        """
        pass

    def test_replace_certificate_signing_request(self) -> None:
        """Test case for replace_certificate_signing_request

        """
        pass

    def test_replace_certificate_signing_request_approval(self) -> None:
        """Test case for replace_certificate_signing_request_approval

        """
        pass

    def test_replace_certificate_signing_request_status(self) -> None:
        """Test case for replace_certificate_signing_request_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
