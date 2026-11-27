from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_payout_status_stats import PlatformPayoutStatusStats, _deserialize_platform_payout_status_stats, _serialize_platform_payout_status_stats

@dataclass
class PlatformBulkPayoutStats:
    amount: PlatformPayoutStatusStats
    count: PlatformPayoutStatusStats


def _serialize_platform_bulk_payout_stats(obj: PlatformBulkPayoutStats) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["amount"] = _serialize_platform_payout_status_stats(obj.amount)
    entity["count"] = _serialize_platform_payout_status_stats(obj.count)
    return entity


def _deserialize_platform_bulk_payout_stats(obj: Any) -> PlatformBulkPayoutStats:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "amount" not in obj:
        raise KeyError("Missing required field 'amount'")
    amount = obj["amount"]
    amount = _deserialize_platform_payout_status_stats(amount)
    if "count" not in obj:
        raise KeyError("Missing required field 'count'")
    count = obj["count"]
    count = _deserialize_platform_payout_status_stats(count)
    return PlatformBulkPayoutStats(amount, count)
