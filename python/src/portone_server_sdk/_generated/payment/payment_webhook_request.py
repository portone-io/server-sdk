from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentWebhookRequest:
    """웹훅 요청 정보
    """
    body: str
    """요청 본문
    """
    header: Optional[str]
    """요청 헤더
    """
    requested_at: Optional[str]
    """요청 시점
    (RFC 3339 date-time)
    """


def _serialize_payment_webhook_request(obj: PaymentWebhookRequest) -> Any:
    entity = {}
    entity["body"] = obj.body
    if obj.header is not None:
        entity["header"] = obj.header
    if obj.requested_at is not None:
        entity["requestedAt"] = obj.requested_at
    return entity


def _deserialize_payment_webhook_request(obj: Any) -> PaymentWebhookRequest:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "body" not in obj:
        raise KeyError(f"'body' is not in {obj}")
    body = obj["body"]
    if not isinstance(body, str):
        raise ValueError(f"{repr(body)} is not str")
    if "header" in obj:
        header = obj["header"]
        if not isinstance(header, str):
            raise ValueError(f"{repr(header)} is not str")
    else:
        header = None
    if "requestedAt" in obj:
        requested_at = obj["requestedAt"]
        if not isinstance(requested_at, str):
            raise ValueError(f"{repr(requested_at)} is not str")
    else:
        requested_at = None
    return PaymentWebhookRequest(body, header, requested_at)
