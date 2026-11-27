from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...common.date_range import DateRange, _deserialize_date_range, _serialize_date_range
from ...platform.platform_contract import PlatformContract, _deserialize_platform_contract, _serialize_platform_contract
from ...platform.platform_order_settlement_amount import PlatformOrderSettlementAmount, _deserialize_platform_order_settlement_amount, _serialize_platform_order_settlement_amount
from ...platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner
from ...platform.partner_settlement.platform_partner_settlement_status import PlatformPartnerSettlementStatus, _deserialize_platform_partner_settlement_status, _serialize_platform_partner_settlement_status

@dataclass
class PlatformPartnerOrderCancelSettlement:
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
    (yyyy-MM-dd)
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
    status_updated_at: Optional[str] = field(default=None)
    """상태 업데이트 일시
    (RFC 3339 date-time)
    """
    memo: Optional[str] = field(default=None)
    """메모
    """


def _serialize_platform_partner_order_cancel_settlement(obj: PlatformPartnerOrderCancelSettlement) -> Any:
    if isinstance(obj, dict):
        return obj
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
    if obj.status_updated_at is not None:
        entity["statusUpdatedAt"] = obj.status_updated_at
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_platform_partner_order_cancel_settlement(obj: Any) -> PlatformPartnerOrderCancelSettlement:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "ORDER_CANCEL":
        raise ValueError("Expected 'ORDER_CANCEL' for type")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "graphqlId" not in obj:
        raise KeyError("Missing required field 'graphqlId'")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError("Expected str for graphql_id")
    if "partner" not in obj:
        raise KeyError("Missing required field 'partner'")
    partner = obj["partner"]
    partner = _deserialize_platform_partner(partner)
    if "settlementDate" not in obj:
        raise KeyError("Missing required field 'settlementDate'")
    settlement_date = obj["settlementDate"]
    if not isinstance(settlement_date, str):
        raise ValueError("Expected str for settlement_date")
    if "settlementCurrency" not in obj:
        raise KeyError("Missing required field 'settlementCurrency'")
    settlement_currency = obj["settlementCurrency"]
    settlement_currency = _deserialize_currency(settlement_currency)
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    status = _deserialize_platform_partner_settlement_status(status)
    if "contract" not in obj:
        raise KeyError("Missing required field 'contract'")
    contract = obj["contract"]
    contract = _deserialize_platform_contract(contract)
    if "settlementStartDateRange" not in obj:
        raise KeyError("Missing required field 'settlementStartDateRange'")
    settlement_start_date_range = obj["settlementStartDateRange"]
    settlement_start_date_range = _deserialize_date_range(settlement_start_date_range)
    if "amount" not in obj:
        raise KeyError("Missing required field 'amount'")
    amount = obj["amount"]
    amount = _deserialize_platform_order_settlement_amount(amount)
    if "isForTest" not in obj:
        raise KeyError("Missing required field 'isForTest'")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError("Expected bool for is_for_test")
    if "statusUpdatedAt" in obj:
        status_updated_at = obj["statusUpdatedAt"]
        if not isinstance(status_updated_at, str):
            raise ValueError("Expected str for status_updated_at")
    else:
        status_updated_at = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError("Expected str for memo")
    else:
        memo = None
    return PlatformPartnerOrderCancelSettlement(id, graphql_id, partner, settlement_date, settlement_currency, status, contract, settlement_start_date_range, amount, is_for_test, status_updated_at, memo)
