# coding: utf-8

"""
    Accounting service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SourceKind(str, Enum):
    """
    Source Kind. At the moment only available RESERVATION | GROUP_PROFILE | HOUSE_ACCOUNT | ACCOUNTS_RECEIVABLE.
    """

    """
    allowed enum values
    """
    RESERVATION = 'RESERVATION'
    HOUSE_ACCOUNT = 'HOUSE_ACCOUNT'
    GROUP_PROFILE = 'GROUP_PROFILE'
    ACCOUNTS_RECEIVABLE_LEDGER = 'ACCOUNTS_RECEIVABLE_LEDGER'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SourceKind from a JSON string"""
        return cls(json.loads(json_str))


