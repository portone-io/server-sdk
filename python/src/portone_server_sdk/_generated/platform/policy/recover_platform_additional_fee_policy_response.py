from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_additional_fee_policy import PlatformAdditionalFeePolicy, _deserialize_platform_additional_fee_policy, _serialize_platform_additional_fee_policy

@dataclass
class RecoverPlatformAdditionalFeePolicyResponse:
    """추가 수수료 정책 복원 성공 응답
    """
    additional_fee_policy: PlatformAdditionalFeePolicy
    """복원된 추가 수수료 정책
    """


def _serialize_recover_platform_additional_fee_policy_response(obj: RecoverPlatformAdditionalFeePolicyResponse) -> Any:
    entity = {}
    entity["additionalFeePolicy"] = _serialize_platform_additional_fee_policy(obj.additional_fee_policy)
    return entity


def _deserialize_recover_platform_additional_fee_policy_response(obj: Any) -> RecoverPlatformAdditionalFeePolicyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "additionalFeePolicy" not in obj:
        raise KeyError(f"'additionalFeePolicy' is not in {obj}")
    additional_fee_policy = obj["additionalFeePolicy"]
    additional_fee_policy = _deserialize_platform_additional_fee_policy(additional_fee_policy)
    return RecoverPlatformAdditionalFeePolicyResponse(additional_fee_policy)
