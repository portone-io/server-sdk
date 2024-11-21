from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.policy.platform_discount_share_policy_filter_input_keyword import PlatformDiscountSharePolicyFilterInputKeyword, _deserialize_platform_discount_share_policy_filter_input_keyword, _serialize_platform_discount_share_policy_filter_input_keyword

@dataclass
class PlatformDiscountSharePolicyFilterInput:
    """할인 분담 정책 다건 조회를 위한 필터 조건
    """
    is_archived: Optional[bool] = field(default=None)
    """보관 조회 여부

    true 이면 보관된 할인 분담 정책을 조회하고, false 이면 보관되지 않은 할인 분담 정책을 조회합니다. 기본값은 false 입니다.
    """
    partner_share_rates: Optional[list[int]] = field(default=None)
    """하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 파트너 분담율을 가진 할인 분담 정책만 조회합니다.
    """
    keyword: Optional[PlatformDiscountSharePolicyFilterInputKeyword] = field(default=None)
    """검색 키워드
    """


def _serialize_platform_discount_share_policy_filter_input(obj: PlatformDiscountSharePolicyFilterInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.is_archived is not None:
        entity["isArchived"] = obj.is_archived
    if obj.partner_share_rates is not None:
        entity["partnerShareRates"] = obj.partner_share_rates
    if obj.keyword is not None:
        entity["keyword"] = _serialize_platform_discount_share_policy_filter_input_keyword(obj.keyword)
    return entity


def _deserialize_platform_discount_share_policy_filter_input(obj: Any) -> PlatformDiscountSharePolicyFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "isArchived" in obj:
        is_archived = obj["isArchived"]
        if not isinstance(is_archived, bool):
            raise ValueError(f"{repr(is_archived)} is not bool")
    else:
        is_archived = None
    if "partnerShareRates" in obj:
        partner_share_rates = obj["partnerShareRates"]
        if not isinstance(partner_share_rates, list):
            raise ValueError(f"{repr(partner_share_rates)} is not list")
        for i, item in enumerate(partner_share_rates):
            if not isinstance(item, int):
                raise ValueError(f"{repr(item)} is not int")
    else:
        partner_share_rates = None
    if "keyword" in obj:
        keyword = obj["keyword"]
        keyword = _deserialize_platform_discount_share_policy_filter_input_keyword(keyword)
    else:
        keyword = None
    return PlatformDiscountSharePolicyFilterInput(is_archived, partner_share_rates, keyword)
