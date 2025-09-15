from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_attachment import B2bTaxInvoiceAttachment, _deserialize_b2b_tax_invoice_attachment, _serialize_b2b_tax_invoice_attachment

@dataclass
class GetB2bTaxInvoiceAttachmentsResponse:
    """세금계산서 첨부파일 목록 조회 성공 응답
    """
    attachments: list[B2bTaxInvoiceAttachment]
    """첨부파일 목록
    """


def _serialize_get_b2b_tax_invoice_attachments_response(obj: GetB2bTaxInvoiceAttachmentsResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["attachments"] = list(map(_serialize_b2b_tax_invoice_attachment, obj.attachments))
    return entity


def _deserialize_get_b2b_tax_invoice_attachments_response(obj: Any) -> GetB2bTaxInvoiceAttachmentsResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "attachments" not in obj:
        raise KeyError(f"'attachments' is not in {obj}")
    attachments = obj["attachments"]
    if not isinstance(attachments, list):
        raise ValueError(f"{repr(attachments)} is not list")
    for i, item in enumerate(attachments):
        item = _deserialize_b2b_tax_invoice_attachment(item)
        attachments[i] = item
    return GetB2bTaxInvoiceAttachmentsResponse(attachments)
