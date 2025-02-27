from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.cash_receipt.cash_receipt_filter_input import CashReceiptFilterInput, _deserialize_cash_receipt_filter_input, _serialize_cash_receipt_filter_input
from ...payment.cash_receipt.cash_receipt_sort_input import CashReceiptSortInput, _deserialize_cash_receipt_sort_input, _serialize_cash_receipt_sort_input
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input

@dataclass
class GetCashReceiptsBody:
    """현금영수증 다건 조회를 위한 입력 정보
    """
    page: Optional[PageInput] = field(default=None)
    """요청할 페이지 정보

    미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
    """
    sort: Optional[CashReceiptSortInput] = field(default=None)
    """정렬 조건

    미 입력 시 sortBy: ISSUED_AT, sortOrder: DESC 으로 기본값이 적용됩니다.
    """
    filter: Optional[CashReceiptFilterInput] = field(default=None)
    """조회할 현금영수증 조건 필터
    """


def _serialize_get_cash_receipts_body(obj: GetCashReceiptsBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    if obj.sort is not None:
        entity["sort"] = _serialize_cash_receipt_sort_input(obj.sort)
    if obj.filter is not None:
        entity["filter"] = _serialize_cash_receipt_filter_input(obj.filter)
    return entity


def _deserialize_get_cash_receipts_body(obj: Any) -> GetCashReceiptsBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "page" in obj:
        page = obj["page"]
        page = _deserialize_page_input(page)
    else:
        page = None
    if "sort" in obj:
        sort = obj["sort"]
        sort = _deserialize_cash_receipt_sort_input(sort)
    else:
        sort = None
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_cash_receipt_filter_input(filter)
    else:
        filter = None
    return GetCashReceiptsBody(page, sort, filter)
