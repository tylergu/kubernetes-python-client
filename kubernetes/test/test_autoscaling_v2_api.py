# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.29
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.api.autoscaling_v2_api import AutoscalingV2Api


class TestAutoscalingV2Api(unittest.TestCase):
    """AutoscalingV2Api unit test stubs"""

    def setUp(self) -> None:
        self.api = AutoscalingV2Api()

    def tearDown(self) -> None:
        pass

    def test_create_namespaced_horizontal_pod_autoscaler(self) -> None:
        """Test case for create_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_delete_collection_namespaced_horizontal_pod_autoscaler(self) -> None:
        """Test case for delete_collection_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_delete_namespaced_horizontal_pod_autoscaler(self) -> None:
        """Test case for delete_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_get_api_resources(self) -> None:
        """Test case for get_api_resources

        """
        pass

    def test_list_horizontal_pod_autoscaler_for_all_namespaces(self) -> None:
        """Test case for list_horizontal_pod_autoscaler_for_all_namespaces

        """
        pass

    def test_list_namespaced_horizontal_pod_autoscaler(self) -> None:
        """Test case for list_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_patch_namespaced_horizontal_pod_autoscaler(self) -> None:
        """Test case for patch_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_patch_namespaced_horizontal_pod_autoscaler_status(self) -> None:
        """Test case for patch_namespaced_horizontal_pod_autoscaler_status

        """
        pass

    def test_read_namespaced_horizontal_pod_autoscaler(self) -> None:
        """Test case for read_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_read_namespaced_horizontal_pod_autoscaler_status(self) -> None:
        """Test case for read_namespaced_horizontal_pod_autoscaler_status

        """
        pass

    def test_replace_namespaced_horizontal_pod_autoscaler(self) -> None:
        """Test case for replace_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_replace_namespaced_horizontal_pod_autoscaler_status(self) -> None:
        """Test case for replace_namespaced_horizontal_pod_autoscaler_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
