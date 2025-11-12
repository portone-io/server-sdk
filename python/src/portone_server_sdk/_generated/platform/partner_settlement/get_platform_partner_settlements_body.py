from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...platform.partner_settlement.platform_partner_settlement_filter_input import PlatformPartnerSettlementFilterInput, _deserialize_platform_partner_settlement_filter_input, _serialize_platform_partner_settlement_filter_input

@dataclass
class GetPlatformPartnerSettlementsBody:
    """정산내역 다건 조회를 위한 입력 정보
    """
    filter: PlatformPartnerSettlementFilterInput
    """조회할 정산내역 조건 필터
    """
    page: Optional[PageInput] = field(default=None)
    """요청할 페이지 정보
    """
    is_for_test: Optional[bool] = field(default=None)
    """테스트 모드 여부

    Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
    Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
    """


def _serialize_get_platform_partner_settlements_body(obj: GetPlatformPartnerSettlementsBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["filter"] = _serialize_platform_partner_settlement_filter_input(obj.filter)
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    if obj.is_for_test is not None:
        entity["isForTest"] = obj.is_for_test
    return entity


def _deserialize_get_platform_partner_settlements_body(obj: Any) -> GetPlatformPartnerSettlementsBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "filter" not in obj:
        raise KeyError(f"'filter' is not in {obj}")
    filter = obj["filter"]
    filter = _deserialize_platform_partner_settlement_filter_input(filter)
    if "page" in obj:
        page = obj["page"]
        page = _deserialize_page_input(page)
    else:
        page = None
    if "isForTest" in obj:
        is_for_test = obj["isForTest"]
        if not isinstance(is_for_test, bool):
            raise ValueError(f"{repr(is_for_test)} is not bool")
    else:
        is_for_test = None
    return GetPlatformPartnerSettlementsBody(filter, page, is_for_test)
