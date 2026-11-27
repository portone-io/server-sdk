from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner
from ...platform.transfer.platform_transfer_status import PlatformTransferStatus, _deserialize_platform_transfer_status, _serialize_platform_transfer_status
from ...platform.transfer.platform_user_defined_property_key_value import PlatformUserDefinedPropertyKeyValue, _deserialize_platform_user_defined_property_key_value, _serialize_platform_user_defined_property_key_value

@dataclass
class PlatformManualTransfer:
    """수기 정산건
    """
    id: str
    """정산건 아이디
    """
    graphql_id: str
    partner: PlatformPartner
    """파트너
    """
    status: PlatformTransferStatus
    """정산 상태
    """
    settlement_date: str
    """정산 일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    (yyyy-MM-dd)
    """
    settlement_currency: Currency
    """정산 통화
    """
    is_for_test: bool
    """테스트 모드 여부
    """
    user_defined_properties: list[PlatformUserDefinedPropertyKeyValue]
    """사용자 정의 속성
    """
    settlement_amount: int
    """정산 금액
    (int64)
    """
    settlement_tax_free_amount: int
    """정산 면세 금액
    (int64)
    """
    memo: Optional[str] = field(default=None)
    """메모
    """
    payout_id: Optional[str] = field(default=None)
    """더 이상 사용되지 않는 값입니다.
    """
    payout_graphql_id: Optional[str] = field(default=None)


def _serialize_platform_manual_transfer(obj: PlatformManualTransfer) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "MANUAL"
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["partner"] = _serialize_platform_partner(obj.partner)
    entity["status"] = _serialize_platform_transfer_status(obj.status)
    entity["settlementDate"] = obj.settlement_date
    entity["settlementCurrency"] = _serialize_currency(obj.settlement_currency)
    entity["isForTest"] = obj.is_for_test
    entity["userDefinedProperties"] = list(map(_serialize_platform_user_defined_property_key_value, obj.user_defined_properties))
    entity["settlementAmount"] = obj.settlement_amount
    entity["settlementTaxFreeAmount"] = obj.settlement_tax_free_amount
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.payout_id is not None:
        entity["payoutId"] = obj.payout_id
    if obj.payout_graphql_id is not None:
        entity["payoutGraphqlId"] = obj.payout_graphql_id
    return entity


def _deserialize_platform_manual_transfer(obj: Any) -> PlatformManualTransfer:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "MANUAL":
        raise ValueError("Expected 'MANUAL' for type")
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
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    status = _deserialize_platform_transfer_status(status)
    if "settlementDate" not in obj:
        raise KeyError("Missing required field 'settlementDate'")
    settlement_date = obj["settlementDate"]
    if not isinstance(settlement_date, str):
        raise ValueError("Expected str for settlement_date")
    if "settlementCurrency" not in obj:
        raise KeyError("Missing required field 'settlementCurrency'")
    settlement_currency = obj["settlementCurrency"]
    settlement_currency = _deserialize_currency(settlement_currency)
    if "isForTest" not in obj:
        raise KeyError("Missing required field 'isForTest'")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError("Expected bool for is_for_test")
    if "userDefinedProperties" not in obj:
        raise KeyError("Missing required field 'userDefinedProperties'")
    user_defined_properties = obj["userDefinedProperties"]
    if not isinstance(user_defined_properties, list):
        raise ValueError("Expected list for user_defined_properties")
    for i, item in enumerate(user_defined_properties):
        item = _deserialize_platform_user_defined_property_key_value(item)
        user_defined_properties[i] = item
    if "settlementAmount" not in obj:
        raise KeyError("Missing required field 'settlementAmount'")
    settlement_amount = obj["settlementAmount"]
    if not isinstance(settlement_amount, int):
        raise ValueError("Expected int for settlement_amount")
    if "settlementTaxFreeAmount" not in obj:
        raise KeyError("Missing required field 'settlementTaxFreeAmount'")
    settlement_tax_free_amount = obj["settlementTaxFreeAmount"]
    if not isinstance(settlement_tax_free_amount, int):
        raise ValueError("Expected int for settlement_tax_free_amount")
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError("Expected str for memo")
    else:
        memo = None
    if "payoutId" in obj:
        payout_id = obj["payoutId"]
        if not isinstance(payout_id, str):
            raise ValueError("Expected str for payout_id")
    else:
        payout_id = None
    if "payoutGraphqlId" in obj:
        payout_graphql_id = obj["payoutGraphqlId"]
        if not isinstance(payout_graphql_id, str):
            raise ValueError("Expected str for payout_graphql_id")
    else:
        payout_graphql_id = None
    return PlatformManualTransfer(id, graphql_id, partner, status, settlement_date, settlement_currency, is_for_test, user_defined_properties, settlement_amount, settlement_tax_free_amount, memo, payout_id, payout_graphql_id)
