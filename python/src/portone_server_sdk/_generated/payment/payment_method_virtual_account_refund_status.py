from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentMethodVirtualAccountRefundStatus = Union[Literal["PENDING", "PARTIAL_REFUND_FAILED", "FAILED", "COMPLETED"], str]
"""가상계좌 환불 상태
"""


def _serialize_payment_method_virtual_account_refund_status(obj: PaymentMethodVirtualAccountRefundStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_method_virtual_account_refund_status(obj: Any) -> PaymentMethodVirtualAccountRefundStatus:
    return obj
