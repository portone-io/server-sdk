from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.billing_key.billing_key_info import BillingKeyInfo, _deserialize_billing_key_info, _serialize_billing_key_info
from portone_server_sdk._generated.common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info

@dataclass
class GetBillingKeyInfosResponse:
    """빌링키 다건 조회 성공 응답 정보
    """
    items: list[BillingKeyInfo]
    """조회된 빌링키 리스트
    """
    page: PageInfo
    """조회된 페이지 정보
    """


def _serialize_get_billing_key_infos_response(obj: GetBillingKeyInfosResponse) -> Any:
    entity = {}
    entity["items"] = list(map(_serialize_billing_key_info, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
    return entity


def _deserialize_get_billing_key_infos_response(obj: Any) -> GetBillingKeyInfosResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_billing_key_info(item)
        items[i] = item
    if "page" not in obj:
        raise KeyError(f"'page' is not in {obj}")
    page = obj["page"]
    page = _deserialize_page_info(page)
    return GetBillingKeyInfosResponse(items, page)
