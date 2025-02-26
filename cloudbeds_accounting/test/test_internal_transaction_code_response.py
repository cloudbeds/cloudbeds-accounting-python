# coding: utf-8

"""
    Accounting service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cloudbeds_accounting.models.internal_transaction_code_response import InternalTransactionCodeResponse

class TestInternalTransactionCodeResponse(unittest.TestCase):
    """InternalTransactionCodeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InternalTransactionCodeResponse:
        """Test InternalTransactionCodeResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InternalTransactionCodeResponse`
        """
        model = InternalTransactionCodeResponse()
        if include_optional:
            return InternalTransactionCodeResponse(
                id = 56,
                code = '',
                description = '',
                group = 'ROOM_REVENUE_RATE'
            )
        else:
            return InternalTransactionCodeResponse(
        )
        """

    def testInternalTransactionCodeResponse(self):
        """Test InternalTransactionCodeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
