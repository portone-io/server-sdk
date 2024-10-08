from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CreatePlatformDiscountSharePolicyBody:
    """할인 분담 정책 생성을 위한 입력 정보
    """
    name: str
    """할인 분담에 부여할 이름
    """
    partner_share_rate: int
    """파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
    (int32)
    """
    id: Optional[str]
    """할인 분담에 부여할 고유 아이디

    명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
    """
    memo: Optional[str]
    """해당 할인 분담에 대한 메모 ex) 파트너 브랜드 쿠폰
    """


def _serialize_create_platform_discount_share_policy_body(obj: CreatePlatformDiscountSharePolicyBody) -> Any:
    entity = {}
    entity["name"] = obj.name
    entity["partnerShareRate"] = obj.partner_share_rate
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_create_platform_discount_share_policy_body(obj: Any) -> CreatePlatformDiscountSharePolicyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "partnerShareRate" not in obj:
        raise KeyError(f"'partnerShareRate' is not in {obj}")
    partner_share_rate = obj["partnerShareRate"]
    if not isinstance(partner_share_rate, int):
        raise ValueError(f"{repr(partner_share_rate)} is not int")
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return CreatePlatformDiscountSharePolicyBody(name, partner_share_rate, id, memo)
