from __future__ import annotations
from typing import Any, Literal, Optional

PaymentMethodVirtualAccountRefundStatus = Literal["PENDING", "PARTIAL_REFUND_FAILED", "FAILED", "COMPLETED"]
"""가상계좌 환불 상태
"""


def _serialize_payment_method_virtual_account_refund_status(obj: PaymentMethodVirtualAccountRefundStatus) -> Any:
    return obj


def _deserialize_payment_method_virtual_account_refund_status(obj: Any) -> PaymentMethodVirtualAccountRefundStatus:
    if obj not in ["PENDING", "PARTIAL_REFUND_FAILED", "FAILED", "COMPLETED"]:
        raise ValueError(f"{repr(obj)} is not PaymentMethodVirtualAccountRefundStatus")
    return obj
