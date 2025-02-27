from __future__ import annotations
from typing import Any, Literal, Optional, Union

CashReceiptSortBy = Union[Literal["ISSUED_AT", "CANCELLED_AT", "STATUS_UPDATED_AT"], str]
"""현금영수증 정렬 기준
"""


def _serialize_cash_receipt_sort_by(obj: CashReceiptSortBy) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_cash_receipt_sort_by(obj: Any) -> CashReceiptSortBy:
    return obj
