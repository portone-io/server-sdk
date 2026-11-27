from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice import B2bTaxInvoice, _deserialize_b2b_tax_invoice, _serialize_b2b_tax_invoice

@dataclass
class DraftB2bTaxInvoiceResponse:
    """세금계산서 임시 저장 응답
    """
    tax_invoice: B2bTaxInvoice


def _serialize_draft_b2b_tax_invoice_response(obj: DraftB2bTaxInvoiceResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["taxInvoice"] = _serialize_b2b_tax_invoice(obj.tax_invoice)
    return entity


def _deserialize_draft_b2b_tax_invoice_response(obj: Any) -> DraftB2bTaxInvoiceResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "taxInvoice" not in obj:
        raise KeyError("Missing required field 'taxInvoice'")
    tax_invoice = obj["taxInvoice"]
    tax_invoice = _deserialize_b2b_tax_invoice(tax_invoice)
    return DraftB2bTaxInvoiceResponse(tax_invoice)
