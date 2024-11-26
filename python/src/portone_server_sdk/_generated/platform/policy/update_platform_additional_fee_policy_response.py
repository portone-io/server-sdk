from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_additional_fee_policy import PlatformAdditionalFeePolicy, _deserialize_platform_additional_fee_policy, _serialize_platform_additional_fee_policy

@dataclass
class UpdatePlatformAdditionalFeePolicyResponse:
    """추가 수수료 정책 업데이트 성공 응답
    """
    additional_fee_policy: PlatformAdditionalFeePolicy
    """업데이트된 추가 수수료 정책
    """


def _serialize_update_platform_additional_fee_policy_response(obj: UpdatePlatformAdditionalFeePolicyResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["additionalFeePolicy"] = _serialize_platform_additional_fee_policy(obj.additional_fee_policy)
    return entity


def _deserialize_update_platform_additional_fee_policy_response(obj: Any) -> UpdatePlatformAdditionalFeePolicyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "additionalFeePolicy" not in obj:
        raise KeyError(f"'additionalFeePolicy' is not in {obj}")
    additional_fee_policy = obj["additionalFeePolicy"]
    additional_fee_policy = _deserialize_platform_additional_fee_policy(additional_fee_policy)
    return UpdatePlatformAdditionalFeePolicyResponse(additional_fee_policy)
