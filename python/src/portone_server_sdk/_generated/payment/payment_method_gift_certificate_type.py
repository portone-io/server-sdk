from __future__ import annotations
from typing import Any, Literal, Optional

PaymentMethodGiftCertificateType = Literal["BOOKNLIFE", "SMART_MUNSANG", "CULTURELAND", "HAPPYMONEY", "CULTUREGIFT"]
"""상품권 종류
"""


def _serialize_payment_method_gift_certificate_type(obj: PaymentMethodGiftCertificateType) -> Any:
    return obj


def _deserialize_payment_method_gift_certificate_type(obj: Any) -> PaymentMethodGiftCertificateType:
    if obj not in ["BOOKNLIFE", "SMART_MUNSANG", "CULTURELAND", "HAPPYMONEY", "CULTUREGIFT"]:
        raise ValueError(f"{repr(obj)} is not PaymentMethodGiftCertificateType")
    return obj
