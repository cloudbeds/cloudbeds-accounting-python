# coding: utf-8

"""
    Accounting service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from cloudbeds_accounting.models.trial_balance_report_code_info import TrialBalanceReportCodeInfo
from typing import Optional, Set
from typing_extensions import Self

class TrialBalanceReportLedgerBalances(BaseModel):
    """
    TrialBalanceReportLedgerBalances
    """ # noqa: E501
    deposit_ledger: Optional[List[TrialBalanceReportCodeInfo]] = Field(default=None, alias="depositLedger")
    guest_ledger: Optional[List[TrialBalanceReportCodeInfo]] = Field(default=None, alias="guestLedger")
    accounts_receivable: Optional[List[TrialBalanceReportCodeInfo]] = Field(default=None, alias="accountsReceivable")
    __properties: ClassVar[List[str]] = ["depositLedger", "guestLedger", "accountsReceivable"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TrialBalanceReportLedgerBalances from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in deposit_ledger (list)
        _items = []
        if self.deposit_ledger:
            for _item_deposit_ledger in self.deposit_ledger:
                if _item_deposit_ledger:
                    _items.append(_item_deposit_ledger.to_dict())
            _dict['depositLedger'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in guest_ledger (list)
        _items = []
        if self.guest_ledger:
            for _item_guest_ledger in self.guest_ledger:
                if _item_guest_ledger:
                    _items.append(_item_guest_ledger.to_dict())
            _dict['guestLedger'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in accounts_receivable (list)
        _items = []
        if self.accounts_receivable:
            for _item_accounts_receivable in self.accounts_receivable:
                if _item_accounts_receivable:
                    _items.append(_item_accounts_receivable.to_dict())
            _dict['accountsReceivable'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrialBalanceReportLedgerBalances from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "depositLedger": [TrialBalanceReportCodeInfo.from_dict(_item) for _item in obj["depositLedger"]] if obj.get("depositLedger") is not None else None,
            "guestLedger": [TrialBalanceReportCodeInfo.from_dict(_item) for _item in obj["guestLedger"]] if obj.get("guestLedger") is not None else None,
            "accountsReceivable": [TrialBalanceReportCodeInfo.from_dict(_item) for _item in obj["accountsReceivable"]] if obj.get("accountsReceivable") is not None else None
        })
        return _obj


