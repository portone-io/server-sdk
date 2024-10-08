from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CancelCashReceiptResponse:
    """현금 영수증 취소 성공 응답
    """
    cancelled_amount: int
    """취소 금액
    (int64)
    """
    cancelled_at: str
    """현금 영수증 취소 완료 시점
    (RFC 3339 date-time)
    """


def _serialize_cancel_cash_receipt_response(obj: CancelCashReceiptResponse) -> Any:
    entity = {}
    entity["cancelledAmount"] = obj.cancelled_amount
    entity["cancelledAt"] = obj.cancelled_at
    return entity


def _deserialize_cancel_cash_receipt_response(obj: Any) -> CancelCashReceiptResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "cancelledAmount" not in obj:
        raise KeyError(f"'cancelledAmount' is not in {obj}")
    cancelled_amount = obj["cancelledAmount"]
    if not isinstance(cancelled_amount, int):
        raise ValueError(f"{repr(cancelled_amount)} is not int")
    if "cancelledAt" not in obj:
        raise KeyError(f"'cancelledAt' is not in {obj}")
    cancelled_at = obj["cancelledAt"]
    if not isinstance(cancelled_at, str):
        raise ValueError(f"{repr(cancelled_at)} is not str")
    return CancelCashReceiptResponse(cancelled_amount, cancelled_at)
