from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPaymentMethodVirtualAccountInput:
    pass


def _serialize_platform_payment_method_virtual_account_input(obj: PlatformPaymentMethodVirtualAccountInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_platform_payment_method_virtual_account_input(obj: Any) -> PlatformPaymentMethodVirtualAccountInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return PlatformPaymentMethodVirtualAccountInput()
