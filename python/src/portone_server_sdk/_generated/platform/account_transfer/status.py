from __future__ import annotations
from typing import Any, Literal, Optional, Union

Status = Union[Literal["PROCESSING", "ASYNC_PROCESSING", "SUCCEEDED", "FAILED"], str]
"""계좌 이체 상태
"""


def _serialize_status(obj: Status) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_status(obj: Any) -> Status:
    return obj
