from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...platform.transfer.platform_transfer_status import PlatformTransferStatus, _deserialize_platform_transfer_status, _serialize_platform_transfer_status
from ...platform.transfer.platform_transfer_summary_partner import PlatformTransferSummaryPartner, _deserialize_platform_transfer_summary_partner, _serialize_platform_transfer_summary_partner
from ...platform.transfer.platform_user_defined_property_key_value import PlatformUserDefinedPropertyKeyValue, _deserialize_platform_user_defined_property_key_value, _serialize_platform_user_defined_property_key_value

@dataclass
class PlatformManualTransferSummary:
    id: str
    graphql_id: str
    partner: PlatformTransferSummaryPartner
    status: PlatformTransferStatus
    settlement_date: str
    """날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    settlement_currency: Currency
    is_for_test: bool
    partner_user_defined_properties: list[PlatformUserDefinedPropertyKeyValue]
    """사용자 정의 속성
    """
    user_defined_properties: list[PlatformUserDefinedPropertyKeyValue]
    """사용자 정의 속성
    """
    settlement_amount: int
    """(int64)
    """
    memo: Optional[str] = field(default=None)


def _serialize_platform_manual_transfer_summary(obj: PlatformManualTransferSummary) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "MANUAL"
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["partner"] = _serialize_platform_transfer_summary_partner(obj.partner)
    entity["status"] = _serialize_platform_transfer_status(obj.status)
    entity["settlementDate"] = obj.settlement_date
    entity["settlementCurrency"] = _serialize_currency(obj.settlement_currency)
    entity["isForTest"] = obj.is_for_test
    entity["partnerUserDefinedProperties"] = list(map(_serialize_platform_user_defined_property_key_value, obj.partner_user_defined_properties))
    entity["userDefinedProperties"] = list(map(_serialize_platform_user_defined_property_key_value, obj.user_defined_properties))
    entity["settlementAmount"] = obj.settlement_amount
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_platform_manual_transfer_summary(obj: Any) -> PlatformManualTransferSummary:
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
    partner = _deserialize_platform_transfer_summary_partner(partner)
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_platform_transfer_status(status)
    if "settlementDate" not in obj:
        raise KeyError(f"'settlementDate' is not in {obj}")
    settlement_date = obj["settlementDate"]
    if not isinstance(settlement_date, str):
        raise ValueError(f"{repr(settlement_date)} is not str")
    if "settlementCurrency" not in obj:
        raise KeyError(f"'settlementCurrency' is not in {obj}")
    settlement_currency = obj["settlementCurrency"]
    settlement_currency = _deserialize_currency(settlement_currency)
    if "isForTest" not in obj:
        raise KeyError(f"'isForTest' is not in {obj}")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError(f"{repr(is_for_test)} is not bool")
    if "partnerUserDefinedProperties" not in obj:
        raise KeyError(f"'partnerUserDefinedProperties' is not in {obj}")
    partner_user_defined_properties = obj["partnerUserDefinedProperties"]
    if not isinstance(partner_user_defined_properties, list):
        raise ValueError(f"{repr(partner_user_defined_properties)} is not list")
    for i, item in enumerate(partner_user_defined_properties):
        item = _deserialize_platform_user_defined_property_key_value(item)
        partner_user_defined_properties[i] = item
    if "userDefinedProperties" not in obj:
        raise KeyError(f"'userDefinedProperties' is not in {obj}")
    user_defined_properties = obj["userDefinedProperties"]
    if not isinstance(user_defined_properties, list):
        raise ValueError(f"{repr(user_defined_properties)} is not list")
    for i, item in enumerate(user_defined_properties):
        item = _deserialize_platform_user_defined_property_key_value(item)
        user_defined_properties[i] = item
    if "settlementAmount" not in obj:
        raise KeyError(f"'settlementAmount' is not in {obj}")
    settlement_amount = obj["settlementAmount"]
    if not isinstance(settlement_amount, int):
        raise ValueError(f"{repr(settlement_amount)} is not int")
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return PlatformManualTransferSummary(id, graphql_id, partner, status, settlement_date, settlement_currency, is_for_test, partner_user_defined_properties, user_defined_properties, settlement_amount, memo)
