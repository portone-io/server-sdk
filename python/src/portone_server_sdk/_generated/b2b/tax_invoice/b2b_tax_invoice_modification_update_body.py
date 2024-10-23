from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_modification_type import B2bTaxInvoiceModificationType, _deserialize_b2b_tax_invoice_modification_type, _serialize_b2b_tax_invoice_modification_type

@dataclass
class B2bTaxInvoiceModificationUpdateBody:
    """임시 저장된 수정 세금계산서 업데이트 입력 정보
    """
    type: B2bTaxInvoiceModificationType
    """수정 사유
    """


def _serialize_b2b_tax_invoice_modification_update_body(obj: B2bTaxInvoiceModificationUpdateBody) -> Any:
    entity = {}
    entity["type"] = _serialize_b2b_tax_invoice_modification_type(obj.type)
    return entity


def _deserialize_b2b_tax_invoice_modification_update_body(obj: Any) -> B2bTaxInvoiceModificationUpdateBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    type = _deserialize_b2b_tax_invoice_modification_type(type)
    return B2bTaxInvoiceModificationUpdateBody(type)
