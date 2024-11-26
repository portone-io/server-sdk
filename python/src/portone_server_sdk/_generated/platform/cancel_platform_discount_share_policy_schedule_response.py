from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CancelPlatformDiscountSharePolicyScheduleResponse:
    """할인 분담 정책 예약 업데이트 취소 성공 응답
    """
    pass


def _serialize_cancel_platform_discount_share_policy_schedule_response(obj: CancelPlatformDiscountSharePolicyScheduleResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_cancel_platform_discount_share_policy_schedule_response(obj: Any) -> CancelPlatformDiscountSharePolicyScheduleResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return CancelPlatformDiscountSharePolicyScheduleResponse()
