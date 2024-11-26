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
        raise ValueError(f"{repr(obj)} is not dict")
    if "first" not in obj:
        raise KeyError(f"'first' is not in {obj}")
    first = obj["first"]
    if not isinstance(first, str):
        raise ValueError(f"{repr(first)} is not str")
    if "last" not in obj:
        raise KeyError(f"'last' is not in {obj}")
    last = obj["last"]
    if not isinstance(last, str):
        raise ValueError(f"{repr(last)} is not str")
    return CustomerSeparatedName(first, last)
