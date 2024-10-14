from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class CashReceiptNotFoundError:
    """현금영수증이 존재하지 않는 경우
    """
    type: Literal["CASH_RECEIPT_NOT_FOUND"] = field(repr=False)
    message: Optional[str]


def _serialize_cash_receipt_not_found_error(obj: CashReceiptNotFoundError) -> Any:
    entity = {}
    entity["type"] = "CASH_RECEIPT_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_cash_receipt_not_found_error(obj: Any) -> CashReceiptNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "CASH_RECEIPT_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'CASH_RECEIPT_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return CashReceiptNotFoundError(type, message)
