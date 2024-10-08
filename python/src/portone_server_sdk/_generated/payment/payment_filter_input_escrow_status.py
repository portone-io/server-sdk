from __future__ import annotations
from typing import Any, Literal, Optional

PaymentFilterInputEscrowStatus = Literal["REGISTERED", "DELIVERED", "CONFIRMED", "REJECTED", "CANCELLED", "REJECT_CONFIRMED"]
"""에스크로 상태
"""


def _serialize_payment_filter_input_escrow_status(obj: PaymentFilterInputEscrowStatus) -> Any:
    return obj


def _deserialize_payment_filter_input_escrow_status(obj: Any) -> PaymentFilterInputEscrowStatus:
    if obj not in ["REGISTERED", "DELIVERED", "CONFIRMED", "REJECTED", "CANCELLED", "REJECT_CONFIRMED"]:
        raise ValueError(f"{repr(obj)} is not PaymentFilterInputEscrowStatus")
    return obj
