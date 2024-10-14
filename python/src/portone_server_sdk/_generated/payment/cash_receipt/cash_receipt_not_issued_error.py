from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class CashReceiptNotIssuedError:
    """현금영수증이 발급되지 않은 경우
    """
    type: Literal["CASH_RECEIPT_NOT_ISSUED"] = field(repr=False)
    message: Optional[str]


def _serialize_cash_receipt_not_issued_error(obj: CashReceiptNotIssuedError) -> Any:
    entity = {}
    entity["type"] = "CASH_RECEIPT_NOT_ISSUED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_cash_receipt_not_issued_error(obj: Any) -> CashReceiptNotIssuedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "CASH_RECEIPT_NOT_ISSUED":
        raise ValueError(f"{repr(type)} is not 'CASH_RECEIPT_NOT_ISSUED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return CashReceiptNotIssuedError(type, message)
