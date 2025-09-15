from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bTaxInvoiceTaxationType = Union[Literal["TAXABLE", "ZERO_RATED", "FREE"], str]
"""과세 유형
"""


def _serialize_b2b_tax_invoice_taxation_type(obj: B2bTaxInvoiceTaxationType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_tax_invoice_taxation_type(obj: Any) -> B2bTaxInvoiceTaxationType:
    return obj
