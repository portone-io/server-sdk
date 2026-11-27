from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformBulkPayoutStatusStats:
    preparing: int
    """(int64)
    """
    prepared: int
    """(int64)
    """
    ongoing: int
    """(int64)
    """
    post_process_pending: int
    """(int64)
    """
    completed: int
    """(int64)
    """
    cancelled: int
    """(int64)
    """


def _serialize_platform_bulk_payout_status_stats(obj: PlatformBulkPayoutStatusStats) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["preparing"] = obj.preparing
    entity["prepared"] = obj.prepared
    entity["ongoing"] = obj.ongoing
    entity["postProcessPending"] = obj.post_process_pending
    entity["completed"] = obj.completed
    entity["cancelled"] = obj.cancelled
    return entity


def _deserialize_platform_bulk_payout_status_stats(obj: Any) -> PlatformBulkPayoutStatusStats:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "preparing" not in obj:
        raise KeyError("Missing required field 'preparing'")
    preparing = obj["preparing"]
    if not isinstance(preparing, int):
        raise ValueError("Expected int for preparing")
    if "prepared" not in obj:
        raise KeyError("Missing required field 'prepared'")
    prepared = obj["prepared"]
    if not isinstance(prepared, int):
        raise ValueError("Expected int for prepared")
    if "ongoing" not in obj:
        raise KeyError("Missing required field 'ongoing'")
    ongoing = obj["ongoing"]
    if not isinstance(ongoing, int):
        raise ValueError("Expected int for ongoing")
    if "postProcessPending" not in obj:
        raise KeyError("Missing required field 'postProcessPending'")
    post_process_pending = obj["postProcessPending"]
    if not isinstance(post_process_pending, int):
        raise ValueError("Expected int for post_process_pending")
    if "completed" not in obj:
        raise KeyError("Missing required field 'completed'")
    completed = obj["completed"]
    if not isinstance(completed, int):
        raise ValueError("Expected int for completed")
    if "cancelled" not in obj:
        raise KeyError("Missing required field 'cancelled'")
    cancelled = obj["cancelled"]
    if not isinstance(cancelled, int):
        raise ValueError("Expected int for cancelled")
    return PlatformBulkPayoutStatusStats(preparing, prepared, ongoing, post_process_pending, completed, cancelled)
