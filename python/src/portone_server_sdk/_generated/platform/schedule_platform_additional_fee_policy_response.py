from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_additional_fee_policy import PlatformAdditionalFeePolicy, _deserialize_platform_additional_fee_policy, _serialize_platform_additional_fee_policy

@dataclass
class SchedulePlatformAdditionalFeePolicyResponse:
    """추가 수수료 정책 업데이트 예약 성공 응답
    """
    scheduled_additional_fee_policy: PlatformAdditionalFeePolicy
    """예약된 추가 수수료 정책
    """


def _serialize_schedule_platform_additional_fee_policy_response(obj: SchedulePlatformAdditionalFeePolicyResponse) -> Any:
    entity = {}
    entity["scheduledAdditionalFeePolicy"] = _serialize_platform_additional_fee_policy(obj.scheduled_additional_fee_policy)
    return entity


def _deserialize_schedule_platform_additional_fee_policy_response(obj: Any) -> SchedulePlatformAdditionalFeePolicyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "scheduledAdditionalFeePolicy" not in obj:
        raise KeyError(f"'scheduledAdditionalFeePolicy' is not in {obj}")
    scheduled_additional_fee_policy = obj["scheduledAdditionalFeePolicy"]
    scheduled_additional_fee_policy = _deserialize_platform_additional_fee_policy(scheduled_additional_fee_policy)
    return SchedulePlatformAdditionalFeePolicyResponse(scheduled_additional_fee_policy)
