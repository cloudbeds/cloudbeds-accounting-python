# coding: utf-8

"""
    Accounting service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cloudbeds_accounting.models.field_filter import FieldFilter

class TestFieldFilter(unittest.TestCase):
    """FieldFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FieldFilter:
        """Test FieldFilter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FieldFilter`
        """
        model = FieldFilter()
        if include_optional:
            return FieldFilter(
                operator = 'greater_than_or_equal',
                value = None,
                var_field = ''
            )
        else:
            return FieldFilter(
                operator = 'greater_than_or_equal',
                var_field = '',
        )
        """

    def testFieldFilter(self):
        """Test FieldFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
