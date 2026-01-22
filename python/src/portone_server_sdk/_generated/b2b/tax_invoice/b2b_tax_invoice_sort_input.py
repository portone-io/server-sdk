from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_sort_by import B2bTaxInvoiceSortBy, _deserialize_b2b_tax_invoice_sort_by, _serialize_b2b_tax_invoice_sort_by
from ...common.sort_order import SortOrder, _deserialize_sort_order, _serialize_sort_order

@dataclass
class B2bTaxInvoiceSortInput:
    """세금계산서 다건 조회 시 정렬 조건
    """
    by: Optional[B2bTaxInvoiceSortBy] = field(default=None)
    """정렬 기준
    """
    order: Optional[SortOrder] = field(default=None)
    """정렬 방식
    """


def _serialize_b2b_tax_invoice_sort_input(obj: B2bTaxInvoiceSortInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.by is not None:
        entity["by"] = _serialize_b2b_tax_invoice_sort_by(obj.by)
    if obj.order is not None:
        entity["order"] = _serialize_sort_order(obj.order)
    return entity


def _deserialize_b2b_tax_invoice_sort_input(obj: Any) -> B2bTaxInvoiceSortInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "by" in obj:
        by = obj["by"]
        by = _deserialize_b2b_tax_invoice_sort_by(by)
    else:
        by = None
    if "order" in obj:
        order = obj["order"]
        order = _deserialize_sort_order(order)
    else:
        order = None
    return B2bTaxInvoiceSortInput(by, order)
