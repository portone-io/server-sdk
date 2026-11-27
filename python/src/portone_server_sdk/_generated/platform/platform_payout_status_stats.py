from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPayoutStatusStats:
    confirmed: int
    """(int64)
    """
    prepared: int
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
    succeeded: int
    """(int64)
    """
    failed: int
    """(int64)
    """
    scheduled: int
    """(int64)
    """


def _serialize_platform_payout_status_stats(obj: PlatformPayoutStatusStats) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["confirmed"] = obj.confirmed
    entity["prepared"] = obj.prepared
    entity["cancelled"] = obj.cancelled
    entity["stopped"] = obj.stopped
    entity["processing"] = obj.processing
    entity["succeeded"] = obj.succeeded
    entity["failed"] = obj.failed
    entity["scheduled"] = obj.scheduled
    return entity


def _deserialize_platform_payout_status_stats(obj: Any) -> PlatformPayoutStatusStats:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "confirmed" not in obj:
        raise KeyError("Missing required field 'confirmed'")
    confirmed = obj["confirmed"]
    if not isinstance(confirmed, int):
        raise ValueError("Expected int for confirmed")
    if "prepared" not in obj:
        raise KeyError("Missing required field 'prepared'")
    prepared = obj["prepared"]
    if not isinstance(prepared, int):
        raise ValueError("Expected int for prepared")
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
    if "scheduled" not in obj:
        raise KeyError("Missing required field 'scheduled'")
    scheduled = obj["scheduled"]
    if not isinstance(scheduled, int):
        raise ValueError("Expected int for scheduled")
    return PlatformPayoutStatusStats(confirmed, prepared, cancelled, stopped, processing, succeeded, failed, scheduled)
