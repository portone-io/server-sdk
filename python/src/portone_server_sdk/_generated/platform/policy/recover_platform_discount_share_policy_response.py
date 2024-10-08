from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_discount_share_policy import PlatformDiscountSharePolicy, _deserialize_platform_discount_share_policy, _serialize_platform_discount_share_policy

@dataclass
class RecoverPlatformDiscountSharePolicyResponse:
    """할인 분담 복원 성공 응답
    """
    discount_share_policy: PlatformDiscountSharePolicy
    """복원된 할인 분담
    """


def _serialize_recover_platform_discount_share_policy_response(obj: RecoverPlatformDiscountSharePolicyResponse) -> Any:
    entity = {}
    entity["discountSharePolicy"] = _serialize_platform_discount_share_policy(obj.discount_share_policy)
    return entity


def _deserialize_recover_platform_discount_share_policy_response(obj: Any) -> RecoverPlatformDiscountSharePolicyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "discountSharePolicy" not in obj:
        raise KeyError(f"'discountSharePolicy' is not in {obj}")
    discount_share_policy = obj["discountSharePolicy"]
    discount_share_policy = _deserialize_platform_discount_share_policy(discount_share_policy)
    return RecoverPlatformDiscountSharePolicyResponse(discount_share_policy)
