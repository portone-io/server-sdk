from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bTaxInvoiceNoRecipientDocumentKeyError:
    """세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_tax_invoice_no_recipient_document_key_error(obj: B2bTaxInvoiceNoRecipientDocumentKeyError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_tax_invoice_no_recipient_document_key_error(obj: Any) -> B2bTaxInvoiceNoRecipientDocumentKeyError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY":
        raise ValueError(f"{repr(type)} is not 'B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bTaxInvoiceNoRecipientDocumentKeyError(message)
