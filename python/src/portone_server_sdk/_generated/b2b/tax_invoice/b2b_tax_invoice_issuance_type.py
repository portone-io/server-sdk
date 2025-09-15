from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bTaxInvoiceIssuanceType = Union[Literal["NORMAL", "REVERSE"], str]
"""발행 유형
"""


def _serialize_b2b_tax_invoice_issuance_type(obj: B2bTaxInvoiceIssuanceType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_tax_invoice_issuance_type(obj: Any) -> B2bTaxInvoiceIssuanceType:
    return obj
