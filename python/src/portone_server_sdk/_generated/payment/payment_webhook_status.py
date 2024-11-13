from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentWebhookStatus = Union[Literal["SUCCEEDED", "FAILED_NOT_OK_RESPONSE", "FAILED_UNEXPECTED_ERROR"], str]
"""웹훅 전송 상태
"""


def _serialize_payment_webhook_status(obj: PaymentWebhookStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_webhook_status(obj: Any) -> PaymentWebhookStatus:
    return obj
