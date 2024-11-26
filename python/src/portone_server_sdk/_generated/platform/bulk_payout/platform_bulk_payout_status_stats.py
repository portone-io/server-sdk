from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformBulkPayoutStatusStats:
    scheduled: int
    """(int64)
    """
    preparing: int
    """(int64)
    """
    prepared: int
    """(int64)
    """
    ongoing: int
    """(int64)
    """
    stopped: int
    """(int64)
    """
    cancelled: int
    """(int64)
    """
    completed: int
    """(int64)
    """


def _serialize_platform_bulk_payout_status_stats(obj: PlatformBulkPayoutStatusStats) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["scheduled"] = obj.scheduled
    entity["preparing"] = obj.preparing
    entity["prepared"] = obj.prepared
    entity["ongoing"] = obj.ongoing
    entity["stopped"] = obj.stopped
    entity["cancelled"] = obj.cancelled
    entity["completed"] = obj.completed
    return entity


def _deserialize_platform_bulk_payout_status_stats(obj: Any) -> PlatformBulkPayoutStatusStats:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "scheduled" not in obj:
        raise KeyError(f"'scheduled' is not in {obj}")
    scheduled = obj["scheduled"]
    if not isinstance(scheduled, int):
        raise ValueError(f"{repr(scheduled)} is not int")
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
    if "stopped" not in obj:
        raise KeyError(f"'stopped' is not in {obj}")
    stopped = obj["stopped"]
    if not isinstance(stopped, int):
        raise ValueError(f"{repr(stopped)} is not int")
    if "cancelled" not in obj:
        raise KeyError(f"'cancelled' is not in {obj}")
    cancelled = obj["cancelled"]
    if not isinstance(cancelled, int):
        raise ValueError(f"{repr(cancelled)} is not int")
    if "completed" not in obj:
        raise KeyError(f"'completed' is not in {obj}")
    completed = obj["completed"]
    if not isinstance(completed, int):
        raise ValueError(f"{repr(completed)} is not int")
    return PlatformBulkPayoutStatusStats(scheduled, preparing, prepared, ongoing, stopped, cancelled, completed)
