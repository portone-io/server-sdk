from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bOriginalTaxInvoiceNotFoundError:
    """원본 세금계산서가 존재하지 않은 경우
    """
    type: Literal["B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_original_tax_invoice_not_found_error(obj: B2bOriginalTaxInvoiceNotFoundError) -> Any:
    entity = {}
    entity["type"] = "B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_original_tax_invoice_not_found_error(obj: Any) -> B2bOriginalTaxInvoiceNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bOriginalTaxInvoiceNotFoundError(type, message)
