from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPartnerSettlementFilterKeywordInput:
    partner_settlement_id: Optional[str] = field(default=None)
    payout_id: Optional[str] = field(default=None)
    bulk_payout_id: Optional[str] = field(default=None)


def _serialize_platform_partner_settlement_filter_keyword_input(obj: PlatformPartnerSettlementFilterKeywordInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.partner_settlement_id is not None:
        entity["partnerSettlementId"] = obj.partner_settlement_id
    if obj.payout_id is not None:
        entity["payoutId"] = obj.payout_id
    if obj.bulk_payout_id is not None:
        entity["bulkPayoutId"] = obj.bulk_payout_id
    return entity


def _deserialize_platform_partner_settlement_filter_keyword_input(obj: Any) -> PlatformPartnerSettlementFilterKeywordInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "partnerSettlementId" in obj:
        partner_settlement_id = obj["partnerSettlementId"]
        if not isinstance(partner_settlement_id, str):
            raise ValueError(f"{repr(partner_settlement_id)} is not str")
    else:
        partner_settlement_id = None
    if "payoutId" in obj:
        payout_id = obj["payoutId"]
        if not isinstance(payout_id, str):
            raise ValueError(f"{repr(payout_id)} is not str")
    else:
        payout_id = None
    if "bulkPayoutId" in obj:
        bulk_payout_id = obj["bulkPayoutId"]
        if not isinstance(bulk_payout_id, str):
            raise ValueError(f"{repr(bulk_payout_id)} is not str")
    else:
        bulk_payout_id = None
    return PlatformPartnerSettlementFilterKeywordInput(partner_settlement_id, payout_id, bulk_payout_id)
