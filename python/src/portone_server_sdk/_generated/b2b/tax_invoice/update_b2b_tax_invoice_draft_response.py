from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice import B2bTaxInvoice, _deserialize_b2b_tax_invoice, _serialize_b2b_tax_invoice

@dataclass
class UpdateB2bTaxInvoiceDraftResponse:
    """세금계산서 임시저장 수정 응답
    """
    tax_invoice: B2bTaxInvoice


def _serialize_update_b2b_tax_invoice_draft_response(obj: UpdateB2bTaxInvoiceDraftResponse) -> Any:
    entity = {}
    entity["taxInvoice"] = _serialize_b2b_tax_invoice(obj.tax_invoice)
    return entity


def _deserialize_update_b2b_tax_invoice_draft_response(obj: Any) -> UpdateB2bTaxInvoiceDraftResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "taxInvoice" not in obj:
        raise KeyError(f"'taxInvoice' is not in {obj}")
    tax_invoice = obj["taxInvoice"]
    tax_invoice = _deserialize_b2b_tax_invoice(tax_invoice)
    return UpdateB2bTaxInvoiceDraftResponse(tax_invoice)
