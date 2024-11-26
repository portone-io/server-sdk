from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentWebhookPaymentStatus = Union[Literal["READY", "VIRTUAL_ACCOUNT_ISSUED", "PAID", "FAILED", "PARTIAL_CANCELLED", "CANCELLED", "PAY_PENDING"], str]
"""웹훅 발송 시 결제 건 상태
"""


def _serialize_payment_webhook_payment_status(obj: PaymentWebhookPaymentStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_webhook_payment_status(obj: Any) -> PaymentWebhookPaymentStatus:
    return obj
