from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bTaxInvoiceDocumentModificationType = Union[Literal["NORMAL", "MODIFICATION"], str]
"""세금계산서 문서 수정 발행 유형
"""


def _serialize_b2b_tax_invoice_document_modification_type(obj: B2bTaxInvoiceDocumentModificationType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_tax_invoice_document_modification_type(obj: Any) -> B2bTaxInvoiceDocumentModificationType:
    return obj
