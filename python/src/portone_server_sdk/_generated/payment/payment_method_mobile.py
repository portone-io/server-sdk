from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentMethodMobile:
    """모바일 상세 정보
    """
    type: Literal["PaymentMethodMobile"] = field(repr=False)
    phone_number: Optional[str]
    """전화번호
    """


def _serialize_payment_method_mobile(obj: PaymentMethodMobile) -> Any:
    entity = {}
    entity["type"] = "PaymentMethodMobile"
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    return entity


def _deserialize_payment_method_mobile(obj: Any) -> PaymentMethodMobile:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PaymentMethodMobile":
        raise ValueError(f"{repr(type)} is not 'PaymentMethodMobile'")
    if "phoneNumber" in obj:
        phone_number = obj["phoneNumber"]
        if not isinstance(phone_number, str):
            raise ValueError(f"{repr(phone_number)} is not str")
    else:
        phone_number = None
    return PaymentMethodMobile(type, phone_number)
