from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformOngoingTaxInvoiceExistsError:
    """진행 중인 세금계산서가 존재하는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_ongoing_tax_invoice_exists_error(obj: PlatformOngoingTaxInvoiceExistsError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_ONGOING_TAX_INVOICE_EXISTS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_ongoing_tax_invoice_exists_error(obj: Any) -> PlatformOngoingTaxInvoiceExistsError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_ONGOING_TAX_INVOICE_EXISTS":
        raise ValueError("Expected 'PLATFORM_ONGOING_TAX_INVOICE_EXISTS' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformOngoingTaxInvoiceExistsError(message)
