from __future__ import annotations
from typing import Any, Literal, Optional

B2bTaxInvoicePurposeType = Literal["RECEIPT", "INVOICE", "NONE"]
"""영수/청구
"""


def _serialize_b2b_tax_invoice_purpose_type(obj: B2bTaxInvoicePurposeType) -> Any:
    return obj


def _deserialize_b2b_tax_invoice_purpose_type(obj: Any) -> B2bTaxInvoicePurposeType:
    if obj not in ["RECEIPT", "INVOICE", "NONE"]:
        raise ValueError(f"{repr(obj)} is not B2bTaxInvoicePurposeType")
    return obj
