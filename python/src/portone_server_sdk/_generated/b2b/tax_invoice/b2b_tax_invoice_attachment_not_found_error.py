from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bTaxInvoiceAttachmentNotFoundError:
    """세금계산서의 첨부파일을 찾을 수 없는 경우
    """
    type: Literal["B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_tax_invoice_attachment_not_found_error(obj: B2bTaxInvoiceAttachmentNotFoundError) -> Any:
    entity = {}
    entity["type"] = "B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_tax_invoice_attachment_not_found_error(obj: Any) -> B2bTaxInvoiceAttachmentNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bTaxInvoiceAttachmentNotFoundError(type, message)
