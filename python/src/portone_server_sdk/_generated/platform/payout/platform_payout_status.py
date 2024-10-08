from __future__ import annotations
from typing import Any, Literal, Optional

PlatformPayoutStatus = Literal["PREPARED", "CANCELLED", "STOPPED", "PROCESSING", "SUCCEEDED", "FAILED"]


def _serialize_platform_payout_status(obj: PlatformPayoutStatus) -> Any:
    return obj


def _deserialize_platform_payout_status(obj: Any) -> PlatformPayoutStatus:
    if obj not in ["PREPARED", "CANCELLED", "STOPPED", "PROCESSING", "SUCCEEDED", "FAILED"]:
        raise ValueError(f"{repr(obj)} is not PlatformPayoutStatus")
    return obj
