from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.b2b_tax_invoice_input import B2bTaxInvoiceInput, _deserialize_b2b_tax_invoice_input, _serialize_b2b_tax_invoice_input

@dataclass
class RequestB2bTaxInvoiceRegisterBody:
    """세금계산서 임시 저장 정보
    """
    tax_invoice: B2bTaxInvoiceInput
    """세금계산서 생성 요청 정보
    """


def _serialize_request_b2b_tax_invoice_register_body(obj: RequestB2bTaxInvoiceRegisterBody) -> Any:
    entity = {}
    entity["taxInvoice"] = _serialize_b2b_tax_invoice_input(obj.tax_invoice)
    return entity


def _deserialize_request_b2b_tax_invoice_register_body(obj: Any) -> RequestB2bTaxInvoiceRegisterBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "taxInvoice" not in obj:
        raise KeyError(f"'taxInvoice' is not in {obj}")
    tax_invoice = obj["taxInvoice"]
    tax_invoice = _deserialize_b2b_tax_invoice_input(tax_invoice)
    return RequestB2bTaxInvoiceRegisterBody(tax_invoice)
