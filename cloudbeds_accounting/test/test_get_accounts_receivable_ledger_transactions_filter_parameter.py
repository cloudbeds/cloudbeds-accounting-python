# coding: utf-8

"""
    Accounting service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cloudbeds_accounting.models.get_accounts_receivable_ledger_transactions_filter_parameter import GetAccountsReceivableLedgerTransactionsFilterParameter

class TestGetAccountsReceivableLedgerTransactionsFilterParameter(unittest.TestCase):
    """GetAccountsReceivableLedgerTransactionsFilterParameter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccountsReceivableLedgerTransactionsFilterParameter:
        """Test GetAccountsReceivableLedgerTransactionsFilterParameter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccountsReceivableLedgerTransactionsFilterParameter`
        """
        model = GetAccountsReceivableLedgerTransactionsFilterParameter()
        if include_optional:
            return GetAccountsReceivableLedgerTransactionsFilterParameter(
                transaction_states = [
                    'POSTED'
                    ],
                search_query = '012',
                transaction_date_from = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                transaction_date_to = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                checkin_date_from = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                checkin_date_to = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                checkout_date_from = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                checkout_date_to = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                transaction_type = [
                    'TRANSFER'
                    ],
                user_id = [
                    56
                    ],
                sort_by = 'CHECKOUT_DATE',
                sort_direction = 'asc'
            )
        else:
            return GetAccountsReceivableLedgerTransactionsFilterParameter(
        )
        """

    def testGetAccountsReceivableLedgerTransactionsFilterParameter(self):
        """Test GetAccountsReceivableLedgerTransactionsFilterParameter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
