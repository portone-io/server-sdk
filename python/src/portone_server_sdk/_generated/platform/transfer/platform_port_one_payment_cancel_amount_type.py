from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformPortOnePaymentCancelAmountType = Union[Literal["SUPPLY_WITH_VAT", "TAX_FREE"], str]
"""금액 타입
"""


def _serialize_platform_port_one_payment_cancel_amount_type(obj: PlatformPortOnePaymentCancelAmountType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_port_one_payment_cancel_amount_type(obj: Any) -> PlatformPortOnePaymentCancelAmountType:
    return obj
