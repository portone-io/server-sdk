from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError:
    """취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error(obj: CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "CANCEL_TAX_FREE_AMOUNT_EXCEEDS_CANCELLABLE_TAX_FREE_AMOUNT"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error(obj: Any) -> CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "CANCEL_TAX_FREE_AMOUNT_EXCEEDS_CANCELLABLE_TAX_FREE_AMOUNT":
        raise ValueError(f"{repr(type)} is not 'CANCEL_TAX_FREE_AMOUNT_EXCEEDS_CANCELLABLE_TAX_FREE_AMOUNT'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError(message)
