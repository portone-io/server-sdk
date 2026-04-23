from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CompletePlatformPayoutByPartnerSettlementIdsResponse:
    """일괄 지급 완료 처리 결과
    """
    payout_count: int
    """(int32)
    """
    partner_settlement_count: int
    """(int32)
    """
    bulk_payout_id: Optional[str] = field(default=None)
    bulk_payout_graphql_id: Optional[str] = field(default=None)


def _serialize_complete_platform_payout_by_partner_settlement_ids_response(obj: CompletePlatformPayoutByPartnerSettlementIdsResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["payoutCount"] = obj.payout_count
    entity["partnerSettlementCount"] = obj.partner_settlement_count
    if obj.bulk_payout_id is not None:
        entity["bulkPayoutId"] = obj.bulk_payout_id
    if obj.bulk_payout_graphql_id is not None:
        entity["bulkPayoutGraphqlId"] = obj.bulk_payout_graphql_id
    return entity


def _deserialize_complete_platform_payout_by_partner_settlement_ids_response(obj: Any) -> CompletePlatformPayoutByPartnerSettlementIdsResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "payoutCount" not in obj:
        raise KeyError(f"'payoutCount' is not in {obj}")
    payout_count = obj["payoutCount"]
    if not isinstance(payout_count, int):
        raise ValueError(f"{repr(payout_count)} is not int")
    if "partnerSettlementCount" not in obj:
        raise KeyError(f"'partnerSettlementCount' is not in {obj}")
    partner_settlement_count = obj["partnerSettlementCount"]
    if not isinstance(partner_settlement_count, int):
        raise ValueError(f"{repr(partner_settlement_count)} is not int")
    if "bulkPayoutId" in obj:
        bulk_payout_id = obj["bulkPayoutId"]
        if not isinstance(bulk_payout_id, str):
            raise ValueError(f"{repr(bulk_payout_id)} is not str")
    else:
        bulk_payout_id = None
    if "bulkPayoutGraphqlId" in obj:
        bulk_payout_graphql_id = obj["bulkPayoutGraphqlId"]
        if not isinstance(bulk_payout_graphql_id, str):
            raise ValueError(f"{repr(bulk_payout_graphql_id)} is not str")
    else:
        bulk_payout_graphql_id = None
    return CompletePlatformPayoutByPartnerSettlementIdsResponse(payout_count, partner_settlement_count, bulk_payout_id, bulk_payout_graphql_id)
