from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCounterpartyOngoingTaxInvoiceExistsError:
    """연동된 거래처에 진행 중인 세금계산서가 있는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_counterparty_ongoing_tax_invoice_exists_error(obj: PlatformCounterpartyOngoingTaxInvoiceExistsError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_COUNTERPARTY_ONGOING_TAX_INVOICE_EXISTS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_counterparty_ongoing_tax_invoice_exists_error(obj: Any) -> PlatformCounterpartyOngoingTaxInvoiceExistsError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_COUNTERPARTY_ONGOING_TAX_INVOICE_EXISTS":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_COUNTERPARTY_ONGOING_TAX_INVOICE_EXISTS'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformCounterpartyOngoingTaxInvoiceExistsError(message)
