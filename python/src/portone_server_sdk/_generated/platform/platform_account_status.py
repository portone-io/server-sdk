from __future__ import annotations
from typing import Any, Literal, Optional

PlatformAccountStatus = Literal["VERIFYING", "VERIFIED", "VERIFY_FAILED", "NOT_VERIFIED", "EXPIRED", "UNKNOWN"]
"""플랫폼 계좌 상태
"""


def _serialize_platform_account_status(obj: PlatformAccountStatus) -> Any:
    return obj


def _deserialize_platform_account_status(obj: Any) -> PlatformAccountStatus:
    if obj not in ["VERIFYING", "VERIFIED", "VERIFY_FAILED", "NOT_VERIFIED", "EXPIRED", "UNKNOWN"]:
        raise ValueError(f"{repr(obj)} is not PlatformAccountStatus")
    return obj
