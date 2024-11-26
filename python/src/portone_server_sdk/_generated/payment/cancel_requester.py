from __future__ import annotations
from typing import Any, Literal, Optional, Union

CancelRequester = Union[Literal["CUSTOMER", "ADMIN"], str]


def _serialize_cancel_requester(obj: CancelRequester) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_cancel_requester(obj: Any) -> CancelRequester:
    return obj
