from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformPayoutStatus = Union[Literal["PREPARED", "CANCELLED", "STOPPED", "PROCESSING", "SUCCEEDED", "FAILED", "SCHEDULED"], str]


def _serialize_platform_payout_status(obj: PlatformPayoutStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_payout_status(obj: Any) -> PlatformPayoutStatus:
    return obj
