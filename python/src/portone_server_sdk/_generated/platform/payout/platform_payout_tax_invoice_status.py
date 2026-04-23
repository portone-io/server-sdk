from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformPayoutTaxInvoiceStatus = Union[Literal["NONE", "DRAFTED", "DRAFT_PENDING", "DRAFT_FAILED", "REQUESTED", "REQUEST_PENDING", "REQUEST_FAILED", "REQUEST_CANCELLED", "REQUEST_REFUSED", "ISSUED", "ISSUE_PENDING", "ISSUE_FAILED", "ISSUANCE_CANCELLED", "CANCEL_PENDING", "BEFORE_SENDING", "WAITING_SENDING", "SENDING", "SENDING_PENDING", "SENDING_COMPLETED", "SENDING_FAILED"], str]


def _serialize_platform_payout_tax_invoice_status(obj: PlatformPayoutTaxInvoiceStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_payout_tax_invoice_status(obj: Any) -> PlatformPayoutTaxInvoiceStatus:
    return obj
