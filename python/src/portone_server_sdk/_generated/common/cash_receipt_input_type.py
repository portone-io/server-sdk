from __future__ import annotations
from typing import Any, Literal, Optional, Union

CashReceiptInputType = Union[Literal["PERSONAL", "CORPORATE", "NO_RECEIPT"], str]
"""입력 시 발급 유형
"""


def _serialize_cash_receipt_input_type(obj: CashReceiptInputType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_cash_receipt_input_type(obj: Any) -> CashReceiptInputType:
    return obj
