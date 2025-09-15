from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice import B2bTaxInvoice, _deserialize_b2b_tax_invoice, _serialize_b2b_tax_invoice

@dataclass
class IssueB2bTaxInvoiceResponse:
    """세금계산서 발행 승인 응답
    """
    tax_invoice: B2bTaxInvoice


def _serialize_issue_b2b_tax_invoice_response(obj: IssueB2bTaxInvoiceResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["taxInvoice"] = _serialize_b2b_tax_invoice(obj.tax_invoice)
    return entity


def _deserialize_issue_b2b_tax_invoice_response(obj: Any) -> IssueB2bTaxInvoiceResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "taxInvoice" not in obj:
        raise KeyError(f"'taxInvoice' is not in {obj}")
    tax_invoice = obj["taxInvoice"]
    tax_invoice = _deserialize_b2b_tax_invoice(tax_invoice)
    return IssueB2bTaxInvoiceResponse(tax_invoice)
