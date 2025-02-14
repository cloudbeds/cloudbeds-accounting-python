# coding: utf-8

"""
    Accounting service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cloudbeds_accounting.models.list_transactions_paginated import ListTransactionsPaginated

class TestListTransactionsPaginated(unittest.TestCase):
    """ListTransactionsPaginated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListTransactionsPaginated:
        """Test ListTransactionsPaginated
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListTransactionsPaginated`
        """
        model = ListTransactionsPaginated()
        if include_optional:
            return ListTransactionsPaginated(
                transactions = [
                    cloudbeds_accounting.models.transaction_response.TransactionResponse(
                        id = '', 
                        property_id = '', 
                        internal_transaction_code = '', 
                        custom_transaction_code = '', 
                        general_ledger_custom_code = '', 
                        amount = 1.337, 
                        currency = '', 
                        customer_id = '', 
                        root_id = '', 
                        parent_id = '', 
                        source_id = '', 
                        sub_source_id = '', 
                        source_kind = 'RESERVATION', 
                        account = cloudbeds_accounting.models.account.Account(
                            id = '', 
                            description = '', 
                            name = '', 
                            category = 'DEPOSITS', 
                            chart_of_account_type = 'LIABILITIES', ), 
                        external_relation_id = '', 
                        external_relation_kind = 'ROOM', 
                        origin_id = '', 
                        routed_from = '', 
                        quantity = 56, 
                        description = '', 
                        user_id = '', 
                        source_datetime = '2017-07-21T17:32:28Z', 
                        transaction_datetime = '2017-07-21T17:32:28Z', 
                        transaction_datetime_property_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        service_date = 'Fri Jul 21 02:00:00 CEST 2017', 
                        created_at = '2017-07-21T17:32:28Z', )
                    ],
                next_page_token = ''
            )
        else:
            return ListTransactionsPaginated(
        )
        """

    def testListTransactionsPaginated(self):
        """Test ListTransactionsPaginated"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
