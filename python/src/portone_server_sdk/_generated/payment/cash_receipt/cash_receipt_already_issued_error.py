from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class CashReceiptAlreadyIssuedError:
    """현금영수증이 이미 발급된 경우
    """
    type: Literal["CASH_RECEIPT_ALREADY_ISSUED"] = field(repr=False)
    message: Optional[str]


def _serialize_cash_receipt_already_issued_error(obj: CashReceiptAlreadyIssuedError) -> Any:
    entity = {}
    entity["type"] = "CASH_RECEIPT_ALREADY_ISSUED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_cash_receipt_already_issued_error(obj: Any) -> CashReceiptAlreadyIssuedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "CASH_RECEIPT_ALREADY_ISSUED":
        raise ValueError(f"{repr(type)} is not 'CASH_RECEIPT_ALREADY_ISSUED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return CashReceiptAlreadyIssuedError(type, message)