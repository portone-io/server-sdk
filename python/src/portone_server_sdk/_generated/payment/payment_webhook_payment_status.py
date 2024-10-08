from __future__ import annotations
from typing import Any, Literal, Optional

PaymentWebhookPaymentStatus = Literal["READY", "VIRTUAL_ACCOUNT_ISSUED", "PAID", "FAILED", "PARTIAL_CANCELLED", "CANCELLED", "PAY_PENDING"]
"""웹훅 발송 시 결제 건 상태
"""


def _serialize_payment_webhook_payment_status(obj: PaymentWebhookPaymentStatus) -> Any:
    return obj


def _deserialize_payment_webhook_payment_status(obj: Any) -> PaymentWebhookPaymentStatus:
    if obj not in ["READY", "VIRTUAL_ACCOUNT_ISSUED", "PAID", "FAILED", "PARTIAL_CANCELLED", "CANCELLED", "PAY_PENDING"]:
        raise ValueError(f"{repr(obj)} is not PaymentWebhookPaymentStatus")
    return obj
