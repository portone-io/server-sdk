from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.update_platform_additional_fee_policy_body import UpdatePlatformAdditionalFeePolicyBody, _deserialize_update_platform_additional_fee_policy_body, _serialize_update_platform_additional_fee_policy_body

@dataclass
class SchedulePlatformAdditionalFeePolicyBody:
    """추가 수수료 정책 업데이트 예약을 위한 입력 정보
    """
    update: UpdatePlatformAdditionalFeePolicyBody
    """반영할 업데이트 내용
    """
    applied_at: str
    """업데이트 적용 시점
    (RFC 3339 date-time)
    """


def _serialize_schedule_platform_additional_fee_policy_body(obj: SchedulePlatformAdditionalFeePolicyBody) -> Any:
    entity = {}
    entity["update"] = _serialize_update_platform_additional_fee_policy_body(obj.update)
    entity["appliedAt"] = obj.applied_at
    return entity


def _deserialize_schedule_platform_additional_fee_policy_body(obj: Any) -> SchedulePlatformAdditionalFeePolicyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "update" not in obj:
        raise KeyError(f"'update' is not in {obj}")
    update = obj["update"]
    update = _deserialize_update_platform_additional_fee_policy_body(update)
    if "appliedAt" not in obj:
        raise KeyError(f"'appliedAt' is not in {obj}")
    applied_at = obj["appliedAt"]
    if not isinstance(applied_at, str):
        raise ValueError(f"{repr(applied_at)} is not str")
    return SchedulePlatformAdditionalFeePolicyBody(update, applied_at)
