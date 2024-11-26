from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class InstantPaymentMethodInputVirtualAccountExpiry:
    """입금 만료 기한

    validHours와 dueDate 둘 중 하나의 필드만 입력합니다.
    """
    valid_hours: Optional[int] = field(default=None)
    """유효 시간

    시간 단위로 입력합니다.
    (int32)
    """
    due_date: Optional[str] = field(default=None)
    """만료 시점
    (RFC 3339 date-time)
    """


def _serialize_instant_payment_method_input_virtual_account_expiry(obj: InstantPaymentMethodInputVirtualAccountExpiry) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.valid_hours is not None:
        entity["validHours"] = obj.valid_hours
    if obj.due_date is not None:
        entity["dueDate"] = obj.due_date
    return entity


def _deserialize_instant_payment_method_input_virtual_account_expiry(obj: Any) -> InstantPaymentMethodInputVirtualAccountExpiry:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "validHours" in obj:
        valid_hours = obj["validHours"]
        if not isinstance(valid_hours, int):
            raise ValueError(f"{repr(valid_hours)} is not int")
    else:
        valid_hours = None
    if "dueDate" in obj:
        due_date = obj["dueDate"]
        if not isinstance(due_date, str):
            raise ValueError(f"{repr(due_date)} is not str")
    else:
        due_date = None
    return InstantPaymentMethodInputVirtualAccountExpiry(valid_hours, due_date)
