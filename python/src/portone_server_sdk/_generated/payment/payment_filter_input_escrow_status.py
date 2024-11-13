from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentFilterInputEscrowStatus = Union[Literal["REGISTERED", "DELIVERED", "CONFIRMED", "REJECTED", "CANCELLED", "REJECT_CONFIRMED"], str]
"""에스크로 상태
"""


def _serialize_payment_filter_input_escrow_status(obj: PaymentFilterInputEscrowStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_filter_input_escrow_status(obj: Any) -> PaymentFilterInputEscrowStatus:
    return obj
