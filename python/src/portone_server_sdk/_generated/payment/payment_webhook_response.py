from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentWebhookResponse:
    """웹훅 응답 정보
    """
    code: str
    """응답 HTTP 코드
    """
    header: str
    """응답 헤더
    """
    body: str
    """응답 본문
    """
    responded_at: str
    """응답 시점
    (RFC 3339 date-time)
    """


def _serialize_payment_webhook_response(obj: PaymentWebhookResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["code"] = obj.code
    entity["header"] = obj.header
    entity["body"] = obj.body
    entity["respondedAt"] = obj.responded_at
    return entity


def _deserialize_payment_webhook_response(obj: Any) -> PaymentWebhookResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "code" not in obj:
        raise KeyError("Missing required field 'code'")
    code = obj["code"]
    if not isinstance(code, str):
        raise ValueError("Expected str for code")
    if "header" not in obj:
        raise KeyError("Missing required field 'header'")
    header = obj["header"]
    if not isinstance(header, str):
        raise ValueError("Expected str for header")
    if "body" not in obj:
        raise KeyError("Missing required field 'body'")
    body = obj["body"]
    if not isinstance(body, str):
        raise ValueError("Expected str for body")
    if "respondedAt" not in obj:
        raise KeyError("Missing required field 'respondedAt'")
    responded_at = obj["respondedAt"]
    if not isinstance(responded_at, str):
        raise ValueError("Expected str for responded_at")
    return PaymentWebhookResponse(code, header, body, responded_at)
