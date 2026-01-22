from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bTaxInvoiceSortBy = Union[Literal["WRITE_DATE", "ISSUANCE_DUE_DATE", "TOTAL_AMOUNT", "TOTAL_SUPPLY_AMOUNT", "TOTAL_TAX_AMOUNT", "REQUESTED_AT", "ISSUED_AT", "NTS_SENT_AT", "STATUS_UPDATED_AT"], str]
"""세금계산서 정렬 기준
"""


def _serialize_b2b_tax_invoice_sort_by(obj: B2bTaxInvoiceSortBy) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_tax_invoice_sort_by(obj: Any) -> B2bTaxInvoiceSortBy:
    return obj
