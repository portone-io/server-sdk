from __future__ import annotations
from typing import Any, Literal, Optional, Union

CashReceiptType = Union[Literal["PERSONAL", "CORPORATE"], str]
"""발급 유형
"""


def _serialize_cash_receipt_type(obj: CashReceiptType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_cash_receipt_type(obj: Any) -> CashReceiptType:
    return obj
