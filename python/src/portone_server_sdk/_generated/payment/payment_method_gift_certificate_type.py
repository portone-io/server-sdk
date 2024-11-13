from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentMethodGiftCertificateType = Union[Literal["BOOKNLIFE", "SMART_MUNSANG", "CULTURELAND", "HAPPYMONEY", "CULTUREGIFT"], str]
"""상품권 종류
"""


def _serialize_payment_method_gift_certificate_type(obj: PaymentMethodGiftCertificateType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_method_gift_certificate_type(obj: Any) -> PaymentMethodGiftCertificateType:
    return obj
