from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_key_type import B2bTaxInvoiceKeyType, _deserialize_b2b_tax_invoice_key_type, _serialize_b2b_tax_invoice_key_type
from ...b2b.tax_invoice.b2b_tax_invoice_modification_type import B2bTaxInvoiceModificationType, _deserialize_b2b_tax_invoice_modification_type, _serialize_b2b_tax_invoice_modification_type

@dataclass
class B2bTaxInvoiceModificationCreateBody:
    """수정 세금계산서 생성 입력 정보
    """
    type: B2bTaxInvoiceModificationType
    """수정 사유
    """
    tax_invoice_key: str
    """세금계산서 문서 번호
    """
    brn: Optional[str] = field(default=None)
    """사업자등록번호

    taxInvoiceKeyType이 TAX_INVOICE_ID가 아닌 경우 필수 값입니다.
    """
    tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = field(default=None)
    """문서 번호 유형

    기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
    """


def _serialize_b2b_tax_invoice_modification_create_body(obj: B2bTaxInvoiceModificationCreateBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = _serialize_b2b_tax_invoice_modification_type(obj.type)
    entity["taxInvoiceKey"] = obj.tax_invoice_key
    if obj.brn is not None:
        entity["brn"] = obj.brn
    if obj.tax_invoice_key_type is not None:
        entity["taxInvoiceKeyType"] = _serialize_b2b_tax_invoice_key_type(obj.tax_invoice_key_type)
    return entity


def _deserialize_b2b_tax_invoice_modification_create_body(obj: Any) -> B2bTaxInvoiceModificationCreateBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    type = _deserialize_b2b_tax_invoice_modification_type(type)
    if "taxInvoiceKey" not in obj:
        raise KeyError(f"'taxInvoiceKey' is not in {obj}")
    tax_invoice_key = obj["taxInvoiceKey"]
    if not isinstance(tax_invoice_key, str):
        raise ValueError(f"{repr(tax_invoice_key)} is not str")
    if "brn" in obj:
        brn = obj["brn"]
        if not isinstance(brn, str):
            raise ValueError(f"{repr(brn)} is not str")
    else:
        brn = None
    if "taxInvoiceKeyType" in obj:
        tax_invoice_key_type = obj["taxInvoiceKeyType"]
        tax_invoice_key_type = _deserialize_b2b_tax_invoice_key_type(tax_invoice_key_type)
    else:
        tax_invoice_key_type = None
    return B2bTaxInvoiceModificationCreateBody(type, tax_invoice_key, brn, tax_invoice_key_type)
