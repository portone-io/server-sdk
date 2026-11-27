from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class DeletePlatformPartnerSettlementsBody:
    partner_settlement_ids: list[str]
    is_for_test: Optional[bool] = field(default=None)
    """Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
    Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
    """


def _serialize_delete_platform_partner_settlements_body(obj: DeletePlatformPartnerSettlementsBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["partnerSettlementIds"] = obj.partner_settlement_ids
    if obj.is_for_test is not None:
        entity["isForTest"] = obj.is_for_test
    return entity


def _deserialize_delete_platform_partner_settlements_body(obj: Any) -> DeletePlatformPartnerSettlementsBody:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "partnerSettlementIds" not in obj:
        raise KeyError("Missing required field 'partnerSettlementIds'")
    partner_settlement_ids = obj["partnerSettlementIds"]
    if not isinstance(partner_settlement_ids, list):
        raise ValueError("Expected list for partner_settlement_ids")
    for i, item in enumerate(partner_settlement_ids):
        if not isinstance(item, str):
            raise ValueError("Expected str for item")
    if "isForTest" in obj:
        is_for_test = obj["isForTest"]
        if not isinstance(is_for_test, bool):
            raise ValueError("Expected bool for is_for_test")
    else:
        is_for_test = None
    return DeletePlatformPartnerSettlementsBody(partner_settlement_ids, is_for_test)
