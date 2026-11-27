from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformAccountTransferStatusStats:
    prepared: int
    """(int64)
    """
    scheduled: int
    """(int64)
    """
    cancelled: int
    """(int64)
    """
    stopped: int
    """(int64)
    """
    processing: int
    """(int64)
    """
    async_processing: int
    """(int64)
    """
    succeeded: int
    """(int64)
    """
    failed: int
    """(int64)
    """


def _serialize_platform_account_transfer_status_stats(obj: PlatformAccountTransferStatusStats) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["prepared"] = obj.prepared
    entity["scheduled"] = obj.scheduled
    entity["cancelled"] = obj.cancelled
    entity["stopped"] = obj.stopped
    entity["processing"] = obj.processing
    entity["asyncProcessing"] = obj.async_processing
    entity["succeeded"] = obj.succeeded
    entity["failed"] = obj.failed
    return entity


def _deserialize_platform_account_transfer_status_stats(obj: Any) -> PlatformAccountTransferStatusStats:
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
    if "cancelled" not in obj:
        raise KeyError("Missing required field 'cancelled'")
    cancelled = obj["cancelled"]
    if not isinstance(cancelled, int):
        raise ValueError("Expected int for cancelled")
    if "stopped" not in obj:
        raise KeyError("Missing required field 'stopped'")
    stopped = obj["stopped"]
    if not isinstance(stopped, int):
        raise ValueError("Expected int for stopped")
    if "processing" not in obj:
        raise KeyError("Missing required field 'processing'")
    processing = obj["processing"]
    if not isinstance(processing, int):
        raise ValueError("Expected int for processing")
    if "asyncProcessing" not in obj:
        raise KeyError("Missing required field 'asyncProcessing'")
    async_processing = obj["asyncProcessing"]
    if not isinstance(async_processing, int):
        raise ValueError("Expected int for async_processing")
    if "succeeded" not in obj:
        raise KeyError("Missing required field 'succeeded'")
    succeeded = obj["succeeded"]
    if not isinstance(succeeded, int):
        raise ValueError("Expected int for succeeded")
    if "failed" not in obj:
        raise KeyError("Missing required field 'failed'")
    failed = obj["failed"]
    if not isinstance(failed, int):
        raise ValueError("Expected int for failed")
    return PlatformAccountTransferStatusStats(prepared, scheduled, cancelled, stopped, processing, async_processing, succeeded, failed)
