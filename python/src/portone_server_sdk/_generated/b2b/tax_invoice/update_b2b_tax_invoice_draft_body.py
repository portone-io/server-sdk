from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_input import B2bTaxInvoiceInput, _deserialize_b2b_tax_invoice_input, _serialize_b2b_tax_invoice_input
from ...b2b.tax_invoice.b2b_tax_invoice_key_type import B2bTaxInvoiceKeyType, _deserialize_b2b_tax_invoice_key_type, _serialize_b2b_tax_invoice_key_type

@dataclass
class UpdateB2bTaxInvoiceDraftBody:
    """세금계산서 임시저장 수정 정보
    """
    tax_invoice_key: str
    """세금계산서 문서 번호
    """
    tax_invoice: B2bTaxInvoiceInput
    """세금계산서 임시저장 수정 정보
    """
    brn: Optional[str] = field(default=None)
    """사업자등록번호

    taxInvoiceKeyType이 TAX_INVOICE_ID가 아닌 경우 필수 값입니다.
    """
    tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = field(default=None)
    """문서 번호 유형

    기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
    """
    memo: Optional[str] = field(default=None)
    """메모
    """


def _serialize_update_b2b_tax_invoice_draft_body(obj: UpdateB2bTaxInvoiceDraftBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["taxInvoiceKey"] = obj.tax_invoice_key
    entity["taxInvoice"] = _serialize_b2b_tax_invoice_input(obj.tax_invoice)
    if obj.brn is not None:
        entity["brn"] = obj.brn
    if obj.tax_invoice_key_type is not None:
        entity["taxInvoiceKeyType"] = _serialize_b2b_tax_invoice_key_type(obj.tax_invoice_key_type)
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_update_b2b_tax_invoice_draft_body(obj: Any) -> UpdateB2bTaxInvoiceDraftBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "taxInvoiceKey" not in obj:
        raise KeyError(f"'taxInvoiceKey' is not in {obj}")
    tax_invoice_key = obj["taxInvoiceKey"]
    if not isinstance(tax_invoice_key, str):
        raise ValueError(f"{repr(tax_invoice_key)} is not str")
    if "taxInvoice" not in obj:
        raise KeyError(f"'taxInvoice' is not in {obj}")
    tax_invoice = obj["taxInvoice"]
    tax_invoice = _deserialize_b2b_tax_invoice_input(tax_invoice)
    if "brn" in obj:
        brn = obj["brn"]
        if not isinstance(brn, str):
            raise ValueError(f"{repr(brn)} is not str")
    else:
        brn = None
    if "taxInvoiceKeyType" in obj:
        tax_invoice_key_type = obj["taxInvoiceKeyType"]
        tax_invoice_key_type = _deserialize_b2b_tax_invoice_key_type(tax_invoice_key_type)
    else:
        tax_invoice_key_type = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return UpdateB2bTaxInvoiceDraftBody(tax_invoice_key, tax_invoice, brn, tax_invoice_key_type, memo)
