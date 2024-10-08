from __future__ import annotations
from typing import Any, Literal, Optional

B2bTaxInvoiceDocumentKeyType = Literal["SUPPLIER", "RECIPIENT"]
"""문서번호 유형
"""


def _serialize_b2b_tax_invoice_document_key_type(obj: B2bTaxInvoiceDocumentKeyType) -> Any:
    return obj


def _deserialize_b2b_tax_invoice_document_key_type(obj: Any) -> B2bTaxInvoiceDocumentKeyType:
    if obj not in ["SUPPLIER", "RECIPIENT"]:
        raise ValueError(f"{repr(obj)} is not B2bTaxInvoiceDocumentKeyType")
    return obj
