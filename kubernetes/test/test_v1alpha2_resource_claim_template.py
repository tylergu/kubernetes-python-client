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

from kubernetes.client.models.v1alpha2_resource_claim_template import V1alpha2ResourceClaimTemplate

class TestV1alpha2ResourceClaimTemplate(unittest.TestCase):
    """V1alpha2ResourceClaimTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha2ResourceClaimTemplate:
        """Test V1alpha2ResourceClaimTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha2ResourceClaimTemplate`
        """
        model = V1alpha2ResourceClaimTemplate()
        if include_optional:
            return V1alpha2ResourceClaimTemplate(
                api_version = '',
                kind = '',
                metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                    annotations = {
                        'key' : ''
                        }, 
                    creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deletion_grace_period_seconds = 56, 
                    deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finalizers = [
                        ''
                        ], 
                    generate_name = '', 
                    generation = 56, 
                    labels = {
                        'key' : ''
                        }, 
                    managed_fields = [
                        kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                            api_version = '', 
                            fields_type = '', 
                            fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                            manager = '', 
                            operation = '', 
                            subresource = '', 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    name = '', 
                    namespace = '', 
                    owner_references = [
                        kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                            api_version = '', 
                            block_owner_deletion = True, 
                            controller = True, 
                            kind = '', 
                            name = '', 
                            uid = '', )
                        ], 
                    resource_version = '', 
                    self_link = '', 
                    uid = '', ),
                spec = kubernetes.client.models.v1alpha2/resource_claim_template_spec.v1alpha2.ResourceClaimTemplateSpec(
                    metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                        annotations = {
                            'key' : ''
                            }, 
                        creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        deletion_grace_period_seconds = 56, 
                        deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        finalizers = [
                            ''
                            ], 
                        generate_name = '', 
                        generation = 56, 
                        labels = {
                            'key' : ''
                            }, 
                        managed_fields = [
                            kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                api_version = '', 
                                fields_type = '', 
                                fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                manager = '', 
                                operation = '', 
                                subresource = '', 
                                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        name = '', 
                        namespace = '', 
                        owner_references = [
                            kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                api_version = '', 
                                block_owner_deletion = True, 
                                controller = True, 
                                kind = '', 
                                name = '', 
                                uid = '', )
                            ], 
                        resource_version = '', 
                        self_link = '', 
                        uid = '', ), 
                    spec = kubernetes.client.models.v1alpha2/resource_claim_spec.v1alpha2.ResourceClaimSpec(
                        allocation_mode = '', 
                        parameters_ref = kubernetes.client.models.v1alpha2/resource_claim_parameters_reference.v1alpha2.ResourceClaimParametersReference(
                            api_group = '', 
                            kind = '', 
                            name = '', ), 
                        resource_class_name = '', ), )
            )
        else:
            return V1alpha2ResourceClaimTemplate(
                spec = kubernetes.client.models.v1alpha2/resource_claim_template_spec.v1alpha2.ResourceClaimTemplateSpec(
                    metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                        annotations = {
                            'key' : ''
                            }, 
                        creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        deletion_grace_period_seconds = 56, 
                        deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        finalizers = [
                            ''
                            ], 
                        generate_name = '', 
                        generation = 56, 
                        labels = {
                            'key' : ''
                            }, 
                        managed_fields = [
                            kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                api_version = '', 
                                fields_type = '', 
                                fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                manager = '', 
                                operation = '', 
                                subresource = '', 
                                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        name = '', 
                        namespace = '', 
                        owner_references = [
                            kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                api_version = '', 
                                block_owner_deletion = True, 
                                controller = True, 
                                kind = '', 
                                name = '', 
                                uid = '', )
                            ], 
                        resource_version = '', 
                        self_link = '', 
                        uid = '', ), 
                    spec = kubernetes.client.models.v1alpha2/resource_claim_spec.v1alpha2.ResourceClaimSpec(
                        allocation_mode = '', 
                        parameters_ref = kubernetes.client.models.v1alpha2/resource_claim_parameters_reference.v1alpha2.ResourceClaimParametersReference(
                            api_group = '', 
                            kind = '', 
                            name = '', ), 
                        resource_class_name = '', ), ),
        )
        """

    def testV1alpha2ResourceClaimTemplate(self):
        """Test V1alpha2ResourceClaimTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
