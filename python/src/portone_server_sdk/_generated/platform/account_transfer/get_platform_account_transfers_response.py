from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info
from ...platform.account_transfer.platform_account_transfer import PlatformAccountTransfer, _deserialize_platform_account_transfer, _serialize_platform_account_transfer
from ...platform.platform_account_transfer_status_stats import PlatformAccountTransferStatusStats, _deserialize_platform_account_transfer_status_stats, _serialize_platform_account_transfer_status_stats

@dataclass
class GetPlatformAccountTransfersResponse:
    """이체내역 다건 조회 성공 응답 정보
    """
    items: list[PlatformAccountTransfer]
    """조회된 이체내역 리스트
    """
    page: PageInfo
    """조회된 페이지 정보
    """
    counts: PlatformAccountTransferStatusStats
    """이체 내역 상태별 건 수
    """


def _serialize_get_platform_account_transfers_response(obj: GetPlatformAccountTransfersResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["items"] = list(map(_serialize_platform_account_transfer, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
    entity["counts"] = _serialize_platform_account_transfer_status_stats(obj.counts)
    return entity


def _deserialize_get_platform_account_transfers_response(obj: Any) -> GetPlatformAccountTransfersResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_platform_account_transfer(item)
        items[i] = item
    if "page" not in obj:
        raise KeyError(f"'page' is not in {obj}")
    page = obj["page"]
    page = _deserialize_page_info(page)
    if "counts" not in obj:
        raise KeyError(f"'counts' is not in {obj}")
    counts = obj["counts"]
    counts = _deserialize_platform_account_transfer_status_stats(counts)
    return GetPlatformAccountTransfersResponse(items, page, counts)
