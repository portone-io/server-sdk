from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info
from ...platform.bulk_account_transfer.platform_bulk_account_transfer import PlatformBulkAccountTransfer, _deserialize_platform_bulk_account_transfer, _serialize_platform_bulk_account_transfer
from ...platform.bulk_account_transfer.platform_bulk_account_transfer_status_stats import PlatformBulkAccountTransferStatusStats, _deserialize_platform_bulk_account_transfer_status_stats, _serialize_platform_bulk_account_transfer_status_stats

@dataclass
class GetPlatformBulkAccountTransfersResponse:
    items: list[PlatformBulkAccountTransfer]
    page: PageInfo
    counts: PlatformBulkAccountTransferStatusStats


def _serialize_get_platform_bulk_account_transfers_response(obj: GetPlatformBulkAccountTransfersResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["items"] = list(map(_serialize_platform_bulk_account_transfer, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
    entity["counts"] = _serialize_platform_bulk_account_transfer_status_stats(obj.counts)
    return entity


def _deserialize_get_platform_bulk_account_transfers_response(obj: Any) -> GetPlatformBulkAccountTransfersResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "items" not in obj:
        raise KeyError("Missing required field 'items'")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError("Expected list for items")
    for i, item in enumerate(items):
        item = _deserialize_platform_bulk_account_transfer(item)
        items[i] = item
    if "page" not in obj:
        raise KeyError("Missing required field 'page'")
    page = obj["page"]
    page = _deserialize_page_info(page)
    if "counts" not in obj:
        raise KeyError("Missing required field 'counts'")
    counts = obj["counts"]
    counts = _deserialize_platform_bulk_account_transfer_status_stats(counts)
    return GetPlatformBulkAccountTransfersResponse(items, page, counts)
