from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_summary import B2bTaxInvoiceSummary, _deserialize_b2b_tax_invoice_summary, _serialize_b2b_tax_invoice_summary
from ...common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info

@dataclass
class GetB2bTaxInvoicesResponse:
    """세금계산서 다건 조회 성공 응답
    """
    items: list[B2bTaxInvoiceSummary]
    """조회된 세금계산서 목록
    """
    page: PageInfo
    """조회된 페이지 정보
    """


def _serialize_get_b2b_tax_invoices_response(obj: GetB2bTaxInvoicesResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["items"] = list(map(_serialize_b2b_tax_invoice_summary, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
    return entity


def _deserialize_get_b2b_tax_invoices_response(obj: Any) -> GetB2bTaxInvoicesResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_b2b_tax_invoice_summary(item)
        items[i] = item
    if "page" not in obj:
        raise KeyError(f"'page' is not in {obj}")
    page = obj["page"]
    page = _deserialize_page_info(page)
    return GetB2bTaxInvoicesResponse(items, page)
