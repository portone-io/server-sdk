from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.b2b_tax_invoice_modification_type import B2bTaxInvoiceModificationType, _deserialize_b2b_tax_invoice_modification_type, _serialize_b2b_tax_invoice_modification_type

@dataclass
class B2bModification:
    """세금 계산서 수정
    """
    type: B2bTaxInvoiceModificationType
    """수정 사유
    """
    original_nts_approve_number: str
    """수정 대상 원본 세금계산서 국세청 승인 번호
    """


def _serialize_b2b_modification(obj: B2bModification) -> Any:
    entity = {}
    entity["type"] = _serialize_b2b_tax_invoice_modification_type(obj.type)
    entity["originalNtsApproveNumber"] = obj.original_nts_approve_number
    return entity


def _deserialize_b2b_modification(obj: Any) -> B2bModification:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    type = _deserialize_b2b_tax_invoice_modification_type(type)
    if "originalNtsApproveNumber" not in obj:
        raise KeyError(f"'originalNtsApproveNumber' is not in {obj}")
    original_nts_approve_number = obj["originalNtsApproveNumber"]
    if not isinstance(original_nts_approve_number, str):
        raise ValueError(f"{repr(original_nts_approve_number)} is not str")
    return B2bModification(type, original_nts_approve_number)
