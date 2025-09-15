from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bTaxInvoicePurposeType = Union[Literal["RECEIPT", "INVOICE", "NONE"], str]
"""영수/청구
"""


def _serialize_b2b_tax_invoice_purpose_type(obj: B2bTaxInvoicePurposeType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_tax_invoice_purpose_type(obj: Any) -> B2bTaxInvoicePurposeType:
    return obj
