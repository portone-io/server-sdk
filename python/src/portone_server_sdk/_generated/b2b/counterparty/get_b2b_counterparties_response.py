from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.counterparty.b2b_counterparty import B2bCounterparty, _deserialize_b2b_counterparty, _serialize_b2b_counterparty
from ...common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info

@dataclass
class GetB2bCounterpartiesResponse:
    """거래처 검색 성공 응답
    """
    page: PageInfo
    """페이지 정보
    """
    items: list[B2bCounterparty]
    """거래처 목록
    """


def _serialize_get_b2b_counterparties_response(obj: GetB2bCounterpartiesResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["page"] = _serialize_page_info(obj.page)
    entity["items"] = list(map(_serialize_b2b_counterparty, obj.items))
    return entity


def _deserialize_get_b2b_counterparties_response(obj: Any) -> GetB2bCounterpartiesResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "page" not in obj:
        raise KeyError(f"'page' is not in {obj}")
    page = obj["page"]
    page = _deserialize_page_info(page)
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_b2b_counterparty(item)
        items[i] = item
    return GetB2bCounterpartiesResponse(page, items)
