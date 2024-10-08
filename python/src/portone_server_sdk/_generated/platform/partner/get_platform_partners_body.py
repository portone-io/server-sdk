from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from portone_server_sdk._generated.platform.platform_partner_filter_input import PlatformPartnerFilterInput, _deserialize_platform_partner_filter_input, _serialize_platform_partner_filter_input

@dataclass
class GetPlatformPartnersBody:
    """파트너 다건 조회를 위한 입력 정보
    """
    page: Optional[PageInput]
    """요청할 페이지 정보
    """
    filter: Optional[PlatformPartnerFilterInput]
    """조회할 파트너 조건 필터
    """


def _serialize_get_platform_partners_body(obj: GetPlatformPartnersBody) -> Any:
    entity = {}
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    if obj.filter is not None:
        entity["filter"] = _serialize_platform_partner_filter_input(obj.filter)
    return entity


def _deserialize_get_platform_partners_body(obj: Any) -> GetPlatformPartnersBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "page" in obj:
        page = obj["page"]
        page = _deserialize_page_input(page)
    else:
        page = None
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_platform_partner_filter_input(filter)
    else:
        filter = None
    return GetPlatformPartnersBody(page, filter)
