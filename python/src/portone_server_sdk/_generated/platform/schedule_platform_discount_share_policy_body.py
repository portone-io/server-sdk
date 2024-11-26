from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.update_platform_discount_share_policy_body import UpdatePlatformDiscountSharePolicyBody, _deserialize_update_platform_discount_share_policy_body, _serialize_update_platform_discount_share_policy_body

@dataclass
class SchedulePlatformDiscountSharePolicyBody:
    """할인 분담 정책 업데이트 예약을 위한 입력 정보
    """
    update: UpdatePlatformDiscountSharePolicyBody
    """반영할 업데이트 내용
    """
    applied_at: str
    """업데이트 적용 시점
    (RFC 3339 date-time)
    """


def _serialize_schedule_platform_discount_share_policy_body(obj: SchedulePlatformDiscountSharePolicyBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["update"] = _serialize_update_platform_discount_share_policy_body(obj.update)
    entity["appliedAt"] = obj.applied_at
    return entity


def _deserialize_schedule_platform_discount_share_policy_body(obj: Any) -> SchedulePlatformDiscountSharePolicyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "update" not in obj:
        raise KeyError(f"'update' is not in {obj}")
    update = obj["update"]
    update = _deserialize_update_platform_discount_share_policy_body(update)
    if "appliedAt" not in obj:
        raise KeyError(f"'appliedAt' is not in {obj}")
    applied_at = obj["appliedAt"]
    if not isinstance(applied_at, str):
        raise ValueError(f"{repr(applied_at)} is not str")
    return SchedulePlatformDiscountSharePolicyBody(update, applied_at)
