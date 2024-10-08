from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.b2b_tax_invoice_input import B2bTaxInvoiceInput, _deserialize_b2b_tax_invoice_input, _serialize_b2b_tax_invoice_input

@dataclass
class RequestB2bTaxInvoiceReverseIssuanceRequestBody:
    """세금계산서 역발행 요청 정보
    """
    tax_invoice: B2bTaxInvoiceInput
    """세금계산서 생성 요청 정보
    """
    memo: Optional[str]
    """메모
    """


def _serialize_request_b2b_tax_invoice_reverse_issuance_request_body(obj: RequestB2bTaxInvoiceReverseIssuanceRequestBody) -> Any:
    entity = {}
    entity["taxInvoice"] = _serialize_b2b_tax_invoice_input(obj.tax_invoice)
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_request_b2b_tax_invoice_reverse_issuance_request_body(obj: Any) -> RequestB2bTaxInvoiceReverseIssuanceRequestBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "taxInvoice" not in obj:
        raise KeyError(f"'taxInvoice' is not in {obj}")
    tax_invoice = obj["taxInvoice"]
    tax_invoice = _deserialize_b2b_tax_invoice_input(tax_invoice)
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return RequestB2bTaxInvoiceReverseIssuanceRequestBody(tax_invoice, memo)
