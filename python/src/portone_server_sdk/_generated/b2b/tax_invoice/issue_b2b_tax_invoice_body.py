from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class IssueB2bTaxInvoiceBody:
    """세금계산서 발행 승인 정보
    """
    memo: Optional[str]
    """메모
    """
    email_subject: Optional[str]
    """이메일 제목
    """


def _serialize_issue_b2b_tax_invoice_body(obj: IssueB2bTaxInvoiceBody) -> Any:
    entity = {}
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.email_subject is not None:
        entity["emailSubject"] = obj.email_subject
    return entity


def _deserialize_issue_b2b_tax_invoice_body(obj: Any) -> IssueB2bTaxInvoiceBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    if "emailSubject" in obj:
        email_subject = obj["emailSubject"]
        if not isinstance(email_subject, str):
            raise ValueError(f"{repr(email_subject)} is not str")
    else:
        email_subject = None
    return IssueB2bTaxInvoiceBody(memo, email_subject)
