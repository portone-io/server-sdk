from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bTaxInvoiceNotDraftedStatusError:
    """세금계산서가 임시저장 완료 상태가 아닌 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_tax_invoice_not_drafted_status_error(obj: B2bTaxInvoiceNotDraftedStatusError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_TAX_INVOICE_NOT_DRAFTED_STATUS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_tax_invoice_not_drafted_status_error(obj: Any) -> B2bTaxInvoiceNotDraftedStatusError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_TAX_INVOICE_NOT_DRAFTED_STATUS":
        raise ValueError(f"{repr(type)} is not 'B2B_TAX_INVOICE_NOT_DRAFTED_STATUS'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bTaxInvoiceNotDraftedStatusError(message)
