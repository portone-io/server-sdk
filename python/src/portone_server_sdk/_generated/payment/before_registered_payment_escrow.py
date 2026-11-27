from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class BeforeRegisteredPaymentEscrow:
    """배송 정보 등록 전
    """
    pass
    """에스크로 상태
    """


def _serialize_before_registered_payment_escrow(obj: BeforeRegisteredPaymentEscrow) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["status"] = "BEFORE_REGISTERED"
    return entity


def _deserialize_before_registered_payment_escrow(obj: Any) -> BeforeRegisteredPaymentEscrow:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    if status != "BEFORE_REGISTERED":
        raise ValueError("Expected 'BEFORE_REGISTERED' for status")
    return BeforeRegisteredPaymentEscrow()
