# coding: utf-8

"""
    Accounting service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cloudbeds_accounting.models.custom_general_ledger_code_model import CustomGeneralLedgerCodeModel

class TestCustomGeneralLedgerCodeModel(unittest.TestCase):
    """CustomGeneralLedgerCodeModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomGeneralLedgerCodeModel:
        """Test CustomGeneralLedgerCodeModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomGeneralLedgerCodeModel`
        """
        model = CustomGeneralLedgerCodeModel()
        if include_optional:
            return CustomGeneralLedgerCodeModel(
                id = '',
                version = 56,
                name = '0',
                code = '0',
                group = 'payments',
                archived = True
            )
        else:
            return CustomGeneralLedgerCodeModel(
                name = '0',
                code = '0',
        )
        """

    def testCustomGeneralLedgerCodeModel(self):
        """Test CustomGeneralLedgerCodeModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
