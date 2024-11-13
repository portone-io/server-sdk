from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class UpdatePlatformDiscountSharePolicyBody:
    """할인 분담 정책 업데이트를 위한 입력 정보

    값이 명시되지 않은 필드는 업데이트하지 않습니다.
    """
    name: Optional[str] = field(default=None)
    """할인 분담 정책 이름
    """
    partner_share_rate: Optional[int] = field(default=None)
    """할인 분담율

    파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
    (int32)
    """
    memo: Optional[str] = field(default=None)
    """해당 할인 분담에 대한 메모
    """


def _serialize_update_platform_discount_share_policy_body(obj: UpdatePlatformDiscountSharePolicyBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.partner_share_rate is not None:
        entity["partnerShareRate"] = obj.partner_share_rate
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_update_platform_discount_share_policy_body(obj: Any) -> UpdatePlatformDiscountSharePolicyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "partnerShareRate" in obj:
        partner_share_rate = obj["partnerShareRate"]
        if not isinstance(partner_share_rate, int):
            raise ValueError(f"{repr(partner_share_rate)} is not int")
    else:
        partner_share_rate = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return UpdatePlatformDiscountSharePolicyBody(name, partner_share_rate, memo)
