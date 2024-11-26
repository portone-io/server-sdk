from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_additional_fee_policy import PlatformAdditionalFeePolicy, _deserialize_platform_additional_fee_policy, _serialize_platform_additional_fee_policy

@dataclass
class ArchivePlatformAdditionalFeePolicyResponse:
    """추가 수수료 정책 보관 성공 응답
    """
    additional_fee_policy: PlatformAdditionalFeePolicy
    """보관된 추가 수수료 정책
    """


def _serialize_archive_platform_additional_fee_policy_response(obj: ArchivePlatformAdditionalFeePolicyResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["additionalFeePolicy"] = _serialize_platform_additional_fee_policy(obj.additional_fee_policy)
    return entity


def _deserialize_archive_platform_additional_fee_policy_response(obj: Any) -> ArchivePlatformAdditionalFeePolicyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "additionalFeePolicy" not in obj:
        raise KeyError(f"'additionalFeePolicy' is not in {obj}")
    additional_fee_policy = obj["additionalFeePolicy"]
    additional_fee_policy = _deserialize_platform_additional_fee_policy(additional_fee_policy)
    return ArchivePlatformAdditionalFeePolicyResponse(additional_fee_policy)
