from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...platform.transfer.platform_user_defined_property_key_value import PlatformUserDefinedPropertyKeyValue, _deserialize_platform_user_defined_property_key_value, _serialize_platform_user_defined_property_key_value

@dataclass
class CreatePlatformManualTransferBody:
    """수기 정산건 생성을 위한 입력 정보
    """
    partner_id: str
    """파트너 아이디
    """
    settlement_amount: int
    """정산 금액
    (int64)
    """
    settlement_date: str
    """정산 일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    (yyyy-MM-dd)
    """
    memo: Optional[str] = field(default=None)
    """메모
    """
    settlement_tax_free_amount: Optional[int] = field(default=None)
    """정산 면세 금액
    (int64)
    """
    is_for_test: Optional[bool] = field(default=None)
    """테스트 모드 여부

    Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
    Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
    """
    user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]] = field(default=None)
    """사용자 정의 속성
    """
    id: Optional[str] = field(default=None)
    """생성할 정산건 아이디

    명시하지 않으면 id 가 임의로 생성됩니다.
    """
    settlement_currency: Optional[Currency] = field(default=None)
    """정산 통화
    """


def _serialize_create_platform_manual_transfer_body(obj: CreatePlatformManualTransferBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["partnerId"] = obj.partner_id
    entity["settlementAmount"] = obj.settlement_amount
    entity["settlementDate"] = obj.settlement_date
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.settlement_tax_free_amount is not None:
        entity["settlementTaxFreeAmount"] = obj.settlement_tax_free_amount
    if obj.is_for_test is not None:
        entity["isForTest"] = obj.is_for_test
    if obj.user_defined_properties is not None:
        entity["userDefinedProperties"] = list(map(_serialize_platform_user_defined_property_key_value, obj.user_defined_properties))
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.settlement_currency is not None:
        entity["settlementCurrency"] = _serialize_currency(obj.settlement_currency)
    return entity


def _deserialize_create_platform_manual_transfer_body(obj: Any) -> CreatePlatformManualTransferBody:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "partnerId" not in obj:
        raise KeyError("Missing required field 'partnerId'")
    partner_id = obj["partnerId"]
    if not isinstance(partner_id, str):
        raise ValueError("Expected str for partner_id")
    if "settlementAmount" not in obj:
        raise KeyError("Missing required field 'settlementAmount'")
    settlement_amount = obj["settlementAmount"]
    if not isinstance(settlement_amount, int):
        raise ValueError("Expected int for settlement_amount")
    if "settlementDate" not in obj:
        raise KeyError("Missing required field 'settlementDate'")
    settlement_date = obj["settlementDate"]
    if not isinstance(settlement_date, str):
        raise ValueError("Expected str for settlement_date")
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError("Expected str for memo")
    else:
        memo = None
    if "settlementTaxFreeAmount" in obj:
        settlement_tax_free_amount = obj["settlementTaxFreeAmount"]
        if not isinstance(settlement_tax_free_amount, int):
            raise ValueError("Expected int for settlement_tax_free_amount")
    else:
        settlement_tax_free_amount = None
    if "isForTest" in obj:
        is_for_test = obj["isForTest"]
        if not isinstance(is_for_test, bool):
            raise ValueError("Expected bool for is_for_test")
    else:
        is_for_test = None
    if "userDefinedProperties" in obj:
        user_defined_properties = obj["userDefinedProperties"]
        if not isinstance(user_defined_properties, list):
            raise ValueError("Expected list for user_defined_properties")
        for i, item in enumerate(user_defined_properties):
            item = _deserialize_platform_user_defined_property_key_value(item)
            user_defined_properties[i] = item
    else:
        user_defined_properties = None
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError("Expected str for id")
    else:
        id = None
    if "settlementCurrency" in obj:
        settlement_currency = obj["settlementCurrency"]
        settlement_currency = _deserialize_currency(settlement_currency)
    else:
        settlement_currency = None
    return CreatePlatformManualTransferBody(partner_id, settlement_amount, settlement_date, memo, settlement_tax_free_amount, is_for_test, user_defined_properties, id, settlement_currency)
