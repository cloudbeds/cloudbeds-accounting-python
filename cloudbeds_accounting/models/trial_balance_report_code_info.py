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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class TrialBalanceReportCodeInfo(BaseModel):
    """
    TrialBalanceReportCodeInfo
    """ # noqa: E501
    code: Optional[StrictStr] = Field(default=None, description="Transaction code")
    description: Optional[StrictStr] = Field(default=None, description="Description of the row")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total amount for specific code")
    __properties: ClassVar[List[str]] = ["code", "description", "amount"]

    @field_validator('description')
    def description_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RATE', 'RATE_A', 'RATE_V', 'ROOM_REVENUE', 'ROOM_REVENUE_A', 'ROOM_REVENUE_V', 'CANCELLATION', 'CANCELLATION_A', 'CANCELLATION_V', 'NO_SHOW', 'NO_SHOW_A', 'NO_SHOW_V', 'ITEM_SERVICE', 'ITEM_SERVICE_A', 'ITEM_SERVICE_V', 'ADDON', 'ADDON_A', 'ADDON_V', 'CUSTOM_ITEM_POS', 'CUSTOM_ITEM_POS_A', 'CUSTOM_ITEM_POS_V', 'FEE', 'FEE_A', 'FEE_V', 'TAX', 'TAX_A', 'TAX_V', 'PAYMENT', 'PAYMENT_V', 'PAYMENT_R', 'PAYMENT_CASH', 'PAYMENT_CASH_V', 'PAYMENT_BANK', 'PAYMENT_BANK_V', 'PAYMENT_CARD', 'PAYMENT_CARD_V', 'REFUND', 'REFUND_CASH', 'REFUND_BANK', 'REFUND_CARD', 'DEPOSIT_LEDGER_BALANCE', 'DEPOSIT_LEDGER_BALANCE_PREVIOUS_DAY', 'DEPOSIT_PAYMENTS', 'DEPOSIT_TRANSFER_OUT', 'GUEST_LEDGER_BALANCE', 'GUEST_LEDGER_BALANCE_PREVIOUS_DAY', 'GUEST_LEDGER_CHARGES', 'DEPOSIT_TRANSFER_IN', 'GUEST_LEDGER_PAYMENTS', 'AR_BALANCE', 'AR_BALANCE_PREVIOUS_DAY', 'AR_TRANSFER_IN', 'AR_PAYMENTS']):
            raise ValueError("must be one of enum values ('RATE', 'RATE_A', 'RATE_V', 'ROOM_REVENUE', 'ROOM_REVENUE_A', 'ROOM_REVENUE_V', 'CANCELLATION', 'CANCELLATION_A', 'CANCELLATION_V', 'NO_SHOW', 'NO_SHOW_A', 'NO_SHOW_V', 'ITEM_SERVICE', 'ITEM_SERVICE_A', 'ITEM_SERVICE_V', 'ADDON', 'ADDON_A', 'ADDON_V', 'CUSTOM_ITEM_POS', 'CUSTOM_ITEM_POS_A', 'CUSTOM_ITEM_POS_V', 'FEE', 'FEE_A', 'FEE_V', 'TAX', 'TAX_A', 'TAX_V', 'PAYMENT', 'PAYMENT_V', 'PAYMENT_R', 'PAYMENT_CASH', 'PAYMENT_CASH_V', 'PAYMENT_BANK', 'PAYMENT_BANK_V', 'PAYMENT_CARD', 'PAYMENT_CARD_V', 'REFUND', 'REFUND_CASH', 'REFUND_BANK', 'REFUND_CARD', 'DEPOSIT_LEDGER_BALANCE', 'DEPOSIT_LEDGER_BALANCE_PREVIOUS_DAY', 'DEPOSIT_PAYMENTS', 'DEPOSIT_TRANSFER_OUT', 'GUEST_LEDGER_BALANCE', 'GUEST_LEDGER_BALANCE_PREVIOUS_DAY', 'GUEST_LEDGER_CHARGES', 'DEPOSIT_TRANSFER_IN', 'GUEST_LEDGER_PAYMENTS', 'AR_BALANCE', 'AR_BALANCE_PREVIOUS_DAY', 'AR_TRANSFER_IN', 'AR_PAYMENTS')")
        return value

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
        """Create an instance of TrialBalanceReportCodeInfo from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrialBalanceReportCodeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "description": obj.get("description"),
            "amount": obj.get("amount")
        })
        return _obj


