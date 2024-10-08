from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.transfer.platform_user_defined_property_key_value import PlatformUserDefinedPropertyKeyValue, _deserialize_platform_user_defined_property_key_value, _serialize_platform_user_defined_property_key_value

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
    """
    memo: Optional[str]
    """메모
    """
    is_for_test: Optional[bool]
    """테스트 모드 여부

    기본값은 false 입니다.
    """
    user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]]
    """사용자 정의 속성
    """


def _serialize_create_platform_manual_transfer_body(obj: CreatePlatformManualTransferBody) -> Any:
    entity = {}
    entity["partnerId"] = obj.partner_id
    entity["settlementAmount"] = obj.settlement_amount
    entity["settlementDate"] = obj.settlement_date
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.is_for_test is not None:
        entity["isForTest"] = obj.is_for_test
    if obj.user_defined_properties is not None:
        entity["userDefinedProperties"] = list(map(_serialize_platform_user_defined_property_key_value, obj.user_defined_properties))
    return entity


def _deserialize_create_platform_manual_transfer_body(obj: Any) -> CreatePlatformManualTransferBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "partnerId" not in obj:
        raise KeyError(f"'partnerId' is not in {obj}")
    partner_id = obj["partnerId"]
    if not isinstance(partner_id, str):
        raise ValueError(f"{repr(partner_id)} is not str")
    if "settlementAmount" not in obj:
        raise KeyError(f"'settlementAmount' is not in {obj}")
    settlement_amount = obj["settlementAmount"]
    if not isinstance(settlement_amount, int):
        raise ValueError(f"{repr(settlement_amount)} is not int")
    if "settlementDate" not in obj:
        raise KeyError(f"'settlementDate' is not in {obj}")
    settlement_date = obj["settlementDate"]
    if not isinstance(settlement_date, str):
        raise ValueError(f"{repr(settlement_date)} is not str")
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    if "isForTest" in obj:
        is_for_test = obj["isForTest"]
        if not isinstance(is_for_test, bool):
            raise ValueError(f"{repr(is_for_test)} is not bool")
    else:
        is_for_test = None
    if "userDefinedProperties" in obj:
        user_defined_properties = obj["userDefinedProperties"]
        if not isinstance(user_defined_properties, list):
            raise ValueError(f"{repr(user_defined_properties)} is not list")
        for i, item in enumerate(user_defined_properties):
            item = _deserialize_platform_user_defined_property_key_value(item)
            user_defined_properties[i] = item
    else:
        user_defined_properties = None
    return CreatePlatformManualTransferBody(partner_id, settlement_amount, settlement_date, memo, is_for_test, user_defined_properties)
