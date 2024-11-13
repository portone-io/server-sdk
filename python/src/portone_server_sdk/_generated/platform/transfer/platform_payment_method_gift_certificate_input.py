from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPaymentMethodGiftCertificateInput:
    pass


def _serialize_platform_payment_method_gift_certificate_input(obj: PlatformPaymentMethodGiftCertificateInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_platform_payment_method_gift_certificate_input(obj: Any) -> PlatformPaymentMethodGiftCertificateInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return PlatformPaymentMethodGiftCertificateInput()
