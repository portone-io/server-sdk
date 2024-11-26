from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info
from ...platform.platform_contract import PlatformContract, _deserialize_platform_contract, _serialize_platform_contract

@dataclass
class GetPlatformContractsResponse:
    """계약 다건 조회 성공 응답
    """
    items: list[PlatformContract]
    """조회된 계약 리스트
    """
    page: PageInfo
    """조회된 페이지 정보
    """


def _serialize_get_platform_contracts_response(obj: GetPlatformContractsResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["items"] = list(map(_serialize_platform_contract, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
    return entity


def _deserialize_get_platform_contracts_response(obj: Any) -> GetPlatformContractsResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_platform_contract(item)
        items[i] = item
    if "page" not in obj:
        raise KeyError(f"'page' is not in {obj}")
    page = obj["page"]
    page = _deserialize_page_info(page)
    return GetPlatformContractsResponse(items, page)
