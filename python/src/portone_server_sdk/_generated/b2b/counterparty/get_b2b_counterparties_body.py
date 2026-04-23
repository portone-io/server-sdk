from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.counterparty.b2b_counterparty_filter import B2bCounterpartyFilter, _deserialize_b2b_counterparty_filter, _serialize_b2b_counterparty_filter
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input

@dataclass
class GetB2bCounterpartiesBody:
    """거래처 검색 요청 정보
    """
    page: Optional[PageInput] = field(default=None)
    """페이지 정보
    """
    filter: Optional[B2bCounterpartyFilter] = field(default=None)
    """검색 필터
    """


def _serialize_get_b2b_counterparties_body(obj: GetB2bCounterpartiesBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    if obj.filter is not None:
        entity["filter"] = _serialize_b2b_counterparty_filter(obj.filter)
    return entity


def _deserialize_get_b2b_counterparties_body(obj: Any) -> GetB2bCounterpartiesBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "page" in obj:
        page = obj["page"]
        page = _deserialize_page_input(page)
    else:
        page = None
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_b2b_counterparty_filter(filter)
    else:
        filter = None
    return GetB2bCounterpartiesBody(page, filter)
