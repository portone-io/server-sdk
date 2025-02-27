from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformBulkTaskProgressStats:
    prepared_count: int
    """(int64)
    """
    processing_count: int
    """(int64)
    """
    succeeded_count: int
    """(int64)
    """
    failed_count: int
    """(int64)
    """
    canceled_count: int
    """(int64)
    """


def _serialize_platform_bulk_task_progress_stats(obj: PlatformBulkTaskProgressStats) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["preparedCount"] = obj.prepared_count
    entity["processingCount"] = obj.processing_count
    entity["succeededCount"] = obj.succeeded_count
    entity["failedCount"] = obj.failed_count
    entity["canceledCount"] = obj.canceled_count
    return entity


def _deserialize_platform_bulk_task_progress_stats(obj: Any) -> PlatformBulkTaskProgressStats:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "preparedCount" not in obj:
        raise KeyError(f"'preparedCount' is not in {obj}")
    prepared_count = obj["preparedCount"]
    if not isinstance(prepared_count, int):
        raise ValueError(f"{repr(prepared_count)} is not int")
    if "processingCount" not in obj:
        raise KeyError(f"'processingCount' is not in {obj}")
    processing_count = obj["processingCount"]
    if not isinstance(processing_count, int):
        raise ValueError(f"{repr(processing_count)} is not int")
    if "succeededCount" not in obj:
        raise KeyError(f"'succeededCount' is not in {obj}")
    succeeded_count = obj["succeededCount"]
    if not isinstance(succeeded_count, int):
        raise ValueError(f"{repr(succeeded_count)} is not int")
    if "failedCount" not in obj:
        raise KeyError(f"'failedCount' is not in {obj}")
    failed_count = obj["failedCount"]
    if not isinstance(failed_count, int):
        raise ValueError(f"{repr(failed_count)} is not int")
    if "canceledCount" not in obj:
        raise KeyError(f"'canceledCount' is not in {obj}")
    canceled_count = obj["canceledCount"]
    if not isinstance(canceled_count, int):
        raise ValueError(f"{repr(canceled_count)} is not int")
    return PlatformBulkTaskProgressStats(prepared_count, processing_count, succeeded_count, failed_count, canceled_count)
