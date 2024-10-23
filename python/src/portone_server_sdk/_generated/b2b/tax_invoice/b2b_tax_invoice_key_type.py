from __future__ import annotations
from typing import Any, Literal, Optional

B2bTaxInvoiceKeyType = Literal["SUPPLIER", "RECIPIENT", "TAX_INVOICE_ID"]
"""세금계산서 식별자 유형
"""


def _serialize_b2b_tax_invoice_key_type(obj: B2bTaxInvoiceKeyType) -> Any:
    return obj


def _deserialize_b2b_tax_invoice_key_type(obj: Any) -> B2bTaxInvoiceKeyType:
    if obj not in ["SUPPLIER", "RECIPIENT", "TAX_INVOICE_ID"]:
        raise ValueError(f"{repr(obj)} is not B2bTaxInvoiceKeyType")
    return obj
