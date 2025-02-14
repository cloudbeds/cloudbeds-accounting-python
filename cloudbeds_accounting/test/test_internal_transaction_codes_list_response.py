# coding: utf-8

"""
    Accounting service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cloudbeds_accounting.models.internal_transaction_codes_list_response import InternalTransactionCodesListResponse

class TestInternalTransactionCodesListResponse(unittest.TestCase):
    """InternalTransactionCodesListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InternalTransactionCodesListResponse:
        """Test InternalTransactionCodesListResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InternalTransactionCodesListResponse`
        """
        model = InternalTransactionCodesListResponse()
        if include_optional:
            return InternalTransactionCodesListResponse(
                content = [
                    cloudbeds_accounting.models.internal_transaction_code_response.InternalTransactionCodeResponse(
                        id = 56, 
                        code = '', 
                        description = '', 
                        group = 'ROOM_REVENUE_RATE', )
                    ]
            )
        else:
            return InternalTransactionCodesListResponse(
        )
        """

    def testInternalTransactionCodesListResponse(self):
        """Test InternalTransactionCodesListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
