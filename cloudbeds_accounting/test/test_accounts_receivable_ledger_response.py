# coding: utf-8

"""
    Accounting service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cloudbeds_accounting.models.accounts_receivable_ledger_response import AccountsReceivableLedgerResponse

class TestAccountsReceivableLedgerResponse(unittest.TestCase):
    """AccountsReceivableLedgerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountsReceivableLedgerResponse:
        """Test AccountsReceivableLedgerResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountsReceivableLedgerResponse`
        """
        model = AccountsReceivableLedgerResponse()
        if include_optional:
            return AccountsReceivableLedgerResponse(
                id = '',
                name = '0',
                description = '',
                status = 'OPEN',
                property_id = '',
                total = 1.337,
                paid = 1.337,
                balance = 1.337,
                created_at = '2017-07-21T17:32:28Z',
                updated_at = '2017-07-21T17:32:28Z'
            )
        else:
            return AccountsReceivableLedgerResponse(
        )
        """

    def testAccountsReceivableLedgerResponse(self):
        """Test AccountsReceivableLedgerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
