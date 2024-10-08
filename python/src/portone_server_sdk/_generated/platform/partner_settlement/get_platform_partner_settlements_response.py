from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info
from portone_server_sdk._generated.platform.partner_settlement.platform_partner_settlement import PlatformPartnerSettlement, _deserialize_platform_partner_settlement, _serialize_platform_partner_settlement
from portone_server_sdk._generated.platform.partner_settlement.platform_partner_settlement_status_stats import PlatformPartnerSettlementStatusStats, _deserialize_platform_partner_settlement_status_stats, _serialize_platform_partner_settlement_status_stats

@dataclass
class GetPlatformPartnerSettlementsResponse:
    """정산내역 다건 조회 성공 응답 정보
    """
    items: list[PlatformPartnerSettlement]
    """조회된 정산내역 리스트
    """
    page: PageInfo
    """조회된 페이지 정보
    """
    counts: PlatformPartnerSettlementStatusStats
    """정산내역 상태 별 갯수
    """


def _serialize_get_platform_partner_settlements_response(obj: GetPlatformPartnerSettlementsResponse) -> Any:
    entity = {}
    entity["items"] = list(map(_serialize_platform_partner_settlement, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
    entity["counts"] = _serialize_platform_partner_settlement_status_stats(obj.counts)
    return entity


def _deserialize_get_platform_partner_settlements_response(obj: Any) -> GetPlatformPartnerSettlementsResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_platform_partner_settlement(item)
        items[i] = item
    if "page" not in obj:
        raise KeyError(f"'page' is not in {obj}")
    page = obj["page"]
    page = _deserialize_page_info(page)
    if "counts" not in obj:
        raise KeyError(f"'counts' is not in {obj}")
    counts = obj["counts"]
    counts = _deserialize_platform_partner_settlement_status_stats(counts)
    return GetPlatformPartnerSettlementsResponse(items, page, counts)
