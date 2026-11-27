from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.trigger import Trigger, _deserialize_trigger, _serialize_trigger

@dataclass
class SucceededPaymentCancellation:
    """취소 완료 상태
    """
    """결제 취소 내역 상태
    """
    id: str
    """취소 내역 아이디
    """
    total_amount: int
    """취소 금액
    (int64)
    """
    tax_free_amount: int
    """취소 금액 중 면세 금액
    (int64)
    """
    vat_amount: int
    """취소 금액 중 부가세액
    (int64)
    """
    reason: str
    """취소 사유
    """
    requested_at: str
    """취소 요청 시점
    (RFC 3339 date-time)
    """
    pg_cancellation_id: Optional[str] = field(default=None)
    """PG사 결제 취소 내역 아이디
    """
    easy_pay_discount_amount: Optional[int] = field(default=None)
    """적립형 포인트의 환불 금액
    (int64)
    """
    cancelled_at: Optional[str] = field(default=None)
    """취소 시점
    (RFC 3339 date-time)
    """
    receipt_url: Optional[str] = field(default=None)
    """취소 영수증 URL
    """
    trigger: Optional[Trigger] = field(default=None)
    """취소 요청 경로
    """


def _serialize_succeeded_payment_cancellation(obj: SucceededPaymentCancellation) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["status"] = "SUCCEEDED"
    entity["id"] = obj.id
    entity["totalAmount"] = obj.total_amount
    entity["taxFreeAmount"] = obj.tax_free_amount
    entity["vatAmount"] = obj.vat_amount
    entity["reason"] = obj.reason
    entity["requestedAt"] = obj.requested_at
    if obj.pg_cancellation_id is not None:
        entity["pgCancellationId"] = obj.pg_cancellation_id
    if obj.easy_pay_discount_amount is not None:
        entity["easyPayDiscountAmount"] = obj.easy_pay_discount_amount
    if obj.cancelled_at is not None:
        entity["cancelledAt"] = obj.cancelled_at
    if obj.receipt_url is not None:
        entity["receiptUrl"] = obj.receipt_url
    if obj.trigger is not None:
        entity["trigger"] = _serialize_trigger(obj.trigger)
    return entity


def _deserialize_succeeded_payment_cancellation(obj: Any) -> SucceededPaymentCancellation:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    if status != "SUCCEEDED":
        raise ValueError("Expected 'SUCCEEDED' for status")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "totalAmount" not in obj:
        raise KeyError("Missing required field 'totalAmount'")
    total_amount = obj["totalAmount"]
    if not isinstance(total_amount, int):
        raise ValueError("Expected int for total_amount")
    if "taxFreeAmount" not in obj:
        raise KeyError("Missing required field 'taxFreeAmount'")
    tax_free_amount = obj["taxFreeAmount"]
    if not isinstance(tax_free_amount, int):
        raise ValueError("Expected int for tax_free_amount")
    if "vatAmount" not in obj:
        raise KeyError("Missing required field 'vatAmount'")
    vat_amount = obj["vatAmount"]
    if not isinstance(vat_amount, int):
        raise ValueError("Expected int for vat_amount")
    if "reason" not in obj:
        raise KeyError("Missing required field 'reason'")
    reason = obj["reason"]
    if not isinstance(reason, str):
        raise ValueError("Expected str for reason")
    if "requestedAt" not in obj:
        raise KeyError("Missing required field 'requestedAt'")
    requested_at = obj["requestedAt"]
    if not isinstance(requested_at, str):
        raise ValueError("Expected str for requested_at")
    if "pgCancellationId" in obj:
        pg_cancellation_id = obj["pgCancellationId"]
        if not isinstance(pg_cancellation_id, str):
            raise ValueError("Expected str for pg_cancellation_id")
    else:
        pg_cancellation_id = None
    if "easyPayDiscountAmount" in obj:
        easy_pay_discount_amount = obj["easyPayDiscountAmount"]
        if not isinstance(easy_pay_discount_amount, int):
            raise ValueError("Expected int for easy_pay_discount_amount")
    else:
        easy_pay_discount_amount = None
    if "cancelledAt" in obj:
        cancelled_at = obj["cancelledAt"]
        if not isinstance(cancelled_at, str):
            raise ValueError("Expected str for cancelled_at")
    else:
        cancelled_at = None
    if "receiptUrl" in obj:
        receipt_url = obj["receiptUrl"]
        if not isinstance(receipt_url, str):
            raise ValueError("Expected str for receipt_url")
    else:
        receipt_url = None
    if "trigger" in obj:
        trigger = obj["trigger"]
        trigger = _deserialize_trigger(trigger)
    else:
        trigger = None
    return SucceededPaymentCancellation(id, total_amount, tax_free_amount, vat_amount, reason, requested_at, pg_cancellation_id, easy_pay_discount_amount, cancelled_at, receipt_url, trigger)
