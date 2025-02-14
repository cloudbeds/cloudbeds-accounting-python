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
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from cloudbeds_accounting.models.and_or_group import AndOrGroup
from cloudbeds_accounting.models.field_filter import FieldFilter
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

FILTERS_ONE_OF_SCHEMAS = ["AndOrGroup", "FieldFilter"]

class Filters(BaseModel):
    """
    Filters
    """
    # data type: AndOrGroup
    oneof_schema_1_validator: Optional[AndOrGroup] = None
    # data type: FieldFilter
    oneof_schema_2_validator: Optional[FieldFilter] = None
    actual_instance: Optional[Union[AndOrGroup, FieldFilter]] = None
    one_of_schemas: Set[str] = { "AndOrGroup", "FieldFilter" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = Filters.model_construct()
        error_messages = []
        match = 0
        # validate data type: AndOrGroup
        if not isinstance(v, AndOrGroup):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AndOrGroup`")
        else:
            match += 1
        # validate data type: FieldFilter
        if not isinstance(v, FieldFilter):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FieldFilter`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in Filters with oneOf schemas: AndOrGroup, FieldFilter. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in Filters with oneOf schemas: AndOrGroup, FieldFilter. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into AndOrGroup
        try:
            instance.actual_instance = AndOrGroup.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FieldFilter
        try:
            instance.actual_instance = FieldFilter.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into Filters with oneOf schemas: AndOrGroup, FieldFilter. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Filters with oneOf schemas: AndOrGroup, FieldFilter. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], AndOrGroup, FieldFilter]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


