# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.29
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.api.internal_apiserver_v1alpha1_api import InternalApiserverV1alpha1Api


class TestInternalApiserverV1alpha1Api(unittest.TestCase):
    """InternalApiserverV1alpha1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = InternalApiserverV1alpha1Api()

    def tearDown(self) -> None:
        pass

    def test_create_storage_version(self) -> None:
        """Test case for create_storage_version

        """
        pass

    def test_delete_collection_storage_version(self) -> None:
        """Test case for delete_collection_storage_version

        """
        pass

    def test_delete_storage_version(self) -> None:
        """Test case for delete_storage_version

        """
        pass

    def test_get_api_resources(self) -> None:
        """Test case for get_api_resources

        """
        pass

    def test_list_storage_version(self) -> None:
        """Test case for list_storage_version

        """
        pass

    def test_patch_storage_version(self) -> None:
        """Test case for patch_storage_version

        """
        pass

    def test_patch_storage_version_status(self) -> None:
        """Test case for patch_storage_version_status

        """
        pass

    def test_read_storage_version(self) -> None:
        """Test case for read_storage_version

        """
        pass

    def test_read_storage_version_status(self) -> None:
        """Test case for read_storage_version_status

        """
        pass

    def test_replace_storage_version(self) -> None:
        """Test case for replace_storage_version

        """
        pass

    def test_replace_storage_version_status(self) -> None:
        """Test case for replace_storage_version_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
