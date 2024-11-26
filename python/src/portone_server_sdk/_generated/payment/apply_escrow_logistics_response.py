from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ApplyEscrowLogisticsResponse:
    """에스크로 배송 정보 등록 성공 응답
    """
    invoice_number: str
    """송장 번호
    """
    sent_at: str
    """발송 시점
    (RFC 3339 date-time)
    """
    applied_at: str
    """에스크로 정보 등록 시점
    (RFC 3339 date-time)
    """


def _serialize_apply_escrow_logistics_response(obj: ApplyEscrowLogisticsResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["invoiceNumber"] = obj.invoice_number
    entity["sentAt"] = obj.sent_at
    entity["appliedAt"] = obj.applied_at
    return entity


def _deserialize_apply_escrow_logistics_response(obj: Any) -> ApplyEscrowLogisticsResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "invoiceNumber" not in obj:
        raise KeyError(f"'invoiceNumber' is not in {obj}")
    invoice_number = obj["invoiceNumber"]
    if not isinstance(invoice_number, str):
        raise ValueError(f"{repr(invoice_number)} is not str")
    if "sentAt" not in obj:
        raise KeyError(f"'sentAt' is not in {obj}")
    sent_at = obj["sentAt"]
    if not isinstance(sent_at, str):
        raise ValueError(f"{repr(sent_at)} is not str")
    if "appliedAt" not in obj:
        raise KeyError(f"'appliedAt' is not in {obj}")
    applied_at = obj["appliedAt"]
    if not isinstance(applied_at, str):
        raise ValueError(f"{repr(applied_at)} is not str")
    return ApplyEscrowLogisticsResponse(invoice_number, sent_at, applied_at)
