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


class AccountCategory(str, Enum):
    """
    Account category
    """

    """
    allowed enum values
    """
    DEPOSITS = 'DEPOSITS'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AccountCategory from a JSON string"""
        return cls(json.loads(json_str))


