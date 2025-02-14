# coding: utf-8

"""
    Accounting service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cloudbeds_accounting.models.accounts_receivable_ledger_reservation_balance_transfer_response import AccountsReceivableLedgerReservationBalanceTransferResponse

class TestAccountsReceivableLedgerReservationBalanceTransferResponse(unittest.TestCase):
    """AccountsReceivableLedgerReservationBalanceTransferResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountsReceivableLedgerReservationBalanceTransferResponse:
        """Test AccountsReceivableLedgerReservationBalanceTransferResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountsReceivableLedgerReservationBalanceTransferResponse`
        """
        model = AccountsReceivableLedgerReservationBalanceTransferResponse()
        if include_optional:
            return AccountsReceivableLedgerReservationBalanceTransferResponse(
                transaction = cloudbeds_accounting.models.accounts_receivable_ledger_reservation_balance_transfer_response_transaction.AccountsReceivableLedgerReservationBalanceTransferResponse_transaction(
                    id = '', 
                    amount = 1.337, ),
                accounts_receivable_id = ''
            )
        else:
            return AccountsReceivableLedgerReservationBalanceTransferResponse(
        )
        """

    def testAccountsReceivableLedgerReservationBalanceTransferResponse(self):
        """Test AccountsReceivableLedgerReservationBalanceTransferResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
