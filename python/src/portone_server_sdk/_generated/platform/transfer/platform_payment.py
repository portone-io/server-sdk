from __future__ import annotations
from typing import Any, Optional, Union
from ...platform.transfer.platform_external_payment import PlatformExternalPayment, _deserialize_platform_external_payment, _serialize_platform_external_payment
from ...platform.transfer.platform_port_one_payment import PlatformPortOnePayment, _deserialize_platform_port_one_payment, _serialize_platform_port_one_payment

PlatformPayment = Union[PlatformExternalPayment, PlatformPortOnePayment, dict]
"""결제 정보
"""


def _serialize_platform_payment(obj: PlatformPayment) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, PlatformExternalPayment):
        return _serialize_platform_external_payment(obj)
    if isinstance(obj, PlatformPortOnePayment):
        return _serialize_platform_port_one_payment(obj)


def _deserialize_platform_payment(obj: Any) -> PlatformPayment:
    try:
        return _deserialize_platform_external_payment(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_port_one_payment(obj)
    except Exception:
        pass
    return obj
