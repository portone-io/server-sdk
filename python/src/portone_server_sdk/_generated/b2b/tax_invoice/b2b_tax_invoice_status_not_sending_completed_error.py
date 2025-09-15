from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2BTaxInvoiceStatusNotSendingCompletedError:
    """원본 세금계산서가 전송완료 상태가 아닌 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_tax_invoice_status_not_sending_completed_error(obj: B2BTaxInvoiceStatusNotSendingCompletedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_tax_invoice_status_not_sending_completed_error(obj: Any) -> B2BTaxInvoiceStatusNotSendingCompletedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED":
        raise ValueError(f"{repr(type)} is not 'B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2BTaxInvoiceStatusNotSendingCompletedError(message)
