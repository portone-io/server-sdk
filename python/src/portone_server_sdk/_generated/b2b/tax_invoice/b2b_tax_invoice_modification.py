from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_modification_type import B2bTaxInvoiceModificationType, _deserialize_b2b_tax_invoice_modification_type, _serialize_b2b_tax_invoice_modification_type

@dataclass
class B2bTaxInvoiceModification:
    """세금 계산서 수정
    """
    type: B2bTaxInvoiceModificationType
    """수정 사유
    """
    original_nts_approval_number: str
    """수정 대상 원본 세금계산서 국세청 승인 번호
    """
    original_tax_invoice_id: str
    """원본 세금계산서 아이디
    """
    root_tax_invoice_id: str
    """최초 원본 세금계산서 아이디
    """


def _serialize_b2b_tax_invoice_modification(obj: B2bTaxInvoiceModification) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = _serialize_b2b_tax_invoice_modification_type(obj.type)
    entity["originalNtsApprovalNumber"] = obj.original_nts_approval_number
    entity["originalTaxInvoiceId"] = obj.original_tax_invoice_id
    entity["rootTaxInvoiceId"] = obj.root_tax_invoice_id
    return entity


def _deserialize_b2b_tax_invoice_modification(obj: Any) -> B2bTaxInvoiceModification:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    type = _deserialize_b2b_tax_invoice_modification_type(type)
    if "originalNtsApprovalNumber" not in obj:
        raise KeyError("Missing required field 'originalNtsApprovalNumber'")
    original_nts_approval_number = obj["originalNtsApprovalNumber"]
    if not isinstance(original_nts_approval_number, str):
        raise ValueError("Expected str for original_nts_approval_number")
    if "originalTaxInvoiceId" not in obj:
        raise KeyError("Missing required field 'originalTaxInvoiceId'")
    original_tax_invoice_id = obj["originalTaxInvoiceId"]
    if not isinstance(original_tax_invoice_id, str):
        raise ValueError("Expected str for original_tax_invoice_id")
    if "rootTaxInvoiceId" not in obj:
        raise KeyError("Missing required field 'rootTaxInvoiceId'")
    root_tax_invoice_id = obj["rootTaxInvoiceId"]
    if not isinstance(root_tax_invoice_id, str):
        raise ValueError("Expected str for root_tax_invoice_id")
    return B2bTaxInvoiceModification(type, original_nts_approval_number, original_tax_invoice_id, root_tax_invoice_id)
