from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency
from portone_server_sdk._generated.platform.date_range import DateRange, _deserialize_date_range, _serialize_date_range
from portone_server_sdk._generated.platform.platform_contract import PlatformContract, _deserialize_platform_contract, _serialize_platform_contract
from portone_server_sdk._generated.platform.platform_order_settlement_amount import PlatformOrderSettlementAmount, _deserialize_platform_order_settlement_amount, _serialize_platform_order_settlement_amount
from portone_server_sdk._generated.platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner
from portone_server_sdk._generated.platform.partner_settlement.platform_partner_settlement_status import PlatformPartnerSettlementStatus, _deserialize_platform_partner_settlement_status, _serialize_platform_partner_settlement_status

@dataclass
class PlatformPartnerOrderCancelSettlement:
    type: Literal["ORDER_CANCEL"] = field(repr=False)
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
    contract: PlatformContract
    """계약
    """
    settlement_start_date_range: DateRange
    """정산 시작 일 범위
    """
    amount: PlatformOrderSettlementAmount
    """금액 정보
    """
    is_for_test: bool
    """테스트 모드 여부
    """
    memo: Optional[str]
    """메모
    """


def _serialize_platform_partner_order_cancel_settlement(obj: PlatformPartnerOrderCancelSettlement) -> Any:
    entity = {}
    entity["type"] = "ORDER_CANCEL"
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["partner"] = _serialize_platform_partner(obj.partner)
    entity["settlementDate"] = obj.settlement_date
    entity["settlementCurrency"] = _serialize_currency(obj.settlement_currency)
    entity["status"] = _serialize_platform_partner_settlement_status(obj.status)
    entity["contract"] = _serialize_platform_contract(obj.contract)
    entity["settlementStartDateRange"] = _serialize_date_range(obj.settlement_start_date_range)
    entity["amount"] = _serialize_platform_order_settlement_amount(obj.amount)
    entity["isForTest"] = obj.is_for_test
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_platform_partner_order_cancel_settlement(obj: Any) -> PlatformPartnerOrderCancelSettlement:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "ORDER_CANCEL":
        raise ValueError(f"{repr(type)} is not 'ORDER_CANCEL'")
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
    if "contract" not in obj:
        raise KeyError(f"'contract' is not in {obj}")
    contract = obj["contract"]
    contract = _deserialize_platform_contract(contract)
    if "settlementStartDateRange" not in obj:
        raise KeyError(f"'settlementStartDateRange' is not in {obj}")
    settlement_start_date_range = obj["settlementStartDateRange"]
    settlement_start_date_range = _deserialize_date_range(settlement_start_date_range)
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    amount = _deserialize_platform_order_settlement_amount(amount)
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
    return PlatformPartnerOrderCancelSettlement(type, id, graphql_id, partner, settlement_date, settlement_currency, status, contract, settlement_start_date_range, amount, is_for_test, memo)
