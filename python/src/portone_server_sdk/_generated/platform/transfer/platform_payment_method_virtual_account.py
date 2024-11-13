from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPaymentMethodVirtualAccount:
    """가상계좌
    """
    pass


def _serialize_platform_payment_method_virtual_account(obj: PlatformPaymentMethodVirtualAccount) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "VIRTUAL_ACCOUNT"
    return entity


def _deserialize_platform_payment_method_virtual_account(obj: Any) -> PlatformPaymentMethodVirtualAccount:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "VIRTUAL_ACCOUNT":
        raise ValueError(f"{repr(type)} is not 'VIRTUAL_ACCOUNT'")
    return PlatformPaymentMethodVirtualAccount()
