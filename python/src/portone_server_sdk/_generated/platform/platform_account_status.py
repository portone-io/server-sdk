from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformAccountStatus = Union[Literal["VERIFIED", "VERIFY_FAILED", "VERIFY_ERROR", "NOT_VERIFIED", "UNKNOWN"], str]
"""플랫폼 계좌 상태
"""


def _serialize_platform_account_status(obj: PlatformAccountStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_account_status(obj: Any) -> PlatformAccountStatus:
    return obj
