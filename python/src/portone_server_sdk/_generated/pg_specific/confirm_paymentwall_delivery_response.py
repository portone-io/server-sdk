from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ConfirmPaymentwallDeliveryResponse:
    """페이먼트월 배송 정보 등록 성공 응답
    """
    pass


def _serialize_confirm_paymentwall_delivery_response(obj: ConfirmPaymentwallDeliveryResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_confirm_paymentwall_delivery_response(obj: Any) -> ConfirmPaymentwallDeliveryResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return ConfirmPaymentwallDeliveryResponse()
