from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CancelPlatformAdditionalFeePolicyScheduleResponse:
    """추가 수수료 정책 예약 업데이트 취소 성공 응답
    """
    pass


def _serialize_cancel_platform_additional_fee_policy_schedule_response(obj: CancelPlatformAdditionalFeePolicyScheduleResponse) -> Any:
    entity = {}
    return entity


def _deserialize_cancel_platform_additional_fee_policy_schedule_response(obj: Any) -> CancelPlatformAdditionalFeePolicyScheduleResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return CancelPlatformAdditionalFeePolicyScheduleResponse()
