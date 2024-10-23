from __future__ import annotations
from typing import Any, Literal, Optional

B2bTaxInvoiceStatus = Literal["DRAFTED", "DRAFT_PENDING", "DRAFT_FAILED", "REQUESTED", "REQUEST_PENDING", "REQUEST_FAILED", "REQUEST_CANCELLED", "ISSUED", "BEFORE_SENDING", "WAITING_SENDING", "SENDING", "SENDING_COMPLETED", "SENDING_FAILED", "REQUEST_REFUSED", "ISSUANCE_CANCELLED"]


def _serialize_b2b_tax_invoice_status(obj: B2bTaxInvoiceStatus) -> Any:
    return obj


def _deserialize_b2b_tax_invoice_status(obj: Any) -> B2bTaxInvoiceStatus:
    if obj not in ["DRAFTED", "DRAFT_PENDING", "DRAFT_FAILED", "REQUESTED", "REQUEST_PENDING", "REQUEST_FAILED", "REQUEST_CANCELLED", "ISSUED", "BEFORE_SENDING", "WAITING_SENDING", "SENDING", "SENDING_COMPLETED", "SENDING_FAILED", "REQUEST_REFUSED", "ISSUANCE_CANCELLED"]:
        raise ValueError(f"{repr(obj)} is not B2bTaxInvoiceStatus")
    return obj
