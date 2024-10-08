from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.b2b_tax_invoice_document_key_type import B2bTaxInvoiceDocumentKeyType, _deserialize_b2b_tax_invoice_document_key_type, _serialize_b2b_tax_invoice_document_key_type

@dataclass
class CancelB2bTaxInvoiceIssuanceBody:
    """세금계산서 역발행 취소 정보
    """
    brn: str
    """사업자등록번호
    """
    document_key: str
    """세금계산서 문서 번호
    """
    document_key_type: Optional[B2bTaxInvoiceDocumentKeyType]
    """문서 번호 유형

    기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
    """
    memo: Optional[str]
    """메모
    """


def _serialize_cancel_b2b_tax_invoice_issuance_body(obj: CancelB2bTaxInvoiceIssuanceBody) -> Any:
    entity = {}
    entity["brn"] = obj.brn
    entity["documentKey"] = obj.document_key
    if obj.document_key_type is not None:
        entity["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(obj.document_key_type)
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_cancel_b2b_tax_invoice_issuance_body(obj: Any) -> CancelB2bTaxInvoiceIssuanceBody:
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
    if "documentKeyType" in obj:
        document_key_type = obj["documentKeyType"]
        document_key_type = _deserialize_b2b_tax_invoice_document_key_type(document_key_type)
    else:
        document_key_type = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return CancelB2bTaxInvoiceIssuanceBody(brn, document_key, document_key_type, memo)
