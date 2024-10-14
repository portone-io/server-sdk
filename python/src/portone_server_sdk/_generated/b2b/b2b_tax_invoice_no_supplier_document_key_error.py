from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bTaxInvoiceNoSupplierDocumentKeyError:
    """세금계산서에 공급자 문서 번호가 기입되지 않은 경우
    """
    type: Literal["B2B_TAX_INVOICE_NO_SUPPLIER_DOCUMENT_KEY"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_tax_invoice_no_supplier_document_key_error(obj: B2bTaxInvoiceNoSupplierDocumentKeyError) -> Any:
    entity = {}
    entity["type"] = "B2B_TAX_INVOICE_NO_SUPPLIER_DOCUMENT_KEY"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_tax_invoice_no_supplier_document_key_error(obj: Any) -> B2bTaxInvoiceNoSupplierDocumentKeyError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_TAX_INVOICE_NO_SUPPLIER_DOCUMENT_KEY":
        raise ValueError(f"{repr(type)} is not 'B2B_TAX_INVOICE_NO_SUPPLIER_DOCUMENT_KEY'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bTaxInvoiceNoSupplierDocumentKeyError(type, message)
