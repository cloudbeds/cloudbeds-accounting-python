# coding: utf-8

"""
    Accounting service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cloudbeds_accounting.models.custom_transaction_codes_update_request import CustomTransactionCodesUpdateRequest

class TestCustomTransactionCodesUpdateRequest(unittest.TestCase):
    """CustomTransactionCodesUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomTransactionCodesUpdateRequest:
        """Test CustomTransactionCodesUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomTransactionCodesUpdateRequest`
        """
        model = CustomTransactionCodesUpdateRequest()
        if include_optional:
            return CustomTransactionCodesUpdateRequest(
                data = [
                    cloudbeds_accounting.models.custom_transaction_codes_update_model.CustomTransactionCodesUpdateModel(
                        id = '', 
                        code = '0', 
                        custom_general_ledger_code_id = '', )
                    ]
            )
        else:
            return CustomTransactionCodesUpdateRequest(
        )
        """

    def testCustomTransactionCodesUpdateRequest(self):
        """Test CustomTransactionCodesUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
