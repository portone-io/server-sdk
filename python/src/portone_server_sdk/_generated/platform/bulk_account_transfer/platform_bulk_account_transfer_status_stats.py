from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformBulkAccountTransferStatusStats:
    prepared: int
    """(int64)
    """
    scheduled: int
    """(int64)
    """
    ongoing: int
    """(int64)
    """
    completed: int
    """(int64)
    """


def _serialize_platform_bulk_account_transfer_status_stats(obj: PlatformBulkAccountTransferStatusStats) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["prepared"] = obj.prepared
    entity["scheduled"] = obj.scheduled
    entity["ongoing"] = obj.ongoing
    entity["completed"] = obj.completed
    return entity


def _deserialize_platform_bulk_account_transfer_status_stats(obj: Any) -> PlatformBulkAccountTransferStatusStats:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "prepared" not in obj:
        raise KeyError(f"'prepared' is not in {obj}")
    prepared = obj["prepared"]
    if not isinstance(prepared, int):
        raise ValueError(f"{repr(prepared)} is not int")
    if "scheduled" not in obj:
        raise KeyError(f"'scheduled' is not in {obj}")
    scheduled = obj["scheduled"]
    if not isinstance(scheduled, int):
        raise ValueError(f"{repr(scheduled)} is not int")
    if "ongoing" not in obj:
        raise KeyError(f"'ongoing' is not in {obj}")
    ongoing = obj["ongoing"]
    if not isinstance(ongoing, int):
        raise ValueError(f"{repr(ongoing)} is not int")
    if "completed" not in obj:
        raise KeyError(f"'completed' is not in {obj}")
    completed = obj["completed"]
    if not isinstance(completed, int):
        raise ValueError(f"{repr(completed)} is not int")
    return PlatformBulkAccountTransferStatusStats(prepared, scheduled, ongoing, completed)
