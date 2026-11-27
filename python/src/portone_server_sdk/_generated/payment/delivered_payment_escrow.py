from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class DeliveredPaymentEscrow:
    """배송 완료
    """
    """에스크로 상태
    """
    company: str
    """택배사
    """
    invoice_number: str
    """송장번호
    """
    sent_at: Optional[str] = field(default=None)
    """발송 일시
    (RFC 3339 date-time)
    """
    applied_at: Optional[str] = field(default=None)
    """배송등록 처리 일자
    (RFC 3339 date-time)
    """


def _serialize_delivered_payment_escrow(obj: DeliveredPaymentEscrow) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["status"] = "DELIVERED"
    entity["company"] = obj.company
    entity["invoiceNumber"] = obj.invoice_number
    if obj.sent_at is not None:
        entity["sentAt"] = obj.sent_at
    if obj.applied_at is not None:
        entity["appliedAt"] = obj.applied_at
    return entity


def _deserialize_delivered_payment_escrow(obj: Any) -> DeliveredPaymentEscrow:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    if status != "DELIVERED":
        raise ValueError("Expected 'DELIVERED' for status")
    if "company" not in obj:
        raise KeyError("Missing required field 'company'")
    company = obj["company"]
    if not isinstance(company, str):
        raise ValueError("Expected str for company")
    if "invoiceNumber" not in obj:
        raise KeyError("Missing required field 'invoiceNumber'")
    invoice_number = obj["invoiceNumber"]
    if not isinstance(invoice_number, str):
        raise ValueError("Expected str for invoice_number")
    if "sentAt" in obj:
        sent_at = obj["sentAt"]
        if not isinstance(sent_at, str):
            raise ValueError("Expected str for sent_at")
    else:
        sent_at = None
    if "appliedAt" in obj:
        applied_at = obj["appliedAt"]
        if not isinstance(applied_at, str):
            raise ValueError("Expected str for applied_at")
    else:
        applied_at = None
    return DeliveredPaymentEscrow(company, invoice_number, sent_at, applied_at)
