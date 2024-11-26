from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_discount_share_policy import PlatformDiscountSharePolicy, _deserialize_platform_discount_share_policy, _serialize_platform_discount_share_policy

@dataclass
class ArchivePlatformDiscountSharePolicyResponse:
    """할인 분담 보관 성공 응답
    """
    discount_share_policy: PlatformDiscountSharePolicy
    """보관된 할인 분담
    """


def _serialize_archive_platform_discount_share_policy_response(obj: ArchivePlatformDiscountSharePolicyResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["discountSharePolicy"] = _serialize_platform_discount_share_policy(obj.discount_share_policy)
    return entity


def _deserialize_archive_platform_discount_share_policy_response(obj: Any) -> ArchivePlatformDiscountSharePolicyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "discountSharePolicy" not in obj:
        raise KeyError(f"'discountSharePolicy' is not in {obj}")
    discount_share_policy = obj["discountSharePolicy"]
    discount_share_policy = _deserialize_platform_discount_share_policy(discount_share_policy)
    return ArchivePlatformDiscountSharePolicyResponse(discount_share_policy)
