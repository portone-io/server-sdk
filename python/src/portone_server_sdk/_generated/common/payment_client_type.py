from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentClientType = Union[Literal["SDK_MOBILE", "SDK_PC", "API"], str]
"""결제가 발생한 클라이언트 환경
"""


def _serialize_payment_client_type(obj: PaymentClientType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_client_type(obj: Any) -> PaymentClientType:
    return obj
