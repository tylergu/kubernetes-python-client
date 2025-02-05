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

from kubernetes.client.models.v1_container import V1Container

class TestV1Container(unittest.TestCase):
    """V1Container unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1Container:
        """Test V1Container
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1Container`
        """
        model = V1Container()
        if include_optional:
            return V1Container(
                args = [
                    ''
                    ],
                command = [
                    ''
                    ],
                env = [
                    kubernetes.client.models.v1/env_var.v1.EnvVar(
                        name = '', 
                        value = '', 
                        value_from = kubernetes.client.models.v1/env_var_source.v1.EnvVarSource(
                            config_map_key_ref = kubernetes.client.models.v1/config_map_key_selector.v1.ConfigMapKeySelector(
                                key = '', 
                                name = '', 
                                optional = True, ), 
                            field_ref = kubernetes.client.models.v1/object_field_selector.v1.ObjectFieldSelector(
                                api_version = '', 
                                field_path = '', ), 
                            resource_field_ref = kubernetes.client.models.v1/resource_field_selector.v1.ResourceFieldSelector(
                                container_name = '', 
                                divisor = '', 
                                resource = '', ), 
                            secret_key_ref = kubernetes.client.models.v1/secret_key_selector.v1.SecretKeySelector(
                                key = '', 
                                name = '', 
                                optional = True, ), ), )
                    ],
                env_from = [
                    kubernetes.client.models.v1/env_from_source.v1.EnvFromSource(
                        config_map_ref = kubernetes.client.models.v1/config_map_env_source.v1.ConfigMapEnvSource(
                            name = '', 
                            optional = True, ), 
                        prefix = '', 
                        secret_ref = kubernetes.client.models.v1/secret_env_source.v1.SecretEnvSource(
                            name = '', 
                            optional = True, ), )
                    ],
                image = '',
                image_pull_policy = '',
                lifecycle = kubernetes.client.models.v1/lifecycle.v1.Lifecycle(
                    post_start = kubernetes.client.models.v1/lifecycle_handler.v1.LifecycleHandler(
                        exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(
                            command = [
                                ''
                                ], ), 
                        http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                            host = '', 
                            http_headers = [
                                kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                                    name = '', 
                                    value = '', )
                                ], 
                            path = '', 
                            port = kubernetes.client.models.port.port(), 
                            scheme = '', ), 
                        sleep = kubernetes.client.models.v1/sleep_action.v1.SleepAction(
                            seconds = 56, ), 
                        tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                            host = '', 
                            port = kubernetes.client.models.port.port(), ), ), 
                    pre_stop = kubernetes.client.models.v1/lifecycle_handler.v1.LifecycleHandler(), ),
                liveness_probe = kubernetes.client.models.v1/probe.v1.Probe(
                    exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(
                        command = [
                            ''
                            ], ), 
                    failure_threshold = 56, 
                    grpc = kubernetes.client.models.v1/grpc_action.v1.GRPCAction(
                        port = 56, 
                        service = '', ), 
                    http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                        host = '', 
                        http_headers = [
                            kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                                name = '', 
                                value = '', )
                            ], 
                        path = '', 
                        port = kubernetes.client.models.port.port(), 
                        scheme = '', ), 
                    initial_delay_seconds = 56, 
                    period_seconds = 56, 
                    success_threshold = 56, 
                    tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                        host = '', 
                        port = kubernetes.client.models.port.port(), ), 
                    termination_grace_period_seconds = 56, 
                    timeout_seconds = 56, ),
                name = '',
                ports = [
                    kubernetes.client.models.v1/container_port.v1.ContainerPort(
                        container_port = 56, 
                        host_ip = '', 
                        host_port = 56, 
                        name = '', 
                        protocol = '', )
                    ],
                readiness_probe = kubernetes.client.models.v1/probe.v1.Probe(
                    exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(
                        command = [
                            ''
                            ], ), 
                    failure_threshold = 56, 
                    grpc = kubernetes.client.models.v1/grpc_action.v1.GRPCAction(
                        port = 56, 
                        service = '', ), 
                    http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                        host = '', 
                        http_headers = [
                            kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                                name = '', 
                                value = '', )
                            ], 
                        path = '', 
                        port = kubernetes.client.models.port.port(), 
                        scheme = '', ), 
                    initial_delay_seconds = 56, 
                    period_seconds = 56, 
                    success_threshold = 56, 
                    tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                        host = '', 
                        port = kubernetes.client.models.port.port(), ), 
                    termination_grace_period_seconds = 56, 
                    timeout_seconds = 56, ),
                resize_policy = [
                    kubernetes.client.models.v1/container_resize_policy.v1.ContainerResizePolicy(
                        resource_name = '', 
                        restart_policy = '', )
                    ],
                resources = kubernetes.client.models.v1/resource_requirements.v1.ResourceRequirements(
                    claims = [
                        kubernetes.client.models.v1/resource_claim.v1.ResourceClaim(
                            name = '', )
                        ], 
                    limits = {
                        'key' : ''
                        }, 
                    requests = {
                        'key' : ''
                        }, ),
                restart_policy = '',
                security_context = kubernetes.client.models.v1/security_context.v1.SecurityContext(
                    allow_privilege_escalation = True, 
                    capabilities = kubernetes.client.models.v1/capabilities.v1.Capabilities(
                        add = [
                            ''
                            ], 
                        drop = [
                            ''
                            ], ), 
                    privileged = True, 
                    proc_mount = '', 
                    read_only_root_filesystem = True, 
                    run_as_group = 56, 
                    run_as_non_root = True, 
                    run_as_user = 56, 
                    se_linux_options = kubernetes.client.models.v1/se_linux_options.v1.SELinuxOptions(
                        level = '', 
                        role = '', 
                        type = '', 
                        user = '', ), 
                    seccomp_profile = kubernetes.client.models.v1/seccomp_profile.v1.SeccompProfile(
                        localhost_profile = '', 
                        type = '', ), 
                    windows_options = kubernetes.client.models.v1/windows_security_context_options.v1.WindowsSecurityContextOptions(
                        gmsa_credential_spec = '', 
                        gmsa_credential_spec_name = '', 
                        host_process = True, 
                        run_as_user_name = '', ), ),
                startup_probe = kubernetes.client.models.v1/probe.v1.Probe(
                    exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(
                        command = [
                            ''
                            ], ), 
                    failure_threshold = 56, 
                    grpc = kubernetes.client.models.v1/grpc_action.v1.GRPCAction(
                        port = 56, 
                        service = '', ), 
                    http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                        host = '', 
                        http_headers = [
                            kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                                name = '', 
                                value = '', )
                            ], 
                        path = '', 
                        port = kubernetes.client.models.port.port(), 
                        scheme = '', ), 
                    initial_delay_seconds = 56, 
                    period_seconds = 56, 
                    success_threshold = 56, 
                    tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                        host = '', 
                        port = kubernetes.client.models.port.port(), ), 
                    termination_grace_period_seconds = 56, 
                    timeout_seconds = 56, ),
                stdin = True,
                stdin_once = True,
                termination_message_path = '',
                termination_message_policy = '',
                tty = True,
                volume_devices = [
                    kubernetes.client.models.v1/volume_device.v1.VolumeDevice(
                        device_path = '', 
                        name = '', )
                    ],
                volume_mounts = [
                    kubernetes.client.models.v1/volume_mount.v1.VolumeMount(
                        mount_path = '', 
                        mount_propagation = '', 
                        name = '', 
                        read_only = True, 
                        sub_path = '', 
                        sub_path_expr = '', )
                    ],
                working_dir = ''
            )
        else:
            return V1Container(
                name = '',
        )
        """

    def testV1Container(self):
        """Test V1Container"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
