from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPaymentMethodTransfer:
    """계좌이체
    """
    pass


def _serialize_platform_payment_method_transfer(obj: PlatformPaymentMethodTransfer) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "TRANSFER"
    return entity


def _deserialize_platform_payment_method_transfer(obj: Any) -> PlatformPaymentMethodTransfer:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "TRANSFER":
        raise ValueError(f"{repr(type)} is not 'TRANSFER'")
    return PlatformPaymentMethodTransfer()
