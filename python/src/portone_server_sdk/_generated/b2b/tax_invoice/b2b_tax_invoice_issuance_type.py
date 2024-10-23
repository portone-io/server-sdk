from __future__ import annotations
from typing import Any, Literal, Optional

B2bTaxInvoiceIssuanceType = Literal["NORMAL", "REVERSE"]
"""발행 유형
"""


def _serialize_b2b_tax_invoice_issuance_type(obj: B2bTaxInvoiceIssuanceType) -> Any:
    return obj


def _deserialize_b2b_tax_invoice_issuance_type(obj: Any) -> B2bTaxInvoiceIssuanceType:
    if obj not in ["NORMAL", "REVERSE"]:
        raise ValueError(f"{repr(obj)} is not B2bTaxInvoiceIssuanceType")
    return obj
