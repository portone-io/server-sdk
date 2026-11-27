from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CompletePlatformPayoutByPartnerSettlementIdsBody:
    bulk_payout_id: str
    partner_settlement_ids: list[str]
    name: Optional[str] = field(default=None)
    completed_at: Optional[str] = field(default=None)
    """날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    (yyyy-MM-dd)
    """
    is_for_test: Optional[bool] = field(default=None)
    """Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
    Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
    """


def _serialize_complete_platform_payout_by_partner_settlement_ids_body(obj: CompletePlatformPayoutByPartnerSettlementIdsBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["bulkPayoutId"] = obj.bulk_payout_id
    entity["partnerSettlementIds"] = obj.partner_settlement_ids
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.completed_at is not None:
        entity["completedAt"] = obj.completed_at
    if obj.is_for_test is not None:
        entity["isForTest"] = obj.is_for_test
    return entity


def _deserialize_complete_platform_payout_by_partner_settlement_ids_body(obj: Any) -> CompletePlatformPayoutByPartnerSettlementIdsBody:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "bulkPayoutId" not in obj:
        raise KeyError("Missing required field 'bulkPayoutId'")
    bulk_payout_id = obj["bulkPayoutId"]
    if not isinstance(bulk_payout_id, str):
        raise ValueError("Expected str for bulk_payout_id")
    if "partnerSettlementIds" not in obj:
        raise KeyError("Missing required field 'partnerSettlementIds'")
    partner_settlement_ids = obj["partnerSettlementIds"]
    if not isinstance(partner_settlement_ids, list):
        raise ValueError("Expected list for partner_settlement_ids")
    for i, item in enumerate(partner_settlement_ids):
        if not isinstance(item, str):
            raise ValueError("Expected str for item")
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError("Expected str for name")
    else:
        name = None
    if "completedAt" in obj:
        completed_at = obj["completedAt"]
        if not isinstance(completed_at, str):
            raise ValueError("Expected str for completed_at")
    else:
        completed_at = None
    if "isForTest" in obj:
        is_for_test = obj["isForTest"]
        if not isinstance(is_for_test, bool):
            raise ValueError("Expected bool for is_for_test")
    else:
        is_for_test = None
    return CompletePlatformPayoutByPartnerSettlementIdsBody(bulk_payout_id, partner_settlement_ids, name, completed_at, is_for_test)
