from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice import B2bTaxInvoice, _deserialize_b2b_tax_invoice, _serialize_b2b_tax_invoice

@dataclass
class RefuseB2bTaxInvoiceRequestResponse:
    """세금계산서 역발행 요청 거부 응답
    """
    tax_invoice: B2bTaxInvoice


def _serialize_refuse_b2b_tax_invoice_request_response(obj: RefuseB2bTaxInvoiceRequestResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["taxInvoice"] = _serialize_b2b_tax_invoice(obj.tax_invoice)
    return entity


def _deserialize_refuse_b2b_tax_invoice_request_response(obj: Any) -> RefuseB2bTaxInvoiceRequestResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "taxInvoice" not in obj:
        raise KeyError(f"'taxInvoice' is not in {obj}")
    tax_invoice = obj["taxInvoice"]
    tax_invoice = _deserialize_b2b_tax_invoice(tax_invoice)
    return RefuseB2bTaxInvoiceRequestResponse(tax_invoice)
