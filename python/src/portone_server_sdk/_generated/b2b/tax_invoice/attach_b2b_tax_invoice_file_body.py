from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class AttachB2bTaxInvoiceFileBody:
    """세금계산서 파일 첨부 정보
    """
    file_id: str
    """파일 아이디
    """


def _serialize_attach_b2b_tax_invoice_file_body(obj: AttachB2bTaxInvoiceFileBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["fileId"] = obj.file_id
    return entity


def _deserialize_attach_b2b_tax_invoice_file_body(obj: Any) -> AttachB2bTaxInvoiceFileBody:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "fileId" not in obj:
        raise KeyError("Missing required field 'fileId'")
    file_id = obj["fileId"]
    if not isinstance(file_id, str):
        raise ValueError("Expected str for file_id")
    return AttachB2bTaxInvoiceFileBody(file_id)
