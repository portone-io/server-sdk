from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CreateB2bTaxInvoiceFileUploadLinkResponse:
    """세금계산서 파일 업로드 링크 생성 성공 응답
    """
    file_id: str
    """파일 아이디
    """
    url: str
    """파일 업로드 링크
    """


def _serialize_create_b2b_tax_invoice_file_upload_link_response(obj: CreateB2bTaxInvoiceFileUploadLinkResponse) -> Any:
    entity = {}
    entity["fileId"] = obj.file_id
    entity["url"] = obj.url
    return entity


def _deserialize_create_b2b_tax_invoice_file_upload_link_response(obj: Any) -> CreateB2bTaxInvoiceFileUploadLinkResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "fileId" not in obj:
        raise KeyError(f"'fileId' is not in {obj}")
    file_id = obj["fileId"]
    if not isinstance(file_id, str):
        raise ValueError(f"{repr(file_id)} is not str")
    if "url" not in obj:
        raise KeyError(f"'url' is not in {obj}")
    url = obj["url"]
    if not isinstance(url, str):
        raise ValueError(f"{repr(url)} is not str")
    return CreateB2bTaxInvoiceFileUploadLinkResponse(file_id, url)
