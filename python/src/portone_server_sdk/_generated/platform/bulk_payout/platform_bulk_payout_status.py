from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformBulkPayoutStatus = Union[Literal["SCHEDULED", "PREPARING", "PREPARED", "ONGOING", "CANCELLED", "STOPPED", "COMPLETED"], str]


def _serialize_platform_bulk_payout_status(obj: PlatformBulkPayoutStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_bulk_payout_status(obj: Any) -> PlatformBulkPayoutStatus:
    return obj
