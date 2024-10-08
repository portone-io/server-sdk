from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_additional_fee_policy import PlatformAdditionalFeePolicy, _deserialize_platform_additional_fee_policy, _serialize_platform_additional_fee_policy

@dataclass
class ReschedulePlatformAdditionalFeePolicyResponse:
    """추가 수수료 정책 예약 업데이트 재설정 성공 응답
    """
    scheduled_additional_fee_policy: PlatformAdditionalFeePolicy
    """예약된 추가 수수료 정책
    """


def _serialize_reschedule_platform_additional_fee_policy_response(obj: ReschedulePlatformAdditionalFeePolicyResponse) -> Any:
    entity = {}
    entity["scheduledAdditionalFeePolicy"] = _serialize_platform_additional_fee_policy(obj.scheduled_additional_fee_policy)
    return entity


def _deserialize_reschedule_platform_additional_fee_policy_response(obj: Any) -> ReschedulePlatformAdditionalFeePolicyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "scheduledAdditionalFeePolicy" not in obj:
        raise KeyError(f"'scheduledAdditionalFeePolicy' is not in {obj}")
    scheduled_additional_fee_policy = obj["scheduledAdditionalFeePolicy"]
    scheduled_additional_fee_policy = _deserialize_platform_additional_fee_policy(scheduled_additional_fee_policy)
    return ReschedulePlatformAdditionalFeePolicyResponse(scheduled_additional_fee_policy)
