from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info
from portone_server_sdk._generated.platform.account_transfer.platform_account_transfer import PlatformAccountTransfer, _deserialize_platform_account_transfer, _serialize_platform_account_transfer

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


def _serialize_get_platform_account_transfers_response(obj: GetPlatformAccountTransfersResponse) -> Any:
    entity = {}
    entity["items"] = list(map(_serialize_platform_account_transfer, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
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
    return GetPlatformAccountTransfersResponse(items, page)
