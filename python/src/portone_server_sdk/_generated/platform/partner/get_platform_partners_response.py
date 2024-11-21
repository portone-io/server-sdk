from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info
from ...platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner

@dataclass
class GetPlatformPartnersResponse:
    """파트너 다건 조회 성공 응답 정보
    """
    items: list[PlatformPartner]
    """조회된 파트너 리스트
    """
    page: PageInfo
    """조회된 페이지 정보
    """


def _serialize_get_platform_partners_response(obj: GetPlatformPartnersResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["items"] = list(map(_serialize_platform_partner, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
    return entity


def _deserialize_get_platform_partners_response(obj: Any) -> GetPlatformPartnersResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_platform_partner(item)
        items[i] = item
    if "page" not in obj:
        raise KeyError(f"'page' is not in {obj}")
    page = obj["page"]
    page = _deserialize_page_info(page)
    return GetPlatformPartnersResponse(items, page)
