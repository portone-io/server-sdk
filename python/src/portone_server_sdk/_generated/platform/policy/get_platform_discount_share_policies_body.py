from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...platform.policy.platform_discount_share_policy_filter_input import PlatformDiscountSharePolicyFilterInput, _deserialize_platform_discount_share_policy_filter_input, _serialize_platform_discount_share_policy_filter_input

@dataclass
class GetPlatformDiscountSharePoliciesBody:
    """할인 분담 정책 다건 조회를 위한 입력 정보
    """
    page: Optional[PageInput] = field(default=None)
    """요청할 페이지 정보
    """
    filter: Optional[PlatformDiscountSharePolicyFilterInput] = field(default=None)
    """조회할 할인 분담 정책 조건 필터
    """


def _serialize_get_platform_discount_share_policies_body(obj: GetPlatformDiscountSharePoliciesBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    if obj.filter is not None:
        entity["filter"] = _serialize_platform_discount_share_policy_filter_input(obj.filter)
    return entity


def _deserialize_get_platform_discount_share_policies_body(obj: Any) -> GetPlatformDiscountSharePoliciesBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "page" in obj:
        page = obj["page"]
        page = _deserialize_page_input(page)
    else:
        page = None
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_platform_discount_share_policy_filter_input(filter)
    else:
        filter = None
    return GetPlatformDiscountSharePoliciesBody(page, filter)
