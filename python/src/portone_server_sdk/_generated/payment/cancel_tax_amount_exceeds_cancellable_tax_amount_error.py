from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class CancelTaxAmountExceedsCancellableTaxAmountError:
    """취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우
    """
    type: Literal["CANCEL_TAX_AMOUNT_EXCEEDS_CANCELLABLE_TAX_AMOUNT"] = field(repr=False)
    message: Optional[str]


def _serialize_cancel_tax_amount_exceeds_cancellable_tax_amount_error(obj: CancelTaxAmountExceedsCancellableTaxAmountError) -> Any:
    entity = {}
    entity["type"] = obj.type
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_cancel_tax_amount_exceeds_cancellable_tax_amount_error(obj: Any) -> CancelTaxAmountExceedsCancellableTaxAmountError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "CANCEL_TAX_AMOUNT_EXCEEDS_CANCELLABLE_TAX_AMOUNT":
        raise ValueError(f"{repr(type)} is not 'CANCEL_TAX_AMOUNT_EXCEEDS_CANCELLABLE_TAX_AMOUNT'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return CancelTaxAmountExceedsCancellableTaxAmountError(type, message)
