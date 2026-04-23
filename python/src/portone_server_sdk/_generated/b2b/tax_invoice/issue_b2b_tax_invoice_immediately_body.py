from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_input import B2bTaxInvoiceInput, _deserialize_b2b_tax_invoice_input, _serialize_b2b_tax_invoice_input
from ...b2b.tax_invoice.b2b_tax_invoice_modification_create_body import B2bTaxInvoiceModificationCreateBody, _deserialize_b2b_tax_invoice_modification_create_body, _serialize_b2b_tax_invoice_modification_create_body

@dataclass
class IssueB2bTaxInvoiceImmediatelyBody:
    """세금계산서 즉시 정발행 요청 정보
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
    create_recipient_counterparty: Optional[bool] = field(default=None)
    """공급받는자 거래처 생성 여부

    true인 경우 공급받는자 정보로 거래처를 자동 생성합니다.
    """


def _serialize_issue_b2b_tax_invoice_immediately_body(obj: IssueB2bTaxInvoiceImmediatelyBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["taxInvoice"] = _serialize_b2b_tax_invoice_input(obj.tax_invoice)
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.modification is not None:
        entity["modification"] = _serialize_b2b_tax_invoice_modification_create_body(obj.modification)
    if obj.create_recipient_counterparty is not None:
        entity["createRecipientCounterparty"] = obj.create_recipient_counterparty
    return entity


def _deserialize_issue_b2b_tax_invoice_immediately_body(obj: Any) -> IssueB2bTaxInvoiceImmediatelyBody:
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
    if "createRecipientCounterparty" in obj:
        create_recipient_counterparty = obj["createRecipientCounterparty"]
        if not isinstance(create_recipient_counterparty, bool):
            raise ValueError(f"{repr(create_recipient_counterparty)} is not bool")
    else:
        create_recipient_counterparty = None
    return IssueB2bTaxInvoiceImmediatelyBody(tax_invoice, memo, modification, create_recipient_counterparty)
