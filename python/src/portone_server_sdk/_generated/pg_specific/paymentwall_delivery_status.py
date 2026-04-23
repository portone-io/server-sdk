from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentwallDeliveryStatus = Union[Literal["ORDER_PLACED", "ORDER_SHIPPED", "DELIVERED"], str]
"""페이먼트월 배송 상태
"""


def _serialize_paymentwall_delivery_status(obj: PaymentwallDeliveryStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_paymentwall_delivery_status(obj: Any) -> PaymentwallDeliveryStatus:
    return obj
