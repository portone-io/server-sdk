from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.b2b_tax_invoice_document_key_type import B2bTaxInvoiceDocumentKeyType, _deserialize_b2b_tax_invoice_document_key_type, _serialize_b2b_tax_invoice_document_key_type

@dataclass
class AttachB2bTaxInvoiceFileBody:
    """세금계산서 파일 첨부 정보
    """
    brn: str
    """사업자등록번호

    `-` 없이 숫자 10자리로 구성됩니다.
    """
    document_key: str
    """세금계산서 문서 번호
    """
    file_id: str
    """파일 아이디
    """
    document_key_type: Optional[B2bTaxInvoiceDocumentKeyType]
    """문서 번호 유형

    기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
    """


def _serialize_attach_b2b_tax_invoice_file_body(obj: AttachB2bTaxInvoiceFileBody) -> Any:
    entity = {}
    entity["brn"] = obj.brn
    entity["documentKey"] = obj.document_key
    entity["fileId"] = obj.file_id
    if obj.document_key_type is not None:
        entity["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(obj.document_key_type)
    return entity


def _deserialize_attach_b2b_tax_invoice_file_body(obj: Any) -> AttachB2bTaxInvoiceFileBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "brn" not in obj:
        raise KeyError(f"'brn' is not in {obj}")
    brn = obj["brn"]
    if not isinstance(brn, str):
        raise ValueError(f"{repr(brn)} is not str")
    if "documentKey" not in obj:
        raise KeyError(f"'documentKey' is not in {obj}")
    document_key = obj["documentKey"]
    if not isinstance(document_key, str):
        raise ValueError(f"{repr(document_key)} is not str")
    if "fileId" not in obj:
        raise KeyError(f"'fileId' is not in {obj}")
    file_id = obj["fileId"]
    if not isinstance(file_id, str):
        raise ValueError(f"{repr(file_id)} is not str")
    if "documentKeyType" in obj:
        document_key_type = obj["documentKeyType"]
        document_key_type = _deserialize_b2b_tax_invoice_document_key_type(document_key_type)
    else:
        document_key_type = None
    return AttachB2bTaxInvoiceFileBody(brn, document_key, file_id, document_key_type)
