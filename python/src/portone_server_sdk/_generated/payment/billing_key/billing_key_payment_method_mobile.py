from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class BillingKeyPaymentMethodMobile:
    """모바일 정보
    """
    phone_number: Optional[str] = field(default=None)
    """전화번호
    """


def _serialize_billing_key_payment_method_mobile(obj: BillingKeyPaymentMethodMobile) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "BillingKeyPaymentMethodMobile"
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    return entity


def _deserialize_billing_key_payment_method_mobile(obj: Any) -> BillingKeyPaymentMethodMobile:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "BillingKeyPaymentMethodMobile":
        raise ValueError(f"{repr(type)} is not 'BillingKeyPaymentMethodMobile'")
    if "phoneNumber" in obj:
        phone_number = obj["phoneNumber"]
        if not isinstance(phone_number, str):
            raise ValueError(f"{repr(phone_number)} is not str")
    else:
        phone_number = None
    return BillingKeyPaymentMethodMobile(phone_number)
