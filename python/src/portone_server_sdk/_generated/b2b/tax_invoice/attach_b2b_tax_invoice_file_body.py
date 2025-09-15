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
        raise ValueError(f"{repr(obj)} is not dict")
    if "fileId" not in obj:
        raise KeyError(f"'fileId' is not in {obj}")
    file_id = obj["fileId"]
    if not isinstance(file_id, str):
        raise ValueError(f"{repr(file_id)} is not str")
    return AttachB2bTaxInvoiceFileBody(file_id)
