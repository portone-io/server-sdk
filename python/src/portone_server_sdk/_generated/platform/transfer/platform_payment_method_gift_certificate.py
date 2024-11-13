from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPaymentMethodGiftCertificate:
    """상품권
    """
    pass


def _serialize_platform_payment_method_gift_certificate(obj: PlatformPaymentMethodGiftCertificate) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "GIFT_CERTIFICATE"
    return entity


def _deserialize_platform_payment_method_gift_certificate(obj: Any) -> PlatformPaymentMethodGiftCertificate:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "GIFT_CERTIFICATE":
        raise ValueError(f"{repr(type)} is not 'GIFT_CERTIFICATE'")
    return PlatformPaymentMethodGiftCertificate()
