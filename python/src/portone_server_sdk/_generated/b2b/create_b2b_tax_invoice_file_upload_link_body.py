from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CreateB2bTaxInvoiceFileUploadLinkBody:
    """세금계산서 파일 업로드 링크 생성
    """
    file_name: str
    """파일 이름
    """


def _serialize_create_b2b_tax_invoice_file_upload_link_body(obj: CreateB2bTaxInvoiceFileUploadLinkBody) -> Any:
    entity = {}
    entity["fileName"] = obj.file_name
    return entity


def _deserialize_create_b2b_tax_invoice_file_upload_link_body(obj: Any) -> CreateB2bTaxInvoiceFileUploadLinkBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "fileName" not in obj:
        raise KeyError(f"'fileName' is not in {obj}")
    file_name = obj["fileName"]
    if not isinstance(file_name, str):
        raise ValueError(f"{repr(file_name)} is not str")
    return CreateB2bTaxInvoiceFileUploadLinkBody(file_name)
