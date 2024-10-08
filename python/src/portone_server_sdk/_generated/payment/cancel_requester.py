from __future__ import annotations
from typing import Any, Literal, Optional

CancelRequester = Literal["CUSTOMER", "ADMIN"]


def _serialize_cancel_requester(obj: CancelRequester) -> Any:
    return obj


def _deserialize_cancel_requester(obj: Any) -> CancelRequester:
    if obj not in ["CUSTOMER", "ADMIN"]:
        raise ValueError(f"{repr(obj)} is not CancelRequester")
    return obj
