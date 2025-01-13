from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.date_time_range import DateTimeRange, _deserialize_date_time_range, _serialize_date_time_range

@dataclass
class PlatformPayoutFilterInputCriteria:
    """검색 기준 입력 정보
    """
    timestamp_range: Optional[DateTimeRange] = field(default=None)
    """시간 범위
    """
    payout_id: Optional[str] = field(default=None)
    """지급 아이디
    """
    bulk_payout_id: Optional[str] = field(default=None)
    """일괄 지급 아이디
    """


def _serialize_platform_payout_filter_input_criteria(obj: PlatformPayoutFilterInputCriteria) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.timestamp_range is not None:
        entity["timestampRange"] = _serialize_date_time_range(obj.timestamp_range)
    if obj.payout_id is not None:
        entity["payoutId"] = obj.payout_id
    if obj.bulk_payout_id is not None:
        entity["bulkPayoutId"] = obj.bulk_payout_id
    return entity


def _deserialize_platform_payout_filter_input_criteria(obj: Any) -> PlatformPayoutFilterInputCriteria:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "timestampRange" in obj:
        timestamp_range = obj["timestampRange"]
        timestamp_range = _deserialize_date_time_range(timestamp_range)
    else:
        timestamp_range = None
    if "payoutId" in obj:
        payout_id = obj["payoutId"]
        if not isinstance(payout_id, str):
            raise ValueError(f"{repr(payout_id)} is not str")
    else:
        payout_id = None
    if "bulkPayoutId" in obj:
        bulk_payout_id = obj["bulkPayoutId"]
        if not isinstance(bulk_payout_id, str):
            raise ValueError(f"{repr(bulk_payout_id)} is not str")
    else:
        bulk_payout_id = None
    return PlatformPayoutFilterInputCriteria(timestamp_range, payout_id, bulk_payout_id)
