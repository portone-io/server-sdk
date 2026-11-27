from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ModifyEscrowLogisticsResponse:
    """에스크로 배송 정보 수정 성공 응답
    """
    invoice_number: str
    """송장 번호
    """
    sent_at: str
    """발송 시점
    (RFC 3339 date-time)
    """
    modified_at: str
    """에스크로 정보 수정 시점
    (RFC 3339 date-time)
    """


def _serialize_modify_escrow_logistics_response(obj: ModifyEscrowLogisticsResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["invoiceNumber"] = obj.invoice_number
    entity["sentAt"] = obj.sent_at
    entity["modifiedAt"] = obj.modified_at
    return entity


def _deserialize_modify_escrow_logistics_response(obj: Any) -> ModifyEscrowLogisticsResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "invoiceNumber" not in obj:
        raise KeyError("Missing required field 'invoiceNumber'")
    invoice_number = obj["invoiceNumber"]
    if not isinstance(invoice_number, str):
        raise ValueError("Expected str for invoice_number")
    if "sentAt" not in obj:
        raise KeyError("Missing required field 'sentAt'")
    sent_at = obj["sentAt"]
    if not isinstance(sent_at, str):
        raise ValueError("Expected str for sent_at")
    if "modifiedAt" not in obj:
        raise KeyError("Missing required field 'modifiedAt'")
    modified_at = obj["modifiedAt"]
    if not isinstance(modified_at, str):
        raise ValueError("Expected str for modified_at")
    return ModifyEscrowLogisticsResponse(invoice_number, sent_at, modified_at)
