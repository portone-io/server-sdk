from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformDiscountSharePolicy:
    """할인 분담 정책

    할인 분담은 고객사의 주문건에 쿠폰 및 포인트와 같은 할인금액이 적용될 때, 파트너 정산 시 할인금액에 대한 분담 정책을 가지는 객체입니다.
    할인 유형에 대한 아이디와 메모, 그리고 파트너 분담율을 가집니다.
    """
    id: str
    graphql_id: str
    name: str
    """할인 분담 정책 이름
    """
    partner_share_rate: int
    """할인 분담율

    파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
    (int32)
    """
    is_archived: bool
    """보관 여부
    """
    applied_at: str
    """변경 적용 시점
    (RFC 3339 date-time)
    """
    memo: Optional[str]
    """해당 할인 분담에 대한 메모
    """


def _serialize_platform_discount_share_policy(obj: PlatformDiscountSharePolicy) -> Any:
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["name"] = obj.name
    entity["partnerShareRate"] = obj.partner_share_rate
    entity["isArchived"] = obj.is_archived
    entity["appliedAt"] = obj.applied_at
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_platform_discount_share_policy(obj: Any) -> PlatformDiscountSharePolicy:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "graphqlId" not in obj:
        raise KeyError(f"'graphqlId' is not in {obj}")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError(f"{repr(graphql_id)} is not str")
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
    if "isArchived" not in obj:
        raise KeyError(f"'isArchived' is not in {obj}")
    is_archived = obj["isArchived"]
    if not isinstance(is_archived, bool):
        raise ValueError(f"{repr(is_archived)} is not bool")
    if "appliedAt" not in obj:
        raise KeyError(f"'appliedAt' is not in {obj}")
    applied_at = obj["appliedAt"]
    if not isinstance(applied_at, str):
        raise ValueError(f"{repr(applied_at)} is not str")
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return PlatformDiscountSharePolicy(id, graphql_id, name, partner_share_rate, is_archived, applied_at, memo)
