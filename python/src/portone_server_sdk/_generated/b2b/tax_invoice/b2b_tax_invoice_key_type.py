from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bTaxInvoiceKeyType = Union[Literal["SUPPLIER", "RECIPIENT", "TAX_INVOICE_ID"], str]
"""세금계산서 식별자 유형
"""


def _serialize_b2b_tax_invoice_key_type(obj: B2bTaxInvoiceKeyType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_tax_invoice_key_type(obj: Any) -> B2bTaxInvoiceKeyType:
    return obj
