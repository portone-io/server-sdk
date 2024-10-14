from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPayoutStatusStats:
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
    entity = {}
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
        raise ValueError(f"{repr(obj)} is not dict")
    if "prepared" not in obj:
        raise KeyError(f"'prepared' is not in {obj}")
    prepared = obj["prepared"]
    if not isinstance(prepared, int):
        raise ValueError(f"{repr(prepared)} is not int")
    if "cancelled" not in obj:
        raise KeyError(f"'cancelled' is not in {obj}")
    cancelled = obj["cancelled"]
    if not isinstance(cancelled, int):
        raise ValueError(f"{repr(cancelled)} is not int")
    if "stopped" not in obj:
        raise KeyError(f"'stopped' is not in {obj}")
    stopped = obj["stopped"]
    if not isinstance(stopped, int):
        raise ValueError(f"{repr(stopped)} is not int")
    if "processing" not in obj:
        raise KeyError(f"'processing' is not in {obj}")
    processing = obj["processing"]
    if not isinstance(processing, int):
        raise ValueError(f"{repr(processing)} is not int")
    if "succeeded" not in obj:
        raise KeyError(f"'succeeded' is not in {obj}")
    succeeded = obj["succeeded"]
    if not isinstance(succeeded, int):
        raise ValueError(f"{repr(succeeded)} is not int")
    if "failed" not in obj:
        raise KeyError(f"'failed' is not in {obj}")
    failed = obj["failed"]
    if not isinstance(failed, int):
        raise ValueError(f"{repr(failed)} is not int")
    if "scheduled" not in obj:
        raise KeyError(f"'scheduled' is not in {obj}")
    scheduled = obj["scheduled"]
    if not isinstance(scheduled, int):
        raise ValueError(f"{repr(scheduled)} is not int")
    return PlatformPayoutStatusStats(prepared, cancelled, stopped, processing, succeeded, failed, scheduled)
