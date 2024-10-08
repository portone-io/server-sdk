from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class GetB2bTaxInvoicePdfDownloadUrlResponse:
    """세금계산서 PDF 다운로드 URL 성공 응답
    """
    url: str
    """세금계산서 PDF 다운로드 URL
    """


def _serialize_get_b2b_tax_invoice_pdf_download_url_response(obj: GetB2bTaxInvoicePdfDownloadUrlResponse) -> Any:
    entity = {}
    entity["url"] = obj.url
    return entity


def _deserialize_get_b2b_tax_invoice_pdf_download_url_response(obj: Any) -> GetB2bTaxInvoicePdfDownloadUrlResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "url" not in obj:
        raise KeyError(f"'url' is not in {obj}")
    url = obj["url"]
    if not isinstance(url, str):
        raise ValueError(f"{repr(url)} is not str")
    return GetB2bTaxInvoicePdfDownloadUrlResponse(url)
