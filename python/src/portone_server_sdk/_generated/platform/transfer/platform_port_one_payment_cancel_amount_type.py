from __future__ import annotations
from typing import Any, Literal, Optional

PlatformPortOnePaymentCancelAmountType = Literal["SUPPLY_WITH_VAT", "TAX_FREE"]
"""금액 타입
"""


def _serialize_platform_port_one_payment_cancel_amount_type(obj: PlatformPortOnePaymentCancelAmountType) -> Any:
    return obj


def _deserialize_platform_port_one_payment_cancel_amount_type(obj: Any) -> PlatformPortOnePaymentCancelAmountType:
    if obj not in ["SUPPLY_WITH_VAT", "TAX_FREE"]:
        raise ValueError(f"{repr(obj)} is not PlatformPortOnePaymentCancelAmountType")
    return obj
