from __future__ import annotations
from typing import Any, Literal, Optional

PlatformBulkPayoutStatus = Literal["SCHEDULED", "PREPARING", "PREPARED", "ONGOING", "CANCELLED", "STOPPED", "COMPLETED"]


def _serialize_platform_bulk_payout_status(obj: PlatformBulkPayoutStatus) -> Any:
    return obj


def _deserialize_platform_bulk_payout_status(obj: Any) -> PlatformBulkPayoutStatus:
    if obj not in ["SCHEDULED", "PREPARING", "PREPARED", "ONGOING", "CANCELLED", "STOPPED", "COMPLETED"]:
        raise ValueError(f"{repr(obj)} is not PlatformBulkPayoutStatus")
    return obj
