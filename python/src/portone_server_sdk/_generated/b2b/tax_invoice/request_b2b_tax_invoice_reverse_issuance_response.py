from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice import B2bTaxInvoice, _deserialize_b2b_tax_invoice, _serialize_b2b_tax_invoice

@dataclass
class RequestB2bTaxInvoiceReverseIssuanceResponse:
    """세금계산서 역발행 즉시 요청 응답
    """
    tax_invoice: B2bTaxInvoice


def _serialize_request_b2b_tax_invoice_reverse_issuance_response(obj: RequestB2bTaxInvoiceReverseIssuanceResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["taxInvoice"] = _serialize_b2b_tax_invoice(obj.tax_invoice)
    return entity


def _deserialize_request_b2b_tax_invoice_reverse_issuance_response(obj: Any) -> RequestB2bTaxInvoiceReverseIssuanceResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "taxInvoice" not in obj:
        raise KeyError(f"'taxInvoice' is not in {obj}")
    tax_invoice = obj["taxInvoice"]
    tax_invoice = _deserialize_b2b_tax_invoice(tax_invoice)
    return RequestB2bTaxInvoiceReverseIssuanceResponse(tax_invoice)
