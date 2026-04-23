from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentwallDeliveryType = Union[Literal["DIGITAL", "PHYSICAL"], str]
"""페이먼트월 배송 유형
"""


def _serialize_paymentwall_delivery_type(obj: PaymentwallDeliveryType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_paymentwall_delivery_type(obj: Any) -> PaymentwallDeliveryType:
    return obj
