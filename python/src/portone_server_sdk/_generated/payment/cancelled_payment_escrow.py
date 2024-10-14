from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class CancelledPaymentEscrow:
    """거래 취소
    """
    status: Literal["CANCELLED"] = field(repr=False)
    """에스크로 상태
    """
    company: str
    """택배사
    """
    invoice_number: str
    """송장번호
    """
    sent_at: Optional[str]
    """발송 일시
    (RFC 3339 date-time)
    """
    applied_at: Optional[str]
    """배송등록 처리 일자
    (RFC 3339 date-time)
    """


def _serialize_cancelled_payment_escrow(obj: CancelledPaymentEscrow) -> Any:
    entity = {}
    entity["status"] = "CANCELLED"
    entity["company"] = obj.company
    entity["invoiceNumber"] = obj.invoice_number
    if obj.sent_at is not None:
        entity["sentAt"] = obj.sent_at
    if obj.applied_at is not None:
        entity["appliedAt"] = obj.applied_at
    return entity


def _deserialize_cancelled_payment_escrow(obj: Any) -> CancelledPaymentEscrow:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    if status != "CANCELLED":
        raise ValueError(f"{repr(status)} is not 'CANCELLED'")
    if "company" not in obj:
        raise KeyError(f"'company' is not in {obj}")
    company = obj["company"]
    if not isinstance(company, str):
        raise ValueError(f"{repr(company)} is not str")
    if "invoiceNumber" not in obj:
        raise KeyError(f"'invoiceNumber' is not in {obj}")
    invoice_number = obj["invoiceNumber"]
    if not isinstance(invoice_number, str):
        raise ValueError(f"{repr(invoice_number)} is not str")
    if "sentAt" in obj:
        sent_at = obj["sentAt"]
        if not isinstance(sent_at, str):
            raise ValueError(f"{repr(sent_at)} is not str")
    else:
        sent_at = None
    if "appliedAt" in obj:
        applied_at = obj["appliedAt"]
        if not isinstance(applied_at, str):
            raise ValueError(f"{repr(applied_at)} is not str")
    else:
        applied_at = None
    return CancelledPaymentEscrow(status, company, invoice_number, sent_at, applied_at)
