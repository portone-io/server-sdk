from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bBulkTaxInvoiceStatus = Union[Literal["DRAFT_PENDING", "DRAFTED", "REQUEST_PENDING", "ISSUE_PENDING", "IN_PROGRESS", "COMPLETED", "FAILED", "CANCELLED"], str]
"""일괄 세금계산서 상태
"""


def _serialize_b2b_bulk_tax_invoice_status(obj: B2bBulkTaxInvoiceStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_bulk_tax_invoice_status(obj: Any) -> B2bBulkTaxInvoiceStatus:
    return obj
