from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformDiscountSharePolicyFilterOptions:
    """할인 분담 정책 필터 옵션 조회 성공 응답 정보
    """
    partner_share_rates: list[int]
    """조회된 파트너 분담율 리스트
    """


def _serialize_platform_discount_share_policy_filter_options(obj: PlatformDiscountSharePolicyFilterOptions) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["partnerShareRates"] = obj.partner_share_rates
    return entity


def _deserialize_platform_discount_share_policy_filter_options(obj: Any) -> PlatformDiscountSharePolicyFilterOptions:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "partnerShareRates" not in obj:
        raise KeyError("Missing required field 'partnerShareRates'")
    partner_share_rates = obj["partnerShareRates"]
    if not isinstance(partner_share_rates, list):
        raise ValueError("Expected list for partner_share_rates")
    for i, item in enumerate(partner_share_rates):
        if not isinstance(item, int):
            raise ValueError("Expected int for item")
    return PlatformDiscountSharePolicyFilterOptions(partner_share_rates)
