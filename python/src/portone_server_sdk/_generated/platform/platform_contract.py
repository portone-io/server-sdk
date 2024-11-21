from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_fee import PlatformFee, _deserialize_platform_fee, _serialize_platform_fee
from ..platform.platform_payer import PlatformPayer, _deserialize_platform_payer, _serialize_platform_payer
from ..platform.platform_settlement_cycle import PlatformSettlementCycle, _deserialize_platform_settlement_cycle, _serialize_platform_settlement_cycle

@dataclass
class PlatformContract:
    """계약

    계약은 플랫폼 고객사가 파트너에게 정산해줄 대금과 정산일을 계산하는 데 적용되는 정보입니다.
    고객사의 플랫폼에서 재화 및 서비스를 판매하기 위한 중개수수료와 판매금에 대한 정산일로 구성되어 있습니다.
    """
    id: str
    """계약 고유 아이디
    """
    graphql_id: str
    name: str
    """계약 이름
    """
    platform_fee: PlatformFee
    """중개수수료
    """
    settlement_cycle: PlatformSettlementCycle
    """정산 주기
    """
    platform_fee_vat_payer: PlatformPayer
    """중개수수료에 대한 부가세 부담 주체
    """
    subtract_payment_vat_amount: bool
    """정산 시 결제금액 부가세 감액 여부

    false인 경우 정산금에서 결제 금액 부가세를 감액하지 않고, true인 경우 정산금에서 결제 금액 부가세를 감액합니다.
    """
    is_archived: bool
    """보관 여부
    """
    applied_at: str
    """변경 적용 시점
    (RFC 3339 date-time)
    """
    memo: Optional[str] = field(default=None)
    """계약 내부 표기를 위한 메모
    """


def _serialize_platform_contract(obj: PlatformContract) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["name"] = obj.name
    entity["platformFee"] = _serialize_platform_fee(obj.platform_fee)
    entity["settlementCycle"] = _serialize_platform_settlement_cycle(obj.settlement_cycle)
    entity["platformFeeVatPayer"] = _serialize_platform_payer(obj.platform_fee_vat_payer)
    entity["subtractPaymentVatAmount"] = obj.subtract_payment_vat_amount
    entity["isArchived"] = obj.is_archived
    entity["appliedAt"] = obj.applied_at
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_platform_contract(obj: Any) -> PlatformContract:
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
    if "platformFee" not in obj:
        raise KeyError(f"'platformFee' is not in {obj}")
    platform_fee = obj["platformFee"]
    platform_fee = _deserialize_platform_fee(platform_fee)
    if "settlementCycle" not in obj:
        raise KeyError(f"'settlementCycle' is not in {obj}")
    settlement_cycle = obj["settlementCycle"]
    settlement_cycle = _deserialize_platform_settlement_cycle(settlement_cycle)
    if "platformFeeVatPayer" not in obj:
        raise KeyError(f"'platformFeeVatPayer' is not in {obj}")
    platform_fee_vat_payer = obj["platformFeeVatPayer"]
    platform_fee_vat_payer = _deserialize_platform_payer(platform_fee_vat_payer)
    if "subtractPaymentVatAmount" not in obj:
        raise KeyError(f"'subtractPaymentVatAmount' is not in {obj}")
    subtract_payment_vat_amount = obj["subtractPaymentVatAmount"]
    if not isinstance(subtract_payment_vat_amount, bool):
        raise ValueError(f"{repr(subtract_payment_vat_amount)} is not bool")
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
    return PlatformContract(id, graphql_id, name, platform_fee, settlement_cycle, platform_fee_vat_payer, subtract_payment_vat_amount, is_archived, applied_at, memo)
