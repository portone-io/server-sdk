from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_discount_share_policy import PlatformDiscountSharePolicy, _deserialize_platform_discount_share_policy, _serialize_platform_discount_share_policy

@dataclass
class ReschedulePlatformDiscountSharePolicyResponse:
    """할인 분담 정책 예약 업데이트 재설정 성공 응답
    """
    scheduled_discount_share_policy: PlatformDiscountSharePolicy
    """예약된 할인 분담 정보
    """


def _serialize_reschedule_platform_discount_share_policy_response(obj: ReschedulePlatformDiscountSharePolicyResponse) -> Any:
    entity = {}
    entity["scheduledDiscountSharePolicy"] = _serialize_platform_discount_share_policy(obj.scheduled_discount_share_policy)
    return entity


def _deserialize_reschedule_platform_discount_share_policy_response(obj: Any) -> ReschedulePlatformDiscountSharePolicyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "scheduledDiscountSharePolicy" not in obj:
        raise KeyError(f"'scheduledDiscountSharePolicy' is not in {obj}")
    scheduled_discount_share_policy = obj["scheduledDiscountSharePolicy"]
    scheduled_discount_share_policy = _deserialize_platform_discount_share_policy(scheduled_discount_share_policy)
    return ReschedulePlatformDiscountSharePolicyResponse(scheduled_discount_share_policy)
