from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentMethodMobile:
    """모바일 상세 정보
    """
    phone_number: Optional[str] = field(default=None)
    """전화번호
    """


def _serialize_payment_method_mobile(obj: PaymentMethodMobile) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PaymentMethodMobile"
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    return entity


def _deserialize_payment_method_mobile(obj: Any) -> PaymentMethodMobile:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PaymentMethodMobile":
        raise ValueError("Expected 'PaymentMethodMobile' for type")
    if "phoneNumber" in obj:
        phone_number = obj["phoneNumber"]
        if not isinstance(phone_number, str):
            raise ValueError("Expected str for phone_number")
    else:
        phone_number = None
    return PaymentMethodMobile(phone_number)
