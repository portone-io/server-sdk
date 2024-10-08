from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info
from portone_server_sdk._generated.platform.payout.platform_payout import PlatformPayout, _deserialize_platform_payout, _serialize_platform_payout
from portone_server_sdk._generated.platform.platform_payout_status_stats import PlatformPayoutStatusStats, _deserialize_platform_payout_status_stats, _serialize_platform_payout_status_stats

@dataclass
class GetPlatformPayoutsResponse:
    items: list[PlatformPayout]
    page: PageInfo
    counts: PlatformPayoutStatusStats


def _serialize_get_platform_payouts_response(obj: GetPlatformPayoutsResponse) -> Any:
    entity = {}
    entity["items"] = list(map(_serialize_platform_payout, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
    entity["counts"] = _serialize_platform_payout_status_stats(obj.counts)
    return entity


def _deserialize_get_platform_payouts_response(obj: Any) -> GetPlatformPayoutsResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_platform_payout(item)
        items[i] = item
    if "page" not in obj:
        raise KeyError(f"'page' is not in {obj}")
    page = obj["page"]
    page = _deserialize_page_info(page)
    if "counts" not in obj:
        raise KeyError(f"'counts' is not in {obj}")
    counts = obj["counts"]
    counts = _deserialize_platform_payout_status_stats(counts)
    return GetPlatformPayoutsResponse(items, page, counts)
