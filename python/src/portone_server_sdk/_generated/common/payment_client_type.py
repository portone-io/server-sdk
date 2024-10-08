from __future__ import annotations
from typing import Any, Literal, Optional

PaymentClientType = Literal["SDK_MOBILE", "SDK_PC", "API"]
"""결제가 발생한 클라이언트 환경
"""


def _serialize_payment_client_type(obj: PaymentClientType) -> Any:
    return obj


def _deserialize_payment_client_type(obj: Any) -> PaymentClientType:
    if obj not in ["SDK_MOBILE", "SDK_PC", "API"]:
        raise ValueError(f"{repr(obj)} is not PaymentClientType")
    return obj
