from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bTaxInvoiceNotRequestedStatusError:
    """세금계산서가 역발행 대기 상태가 아닌 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_tax_invoice_not_requested_status_error(obj: B2bTaxInvoiceNotRequestedStatusError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_tax_invoice_not_requested_status_error(obj: Any) -> B2bTaxInvoiceNotRequestedStatusError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
        raise ValueError("Expected 'B2B_TAX_INVOICE_NOT_REQUESTED_STATUS' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return B2bTaxInvoiceNotRequestedStatusError(message)
