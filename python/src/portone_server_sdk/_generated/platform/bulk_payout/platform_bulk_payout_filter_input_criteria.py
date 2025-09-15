from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.date_time_range import DateTimeRange, _deserialize_date_time_range, _serialize_date_time_range

@dataclass
class PlatformBulkPayoutFilterInputCriteria:
    timestamp_range: Optional[DateTimeRange] = field(default=None)
    """생성 일시 범위
    """
    status_updated_timestamp_range: Optional[DateTimeRange] = field(default=None)
    """상태 업데이트 일시 범위
    """
    bulk_payout_id: Optional[str] = field(default=None)
    """일괄 지급 아이디
    """


def _serialize_platform_bulk_payout_filter_input_criteria(obj: PlatformBulkPayoutFilterInputCriteria) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.timestamp_range is not None:
        entity["timestampRange"] = _serialize_date_time_range(obj.timestamp_range)
    if obj.status_updated_timestamp_range is not None:
        entity["statusUpdatedTimestampRange"] = _serialize_date_time_range(obj.status_updated_timestamp_range)
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
    if "statusUpdatedTimestampRange" in obj:
        status_updated_timestamp_range = obj["statusUpdatedTimestampRange"]
        status_updated_timestamp_range = _deserialize_date_time_range(status_updated_timestamp_range)
    else:
        status_updated_timestamp_range = None
    if "bulkPayoutId" in obj:
        bulk_payout_id = obj["bulkPayoutId"]
        if not isinstance(bulk_payout_id, str):
            raise ValueError(f"{repr(bulk_payout_id)} is not str")
    else:
        bulk_payout_id = None
    return PlatformBulkPayoutFilterInputCriteria(timestamp_range, status_updated_timestamp_range, bulk_payout_id)
