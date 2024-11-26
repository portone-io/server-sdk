from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.payment_webhook import PaymentWebhook, _deserialize_payment_webhook, _serialize_payment_webhook

@dataclass
class ResendWebhookResponse:
    """웹훅 재발송 응답 정보
    """
    webhook: PaymentWebhook
    """재발송 웹훅 정보
    """


def _serialize_resend_webhook_response(obj: ResendWebhookResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["webhook"] = _serialize_payment_webhook(obj.webhook)
    return entity


def _deserialize_resend_webhook_response(obj: Any) -> ResendWebhookResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "webhook" not in obj:
        raise KeyError(f"'webhook' is not in {obj}")
    webhook = obj["webhook"]
    webhook = _deserialize_payment_webhook(webhook)
    return ResendWebhookResponse(webhook)
