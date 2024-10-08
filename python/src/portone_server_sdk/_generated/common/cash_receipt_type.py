from __future__ import annotations
from typing import Any, Literal, Optional

CashReceiptType = Literal["PERSONAL", "CORPORATE"]
"""발급 유형
"""


def _serialize_cash_receipt_type(obj: CashReceiptType) -> Any:
    return obj


def _deserialize_cash_receipt_type(obj: Any) -> CashReceiptType:
    if obj not in ["PERSONAL", "CORPORATE"]:
        raise ValueError(f"{repr(obj)} is not CashReceiptType")
    return obj
