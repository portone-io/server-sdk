from __future__ import annotations
from typing import Any, Literal, Optional, Union

Type = Union[Literal["PARTNER_PAYOUT", "REMIT"], str]


def _serialize_type(obj: Type) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_type(obj: Any) -> Type:
    return obj
