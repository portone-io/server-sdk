from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bBulkTaxInvoiceStat:
    """세금계산서 상태별 집계 정보
    """
    count: int
    """(int32)
    """
    amount_sum: int
    """(int64)
    """


def _serialize_b2b_bulk_tax_invoice_stat(obj: B2bBulkTaxInvoiceStat) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["count"] = obj.count
    entity["amountSum"] = obj.amount_sum
    return entity


def _deserialize_b2b_bulk_tax_invoice_stat(obj: Any) -> B2bBulkTaxInvoiceStat:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "count" not in obj:
        raise KeyError(f"'count' is not in {obj}")
    count = obj["count"]
    if not isinstance(count, int):
        raise ValueError(f"{repr(count)} is not int")
    if "amountSum" not in obj:
        raise KeyError(f"'amountSum' is not in {obj}")
    amount_sum = obj["amountSum"]
    if not isinstance(amount_sum, int):
        raise ValueError(f"{repr(amount_sum)} is not int")
    return B2bBulkTaxInvoiceStat(count, amount_sum)
