from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info
from portone_server_sdk._generated.platform.bulk_payout.platform_bulk_payout import PlatformBulkPayout, _deserialize_platform_bulk_payout, _serialize_platform_bulk_payout
from portone_server_sdk._generated.platform.bulk_payout.platform_bulk_payout_status_stats import PlatformBulkPayoutStatusStats, _deserialize_platform_bulk_payout_status_stats, _serialize_platform_bulk_payout_status_stats

@dataclass
class GetPlatformBulkPayoutsResponse:
    items: list[PlatformBulkPayout]
    page: PageInfo
    counts: PlatformBulkPayoutStatusStats


def _serialize_get_platform_bulk_payouts_response(obj: GetPlatformBulkPayoutsResponse) -> Any:
    entity = {}
    entity["items"] = list(map(_serialize_platform_bulk_payout, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
    entity["counts"] = _serialize_platform_bulk_payout_status_stats(obj.counts)
    return entity


def _deserialize_get_platform_bulk_payouts_response(obj: Any) -> GetPlatformBulkPayoutsResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_platform_bulk_payout(item)
        items[i] = item
    if "page" not in obj:
        raise KeyError(f"'page' is not in {obj}")
    page = obj["page"]
    page = _deserialize_page_info(page)
    if "counts" not in obj:
        raise KeyError(f"'counts' is not in {obj}")
    counts = obj["counts"]
    counts = _deserialize_platform_bulk_payout_status_stats(counts)
    return GetPlatformBulkPayoutsResponse(items, page, counts)
