from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CancelB2bTaxInvoiceRequestBody:
    """세금계산서 역발행 요청 취소 정보
    """
    memo: Optional[str]
    """메모
    """


def _serialize_cancel_b2b_tax_invoice_request_body(obj: CancelB2bTaxInvoiceRequestBody) -> Any:
    entity = {}
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_cancel_b2b_tax_invoice_request_body(obj: Any) -> CancelB2bTaxInvoiceRequestBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return CancelB2bTaxInvoiceRequestBody(memo)
