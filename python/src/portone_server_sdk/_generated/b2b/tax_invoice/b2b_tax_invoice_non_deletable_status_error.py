from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bTaxInvoiceNonDeletableStatusError:
    """세금계산서가 삭제 가능한 상태가 아닌 경우

    삭제 가능한 상태는 `DRAFTED`, `ISSUE_REFUSED`, `REQUEST_CANCELLED_BY_RECIPIENT`, `ISSUE_CANCELLED_BY_SUPPLIER`, `SENDING_FAILED` 입니다.
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_tax_invoice_non_deletable_status_error(obj: B2bTaxInvoiceNonDeletableStatusError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_TAX_INVOICE_NON_DELETABLE_STATUS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_tax_invoice_non_deletable_status_error(obj: Any) -> B2bTaxInvoiceNonDeletableStatusError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_TAX_INVOICE_NON_DELETABLE_STATUS":
        raise ValueError(f"{repr(type)} is not 'B2B_TAX_INVOICE_NON_DELETABLE_STATUS'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bTaxInvoiceNonDeletableStatusError(message)
