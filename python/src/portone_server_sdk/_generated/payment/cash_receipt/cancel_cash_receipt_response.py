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
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["cancelledAmount"] = obj.cancelled_amount
    entity["cancelledAt"] = obj.cancelled_at
    return entity


def _deserialize_cancel_cash_receipt_response(obj: Any) -> CancelCashReceiptResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "cancelledAmount" not in obj:
        raise KeyError("Missing required field 'cancelledAmount'")
    cancelled_amount = obj["cancelledAmount"]
    if not isinstance(cancelled_amount, int):
        raise ValueError("Expected int for cancelled_amount")
    if "cancelledAt" not in obj:
        raise KeyError("Missing required field 'cancelledAt'")
    cancelled_at = obj["cancelledAt"]
    if not isinstance(cancelled_at, str):
        raise ValueError("Expected str for cancelled_at")
    return CancelCashReceiptResponse(cancelled_amount, cancelled_at)
