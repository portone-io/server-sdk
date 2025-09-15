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
        raise ValueError(f"{repr(obj)} is not dict")
    if "preparing" not in obj:
        raise KeyError(f"'preparing' is not in {obj}")
    preparing = obj["preparing"]
    if not isinstance(preparing, int):
        raise ValueError(f"{repr(preparing)} is not int")
    if "prepared" not in obj:
        raise KeyError(f"'prepared' is not in {obj}")
    prepared = obj["prepared"]
    if not isinstance(prepared, int):
        raise ValueError(f"{repr(prepared)} is not int")
    if "ongoing" not in obj:
        raise KeyError(f"'ongoing' is not in {obj}")
    ongoing = obj["ongoing"]
    if not isinstance(ongoing, int):
        raise ValueError(f"{repr(ongoing)} is not int")
    if "postProcessPending" not in obj:
        raise KeyError(f"'postProcessPending' is not in {obj}")
    post_process_pending = obj["postProcessPending"]
    if not isinstance(post_process_pending, int):
        raise ValueError(f"{repr(post_process_pending)} is not int")
    if "completed" not in obj:
        raise KeyError(f"'completed' is not in {obj}")
    completed = obj["completed"]
    if not isinstance(completed, int):
        raise ValueError(f"{repr(completed)} is not int")
    if "cancelled" not in obj:
        raise KeyError(f"'cancelled' is not in {obj}")
    cancelled = obj["cancelled"]
    if not isinstance(cancelled, int):
        raise ValueError(f"{repr(cancelled)} is not int")
    return PlatformBulkPayoutStatusStats(preparing, prepared, ongoing, post_process_pending, completed, cancelled)
