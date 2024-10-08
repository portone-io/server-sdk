from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from portone_server_sdk._generated.platform.partner_settlement.platform_partner_settlement_filter_input import PlatformPartnerSettlementFilterInput, _deserialize_platform_partner_settlement_filter_input, _serialize_platform_partner_settlement_filter_input

@dataclass
class GetPlatformPartnerSettlementsBody:
    """정산내역 다건 조회를 위한 입력 정보
    """
    filter: PlatformPartnerSettlementFilterInput
    """조회할 정산내역 조건 필터
    """
    is_for_test: bool
    page: Optional[PageInput]
    """요청할 페이지 정보
    """


def _serialize_get_platform_partner_settlements_body(obj: GetPlatformPartnerSettlementsBody) -> Any:
    entity = {}
    entity["filter"] = _serialize_platform_partner_settlement_filter_input(obj.filter)
    entity["isForTest"] = obj.is_for_test
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    return entity


def _deserialize_get_platform_partner_settlements_body(obj: Any) -> GetPlatformPartnerSettlementsBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "filter" not in obj:
        raise KeyError(f"'filter' is not in {obj}")
    filter = obj["filter"]
    filter = _deserialize_platform_partner_settlement_filter_input(filter)
    if "isForTest" not in obj:
        raise KeyError(f"'isForTest' is not in {obj}")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError(f"{repr(is_for_test)} is not bool")
    if "page" in obj:
        page = obj["page"]
        page = _deserialize_page_input(page)
    else:
        page = None
    return GetPlatformPartnerSettlementsBody(filter, is_for_test, page)
