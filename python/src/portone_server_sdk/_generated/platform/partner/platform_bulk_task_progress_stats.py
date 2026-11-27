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
        raise ValueError("Expected dict for obj")
    if "preparedCount" not in obj:
        raise KeyError("Missing required field 'preparedCount'")
    prepared_count = obj["preparedCount"]
    if not isinstance(prepared_count, int):
        raise ValueError("Expected int for prepared_count")
    if "processingCount" not in obj:
        raise KeyError("Missing required field 'processingCount'")
    processing_count = obj["processingCount"]
    if not isinstance(processing_count, int):
        raise ValueError("Expected int for processing_count")
    if "succeededCount" not in obj:
        raise KeyError("Missing required field 'succeededCount'")
    succeeded_count = obj["succeededCount"]
    if not isinstance(succeeded_count, int):
        raise ValueError("Expected int for succeeded_count")
    if "failedCount" not in obj:
        raise KeyError("Missing required field 'failedCount'")
    failed_count = obj["failedCount"]
    if not isinstance(failed_count, int):
        raise ValueError("Expected int for failed_count")
    if "canceledCount" not in obj:
        raise KeyError("Missing required field 'canceledCount'")
    canceled_count = obj["canceledCount"]
    if not isinstance(canceled_count, int):
        raise ValueError("Expected int for canceled_count")
    return PlatformBulkTaskProgressStats(prepared_count, processing_count, succeeded_count, failed_count, canceled_count)
