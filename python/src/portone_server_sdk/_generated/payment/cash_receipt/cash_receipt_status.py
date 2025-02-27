from __future__ import annotations
from typing import Any, Literal, Optional, Union

CashReceiptStatus = Union[Literal["ISSUED", "CANCELLED", "FAILED"], str]
"""현금영수증 발급 건 상태
"""


def _serialize_cash_receipt_status(obj: CashReceiptStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_cash_receipt_status(obj: Any) -> CashReceiptStatus:
    return obj
