from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_input import B2bTaxInvoiceInput, _deserialize_b2b_tax_invoice_input, _serialize_b2b_tax_invoice_input
from ...b2b.tax_invoice.b2b_tax_invoice_modification_create_body import B2bTaxInvoiceModificationCreateBody, _deserialize_b2b_tax_invoice_modification_create_body, _serialize_b2b_tax_invoice_modification_create_body

@dataclass
class RequestB2bTaxInvoiceReverseIssuanceBody:
    """세금계산서 역발행 즉시 요청 정보
    """
    tax_invoice: B2bTaxInvoiceInput
    """세금계산서 생성 요청 정보
    """
    memo: Optional[str] = field(default=None)
    """메모
    """
    modification: Optional[B2bTaxInvoiceModificationCreateBody] = field(default=None)
    """수정 세금계산서 입력 정보
    """


def _serialize_request_b2b_tax_invoice_reverse_issuance_body(obj: RequestB2bTaxInvoiceReverseIssuanceBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["taxInvoice"] = _serialize_b2b_tax_invoice_input(obj.tax_invoice)
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.modification is not None:
        entity["modification"] = _serialize_b2b_tax_invoice_modification_create_body(obj.modification)
    return entity


def _deserialize_request_b2b_tax_invoice_reverse_issuance_body(obj: Any) -> RequestB2bTaxInvoiceReverseIssuanceBody:
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
    if "modification" in obj:
        modification = obj["modification"]
        modification = _deserialize_b2b_tax_invoice_modification_create_body(modification)
    else:
        modification = None
    return RequestB2bTaxInvoiceReverseIssuanceBody(tax_invoice, memo, modification)
