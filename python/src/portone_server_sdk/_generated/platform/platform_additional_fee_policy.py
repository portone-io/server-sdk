from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_fee import PlatformFee, _deserialize_platform_fee, _serialize_platform_fee
from portone_server_sdk._generated.platform.platform_payer import PlatformPayer, _deserialize_platform_payer, _serialize_platform_payer

@dataclass
class PlatformAdditionalFeePolicy:
    """추가 수수료 정책

    추가 수수료 정책는 고객사의 주문건에 대한 중개수수료에 별도로 추가로 부여되는 수수료입니다. 대표적인 사용 예시로 풀필먼트 수수료, 로켓배송 수수료, 마케팅 채널 수수료등이 있습니다.
    """
    id: str
    """추가 수수료 정책 고유 아이디
    """
    graphql_id: str
    name: str
    """추가 수수료 정책 이름
    """
    fee: PlatformFee
    """책정 수수료
    """
    vat_payer: PlatformPayer
    """부가세를 부담할 주체
    """
    is_archived: bool
    """보관 여부
    """
    applied_at: str
    """변경 적용 시점
    (RFC 3339 date-time)
    """
    memo: Optional[str]
    """해당 추가 수수료 정책에 대한 메모
    """


def _serialize_platform_additional_fee_policy(obj: PlatformAdditionalFeePolicy) -> Any:
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["name"] = obj.name
    entity["fee"] = _serialize_platform_fee(obj.fee)
    entity["vatPayer"] = _serialize_platform_payer(obj.vat_payer)
    entity["isArchived"] = obj.is_archived
    entity["appliedAt"] = obj.applied_at
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_platform_additional_fee_policy(obj: Any) -> PlatformAdditionalFeePolicy:
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
    if "fee" not in obj:
        raise KeyError(f"'fee' is not in {obj}")
    fee = obj["fee"]
    fee = _deserialize_platform_fee(fee)
    if "vatPayer" not in obj:
        raise KeyError(f"'vatPayer' is not in {obj}")
    vat_payer = obj["vatPayer"]
    vat_payer = _deserialize_platform_payer(vat_payer)
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
    return PlatformAdditionalFeePolicy(id, graphql_id, name, fee, vat_payer, is_archived, applied_at, memo)
