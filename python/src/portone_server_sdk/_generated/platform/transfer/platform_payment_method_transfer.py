from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPaymentMethodTransfer:
    """계좌이체
    """
    type: Literal["TRANSFER"] = field(repr=False)


def _serialize_platform_payment_method_transfer(obj: PlatformPaymentMethodTransfer) -> Any:
    entity = {}
    entity["type"] = obj.type
    return entity


def _deserialize_platform_payment_method_transfer(obj: Any) -> PlatformPaymentMethodTransfer:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "TRANSFER":
        raise ValueError(f"{repr(type)} is not 'TRANSFER'")
    return PlatformPaymentMethodTransfer(type)
