from __future__ import annotations
from typing import Any, Literal, Optional

PaymentWebhookStatus = Literal["SUCCEEDED", "FAILED_NOT_OK_RESPONSE", "FAILED_UNEXPECTED_ERROR"]
"""웹훅 전송 상태
"""


def _serialize_payment_webhook_status(obj: PaymentWebhookStatus) -> Any:
    return obj


def _deserialize_payment_webhook_status(obj: Any) -> PaymentWebhookStatus:
    if obj not in ["SUCCEEDED", "FAILED_NOT_OK_RESPONSE", "FAILED_UNEXPECTED_ERROR"]:
        raise ValueError(f"{repr(obj)} is not PaymentWebhookStatus")
    return obj
