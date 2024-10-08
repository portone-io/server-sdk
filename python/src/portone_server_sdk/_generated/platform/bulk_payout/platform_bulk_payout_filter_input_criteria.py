from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.date_time_range import DateTimeRange, _deserialize_date_time_range, _serialize_date_time_range

@dataclass
class PlatformBulkPayoutFilterInputCriteria:
    timestamp_range: Optional[DateTimeRange]
    bulk_payout_id: Optional[str]


def _serialize_platform_bulk_payout_filter_input_criteria(obj: PlatformBulkPayoutFilterInputCriteria) -> Any:
    entity = {}
    if obj.timestamp_range is not None:
        entity["timestampRange"] = _serialize_date_time_range(obj.timestamp_range)
    if obj.bulk_payout_id is not None:
        entity["bulkPayoutId"] = obj.bulk_payout_id
    return entity


def _deserialize_platform_bulk_payout_filter_input_criteria(obj: Any) -> PlatformBulkPayoutFilterInputCriteria:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "timestampRange" in obj:
        timestamp_range = obj["timestampRange"]
        timestamp_range = _deserialize_date_time_range(timestamp_range)
    else:
        timestamp_range = None
    if "bulkPayoutId" in obj:
        bulk_payout_id = obj["bulkPayoutId"]
        if not isinstance(bulk_payout_id, str):
            raise ValueError(f"{repr(bulk_payout_id)} is not str")
    else:
        bulk_payout_id = None
    return PlatformBulkPayoutFilterInputCriteria(timestamp_range, bulk_payout_id)
