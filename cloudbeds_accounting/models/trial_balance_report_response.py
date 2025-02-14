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
from cloudbeds_accounting.models.trial_balance_report_guest_ledger import TrialBalanceReportGuestLedger
from cloudbeds_accounting.models.trial_balance_report_ledger_balances import TrialBalanceReportLedgerBalances
from cloudbeds_accounting.models.trial_balance_report_summary import TrialBalanceReportSummary
from typing import Optional, Set
from typing_extensions import Self

class TrialBalanceReportResponse(BaseModel):
    """
    TrialBalanceReportResponse
    """ # noqa: E501
    summary: Optional[TrialBalanceReportSummary] = None
    ledger_balances: Optional[TrialBalanceReportLedgerBalances] = Field(default=None, alias="ledgerBalances")
    guest_ledger: Optional[TrialBalanceReportGuestLedger] = Field(default=None, alias="guestLedger")
    __properties: ClassVar[List[str]] = ["summary", "ledgerBalances", "guestLedger"]

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
        """Create an instance of TrialBalanceReportResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ledger_balances
        if self.ledger_balances:
            _dict['ledgerBalances'] = self.ledger_balances.to_dict()
        # override the default output from pydantic by calling `to_dict()` of guest_ledger
        if self.guest_ledger:
            _dict['guestLedger'] = self.guest_ledger.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrialBalanceReportResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "summary": TrialBalanceReportSummary.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
            "ledgerBalances": TrialBalanceReportLedgerBalances.from_dict(obj["ledgerBalances"]) if obj.get("ledgerBalances") is not None else None,
            "guestLedger": TrialBalanceReportGuestLedger.from_dict(obj["guestLedger"]) if obj.get("guestLedger") is not None else None
        })
        return _obj


