from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_input import B2bTaxInvoiceInput, _deserialize_b2b_tax_invoice_input, _serialize_b2b_tax_invoice_input
from ...b2b.tax_invoice.b2b_tax_invoice_modification_create_body import B2bTaxInvoiceModificationCreateBody, _deserialize_b2b_tax_invoice_modification_create_body, _serialize_b2b_tax_invoice_modification_create_body

@dataclass
class DraftB2bTaxInvoiceBody:
    """세금계산서 임시 저장 정보
    """
    tax_invoice: B2bTaxInvoiceInput
    """세금계산서 생성 요청 정보
    """
    modification: Optional[B2bTaxInvoiceModificationCreateBody] = field(default=None)
    """수정 세금계산서 입력 정보
    """
    memo: Optional[str] = field(default=None)
    """메모
    """


def _serialize_draft_b2b_tax_invoice_body(obj: DraftB2bTaxInvoiceBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["taxInvoice"] = _serialize_b2b_tax_invoice_input(obj.tax_invoice)
    if obj.modification is not None:
        entity["modification"] = _serialize_b2b_tax_invoice_modification_create_body(obj.modification)
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_draft_b2b_tax_invoice_body(obj: Any) -> DraftB2bTaxInvoiceBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "taxInvoice" not in obj:
        raise KeyError(f"'taxInvoice' is not in {obj}")
    tax_invoice = obj["taxInvoice"]
    tax_invoice = _deserialize_b2b_tax_invoice_input(tax_invoice)
    if "modification" in obj:
        modification = obj["modification"]
        modification = _deserialize_b2b_tax_invoice_modification_create_body(modification)
    else:
        modification = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return DraftB2bTaxInvoiceBody(tax_invoice, modification, memo)
