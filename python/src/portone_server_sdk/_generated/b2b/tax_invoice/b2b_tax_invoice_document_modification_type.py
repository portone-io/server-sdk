from __future__ import annotations
from typing import Any, Literal, Optional

B2bTaxInvoiceDocumentModificationType = Literal["NORMAL", "MODIFICATION"]
"""세금계산서 문서 수정 발행 유형
"""


def _serialize_b2b_tax_invoice_document_modification_type(obj: B2bTaxInvoiceDocumentModificationType) -> Any:
    return obj


def _deserialize_b2b_tax_invoice_document_modification_type(obj: Any) -> B2bTaxInvoiceDocumentModificationType:
    if obj not in ["NORMAL", "MODIFICATION"]:
        raise ValueError(f"{repr(obj)} is not B2bTaxInvoiceDocumentModificationType")
    return obj
