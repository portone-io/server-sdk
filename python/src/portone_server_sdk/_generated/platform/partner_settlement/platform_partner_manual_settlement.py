from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner
from ...platform.partner_settlement.platform_partner_settlement_status import PlatformPartnerSettlementStatus, _deserialize_platform_partner_settlement_status, _serialize_platform_partner_settlement_status

@dataclass
class PlatformPartnerManualSettlement:
    id: str
    """정산내역 아이디
    """
    graphql_id: str
    partner: PlatformPartner
    """파트너
    """
    settlement_date: str
    """정산 일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    settlement_currency: Currency
    """정산 통화
    """
    status: PlatformPartnerSettlementStatus
    """정산 상태
    """
    amount: int
    """정산 금액
    (int64)
    """
    is_for_test: bool
    """테스트 모드 여부
    """
    memo: Optional[str] = field(default=None)
    """메모
    """


def _serialize_platform_partner_manual_settlement(obj: PlatformPartnerManualSettlement) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "MANUAL"
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["partner"] = _serialize_platform_partner(obj.partner)
    entity["settlementDate"] = obj.settlement_date
    entity["settlementCurrency"] = _serialize_currency(obj.settlement_currency)
    entity["status"] = _serialize_platform_partner_settlement_status(obj.status)
    entity["amount"] = obj.amount
    entity["isForTest"] = obj.is_for_test
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_platform_partner_manual_settlement(obj: Any) -> PlatformPartnerManualSettlement:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "MANUAL":
        raise ValueError(f"{repr(type)} is not 'MANUAL'")
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
    if "partner" not in obj:
        raise KeyError(f"'partner' is not in {obj}")
    partner = obj["partner"]
    partner = _deserialize_platform_partner(partner)
    if "settlementDate" not in obj:
        raise KeyError(f"'settlementDate' is not in {obj}")
    settlement_date = obj["settlementDate"]
    if not isinstance(settlement_date, str):
        raise ValueError(f"{repr(settlement_date)} is not str")
    if "settlementCurrency" not in obj:
        raise KeyError(f"'settlementCurrency' is not in {obj}")
    settlement_currency = obj["settlementCurrency"]
    settlement_currency = _deserialize_currency(settlement_currency)
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_platform_partner_settlement_status(status)
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError(f"{repr(amount)} is not int")
    if "isForTest" not in obj:
        raise KeyError(f"'isForTest' is not in {obj}")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError(f"{repr(is_for_test)} is not bool")
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return PlatformPartnerManualSettlement(id, graphql_id, partner, settlement_date, settlement_currency, status, amount, is_for_test, memo)
