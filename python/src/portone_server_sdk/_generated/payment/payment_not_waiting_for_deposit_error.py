from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentNotWaitingForDepositError:
    """결제 건이 입금 대기 상태가 아닌 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_payment_not_waiting_for_deposit_error(obj: PaymentNotWaitingForDepositError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PAYMENT_NOT_WAITING_FOR_DEPOSIT"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_payment_not_waiting_for_deposit_error(obj: Any) -> PaymentNotWaitingForDepositError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PAYMENT_NOT_WAITING_FOR_DEPOSIT":
        raise ValueError(f"{repr(type)} is not 'PAYMENT_NOT_WAITING_FOR_DEPOSIT'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PaymentNotWaitingForDepositError(message)
