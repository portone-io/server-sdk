from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPaymentMethodTransferInput:
    pass


def _serialize_platform_payment_method_transfer_input(obj: PlatformPaymentMethodTransferInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_platform_payment_method_transfer_input(obj: Any) -> PlatformPaymentMethodTransferInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return PlatformPaymentMethodTransferInput()
