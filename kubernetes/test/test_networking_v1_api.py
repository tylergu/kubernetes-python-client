# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.29
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.api.networking_v1_api import NetworkingV1Api


class TestNetworkingV1Api(unittest.TestCase):
    """NetworkingV1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = NetworkingV1Api()

    def tearDown(self) -> None:
        pass

    def test_create_ingress_class(self) -> None:
        """Test case for create_ingress_class

        """
        pass

    def test_create_namespaced_ingress(self) -> None:
        """Test case for create_namespaced_ingress

        """
        pass

    def test_create_namespaced_network_policy(self) -> None:
        """Test case for create_namespaced_network_policy

        """
        pass

    def test_delete_collection_ingress_class(self) -> None:
        """Test case for delete_collection_ingress_class

        """
        pass

    def test_delete_collection_namespaced_ingress(self) -> None:
        """Test case for delete_collection_namespaced_ingress

        """
        pass

    def test_delete_collection_namespaced_network_policy(self) -> None:
        """Test case for delete_collection_namespaced_network_policy

        """
        pass

    def test_delete_ingress_class(self) -> None:
        """Test case for delete_ingress_class

        """
        pass

    def test_delete_namespaced_ingress(self) -> None:
        """Test case for delete_namespaced_ingress

        """
        pass

    def test_delete_namespaced_network_policy(self) -> None:
        """Test case for delete_namespaced_network_policy

        """
        pass

    def test_get_api_resources(self) -> None:
        """Test case for get_api_resources

        """
        pass

    def test_list_ingress_class(self) -> None:
        """Test case for list_ingress_class

        """
        pass

    def test_list_ingress_for_all_namespaces(self) -> None:
        """Test case for list_ingress_for_all_namespaces

        """
        pass

    def test_list_namespaced_ingress(self) -> None:
        """Test case for list_namespaced_ingress

        """
        pass

    def test_list_namespaced_network_policy(self) -> None:
        """Test case for list_namespaced_network_policy

        """
        pass

    def test_list_network_policy_for_all_namespaces(self) -> None:
        """Test case for list_network_policy_for_all_namespaces

        """
        pass

    def test_patch_ingress_class(self) -> None:
        """Test case for patch_ingress_class

        """
        pass

    def test_patch_namespaced_ingress(self) -> None:
        """Test case for patch_namespaced_ingress

        """
        pass

    def test_patch_namespaced_ingress_status(self) -> None:
        """Test case for patch_namespaced_ingress_status

        """
        pass

    def test_patch_namespaced_network_policy(self) -> None:
        """Test case for patch_namespaced_network_policy

        """
        pass

    def test_read_ingress_class(self) -> None:
        """Test case for read_ingress_class

        """
        pass

    def test_read_namespaced_ingress(self) -> None:
        """Test case for read_namespaced_ingress

        """
        pass

    def test_read_namespaced_ingress_status(self) -> None:
        """Test case for read_namespaced_ingress_status

        """
        pass

    def test_read_namespaced_network_policy(self) -> None:
        """Test case for read_namespaced_network_policy

        """
        pass

    def test_replace_ingress_class(self) -> None:
        """Test case for replace_ingress_class

        """
        pass

    def test_replace_namespaced_ingress(self) -> None:
        """Test case for replace_namespaced_ingress

        """
        pass

    def test_replace_namespaced_ingress_status(self) -> None:
        """Test case for replace_namespaced_ingress_status

        """
        pass

    def test_replace_namespaced_network_policy(self) -> None:
        """Test case for replace_namespaced_network_policy

        """
        pass


if __name__ == '__main__':
    unittest.main()
