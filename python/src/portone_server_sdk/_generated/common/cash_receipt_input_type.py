from __future__ import annotations
from typing import Any, Literal, Optional

CashReceiptInputType = Literal["PERSONAL", "CORPORATE", "NO_RECEIPT"]
"""입력 시 발급 유형
"""


def _serialize_cash_receipt_input_type(obj: CashReceiptInputType) -> Any:
    return obj


def _deserialize_cash_receipt_input_type(obj: Any) -> CashReceiptInputType:
    if obj not in ["PERSONAL", "CORPORATE", "NO_RECEIPT"]:
        raise ValueError(f"{repr(obj)} is not CashReceiptInputType")
    return obj
