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
        raise ValueError("Expected dict for obj")
    if "prepared" not in obj:
        raise KeyError("Missing required field 'prepared'")
    prepared = obj["prepared"]
    if not isinstance(prepared, int):
        raise ValueError("Expected int for prepared")
    if "scheduled" not in obj:
        raise KeyError("Missing required field 'scheduled'")
    scheduled = obj["scheduled"]
    if not isinstance(scheduled, int):
        raise ValueError("Expected int for scheduled")
    if "ongoing" not in obj:
        raise KeyError("Missing required field 'ongoing'")
    ongoing = obj["ongoing"]
    if not isinstance(ongoing, int):
        raise ValueError("Expected int for ongoing")
    if "completed" not in obj:
        raise KeyError("Missing required field 'completed'")
    completed = obj["completed"]
    if not isinstance(completed, int):
        raise ValueError("Expected int for completed")
    return PlatformBulkAccountTransferStatusStats(prepared, scheduled, ongoing, completed)
