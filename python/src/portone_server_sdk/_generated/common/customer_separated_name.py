from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CustomerSeparatedName:
    """고객 분리형 이름
    """
    first: str
    """이름
    """
    last: str
    """성
    """


def _serialize_customer_separated_name(obj: CustomerSeparatedName) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["first"] = obj.first
    entity["last"] = obj.last
    return entity


def _deserialize_customer_separated_name(obj: Any) -> CustomerSeparatedName:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "first" not in obj:
        raise KeyError("Missing required field 'first'")
    first = obj["first"]
    if not isinstance(first, str):
        raise ValueError("Expected str for first")
    if "last" not in obj:
        raise KeyError("Missing required field 'last'")
    last = obj["last"]
    if not isinstance(last, str):
        raise ValueError("Expected str for last")
    return CustomerSeparatedName(first, last)
