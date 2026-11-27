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
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "GIFT_CERTIFICATE":
        raise ValueError("Expected 'GIFT_CERTIFICATE' for type")
    return PlatformPaymentMethodGiftCertificate()
