from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...platform.transfer.platform_transfer_filter_input import PlatformTransferFilterInput, _deserialize_platform_transfer_filter_input, _serialize_platform_transfer_filter_input

@dataclass
class GetPlatformTransferSummariesBody:
    """정산건 요약 다건 조회를 위한 입력 정보
    """
    page: Optional[PageInput] = field(default=None)
    """요청할 페이지 정보
    """
    filter: Optional[PlatformTransferFilterInput] = field(default=None)
    """조회할 정산건 조건 필터
    """


def _serialize_get_platform_transfer_summaries_body(obj: GetPlatformTransferSummariesBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    if obj.filter is not None:
        entity["filter"] = _serialize_platform_transfer_filter_input(obj.filter)
    return entity


def _deserialize_get_platform_transfer_summaries_body(obj: Any) -> GetPlatformTransferSummariesBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "page" in obj:
        page = obj["page"]
        page = _deserialize_page_input(page)
    else:
        page = None
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_platform_transfer_filter_input(filter)
    else:
        filter = None
    return GetPlatformTransferSummariesBody(page, filter)
