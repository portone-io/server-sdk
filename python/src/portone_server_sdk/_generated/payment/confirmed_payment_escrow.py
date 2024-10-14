from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class ConfirmedPaymentEscrow:
    """구매 확정
    """
    status: Literal["CONFIRMED"] = field(repr=False)
    """에스크로 상태
    """
    company: str
    """택배사
    """
    invoice_number: str
    """송장번호
    """
    is_automatically_confirmed: bool
    """자동 구매 확정 처리 여부
    """
    sent_at: Optional[str]
    """발송 일시
    (RFC 3339 date-time)
    """
    applied_at: Optional[str]
    """배송등록 처리 일자
    (RFC 3339 date-time)
    """


def _serialize_confirmed_payment_escrow(obj: ConfirmedPaymentEscrow) -> Any:
    entity = {}
    entity["status"] = "CONFIRMED"
    entity["company"] = obj.company
    entity["invoiceNumber"] = obj.invoice_number
    entity["isAutomaticallyConfirmed"] = obj.is_automatically_confirmed
    if obj.sent_at is not None:
        entity["sentAt"] = obj.sent_at
    if obj.applied_at is not None:
        entity["appliedAt"] = obj.applied_at
    return entity


def _deserialize_confirmed_payment_escrow(obj: Any) -> ConfirmedPaymentEscrow:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    if status != "CONFIRMED":
        raise ValueError(f"{repr(status)} is not 'CONFIRMED'")
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
    if "isAutomaticallyConfirmed" not in obj:
        raise KeyError(f"'isAutomaticallyConfirmed' is not in {obj}")
    is_automatically_confirmed = obj["isAutomaticallyConfirmed"]
    if not isinstance(is_automatically_confirmed, bool):
        raise ValueError(f"{repr(is_automatically_confirmed)} is not bool")
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
    return ConfirmedPaymentEscrow(status, company, invoice_number, is_automatically_confirmed, sent_at, applied_at)
