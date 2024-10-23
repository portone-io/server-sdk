from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError:
    """세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
    """
    type: Literal["B2B_TAX_INVOICE_SUPPLIER_DOCUMENT_KEY_ALREADY_USED"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_tax_invoice_supplier_document_key_already_used_error(obj: B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError) -> Any:
    entity = {}
    entity["type"] = "B2B_TAX_INVOICE_SUPPLIER_DOCUMENT_KEY_ALREADY_USED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_tax_invoice_supplier_document_key_already_used_error(obj: Any) -> B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_TAX_INVOICE_SUPPLIER_DOCUMENT_KEY_ALREADY_USED":
        raise ValueError(f"{repr(type)} is not 'B2B_TAX_INVOICE_SUPPLIER_DOCUMENT_KEY_ALREADY_USED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError(type, message)
