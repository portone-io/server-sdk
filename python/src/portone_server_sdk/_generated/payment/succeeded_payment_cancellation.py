from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class SucceededPaymentCancellation:
    """취소 완료 상태
    """
    status: Literal["SUCCEEDED"] = field(repr=False)
    """결제 취소 내역 상태
    """
    id: str
    """취소 내역 아이디
    """
    total_amount: int
    """취소 총 금액
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
    pg_cancellation_id: Optional[str]
    """PG사 결제 취소 내역 아이디
    """
    easy_pay_discount_amount: Optional[int]
    """적립형 포인트의 환불 금액
    (int64)
    """
    cancelled_at: Optional[str]
    """취소 시점
    (RFC 3339 date-time)
    """
    receipt_url: Optional[str]
    """취소 영수증 URL
    """


def _serialize_succeeded_payment_cancellation(obj: SucceededPaymentCancellation) -> Any:
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
    return entity


def _deserialize_succeeded_payment_cancellation(obj: Any) -> SucceededPaymentCancellation:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    if status != "SUCCEEDED":
        raise ValueError(f"{repr(status)} is not 'SUCCEEDED'")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "totalAmount" not in obj:
        raise KeyError(f"'totalAmount' is not in {obj}")
    total_amount = obj["totalAmount"]
    if not isinstance(total_amount, int):
        raise ValueError(f"{repr(total_amount)} is not int")
    if "taxFreeAmount" not in obj:
        raise KeyError(f"'taxFreeAmount' is not in {obj}")
    tax_free_amount = obj["taxFreeAmount"]
    if not isinstance(tax_free_amount, int):
        raise ValueError(f"{repr(tax_free_amount)} is not int")
    if "vatAmount" not in obj:
        raise KeyError(f"'vatAmount' is not in {obj}")
    vat_amount = obj["vatAmount"]
    if not isinstance(vat_amount, int):
        raise ValueError(f"{repr(vat_amount)} is not int")
    if "reason" not in obj:
        raise KeyError(f"'reason' is not in {obj}")
    reason = obj["reason"]
    if not isinstance(reason, str):
        raise ValueError(f"{repr(reason)} is not str")
    if "requestedAt" not in obj:
        raise KeyError(f"'requestedAt' is not in {obj}")
    requested_at = obj["requestedAt"]
    if not isinstance(requested_at, str):
        raise ValueError(f"{repr(requested_at)} is not str")
    if "pgCancellationId" in obj:
        pg_cancellation_id = obj["pgCancellationId"]
        if not isinstance(pg_cancellation_id, str):
            raise ValueError(f"{repr(pg_cancellation_id)} is not str")
    else:
        pg_cancellation_id = None
    if "easyPayDiscountAmount" in obj:
        easy_pay_discount_amount = obj["easyPayDiscountAmount"]
        if not isinstance(easy_pay_discount_amount, int):
            raise ValueError(f"{repr(easy_pay_discount_amount)} is not int")
    else:
        easy_pay_discount_amount = None
    if "cancelledAt" in obj:
        cancelled_at = obj["cancelledAt"]
        if not isinstance(cancelled_at, str):
            raise ValueError(f"{repr(cancelled_at)} is not str")
    else:
        cancelled_at = None
    if "receiptUrl" in obj:
        receipt_url = obj["receiptUrl"]
        if not isinstance(receipt_url, str):
            raise ValueError(f"{repr(receipt_url)} is not str")
    else:
        receipt_url = None
    return SucceededPaymentCancellation(status, id, total_amount, tax_free_amount, vat_amount, reason, requested_at, pg_cancellation_id, easy_pay_discount_amount, cancelled_at, receipt_url)
