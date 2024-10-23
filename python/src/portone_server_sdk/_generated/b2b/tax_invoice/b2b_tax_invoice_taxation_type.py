from __future__ import annotations
from typing import Any, Literal, Optional

B2bTaxInvoiceTaxationType = Literal["TAXABLE", "ZERO_RATED", "FREE"]
"""과세 유형
"""


def _serialize_b2b_tax_invoice_taxation_type(obj: B2bTaxInvoiceTaxationType) -> Any:
    return obj


def _deserialize_b2b_tax_invoice_taxation_type(obj: Any) -> B2bTaxInvoiceTaxationType:
    if obj not in ["TAXABLE", "ZERO_RATED", "FREE"]:
        raise ValueError(f"{repr(obj)} is not B2bTaxInvoiceTaxationType")
    return obj
