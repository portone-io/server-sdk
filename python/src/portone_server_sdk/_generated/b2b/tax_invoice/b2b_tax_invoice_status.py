from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bTaxInvoiceStatus = Union[Literal["DRAFTED", "DRAFT_PENDING", "DRAFT_FAILED", "REQUESTED", "REQUEST_PENDING", "REQUEST_FAILED", "REQUEST_CANCELLED", "ISSUED", "ISSUE_PENDING", "ISSUE_FAILED", "BEFORE_SENDING", "WAITING_SENDING", "SENDING", "SENDING_COMPLETED", "SENDING_FAILED", "REQUEST_REFUSED", "ISSUANCE_CANCELLED"], str]


def _serialize_b2b_tax_invoice_status(obj: B2bTaxInvoiceStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_tax_invoice_status(obj: Any) -> B2bTaxInvoiceStatus:
    return obj
