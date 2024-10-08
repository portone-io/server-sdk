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
    entity = {}
    entity["code"] = obj.code
    entity["header"] = obj.header
    entity["body"] = obj.body
    entity["respondedAt"] = obj.responded_at
    return entity


def _deserialize_payment_webhook_response(obj: Any) -> PaymentWebhookResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "code" not in obj:
        raise KeyError(f"'code' is not in {obj}")
    code = obj["code"]
    if not isinstance(code, str):
        raise ValueError(f"{repr(code)} is not str")
    if "header" not in obj:
        raise KeyError(f"'header' is not in {obj}")
    header = obj["header"]
    if not isinstance(header, str):
        raise ValueError(f"{repr(header)} is not str")
    if "body" not in obj:
        raise KeyError(f"'body' is not in {obj}")
    body = obj["body"]
    if not isinstance(body, str):
        raise ValueError(f"{repr(body)} is not str")
    if "respondedAt" not in obj:
        raise KeyError(f"'respondedAt' is not in {obj}")
    responded_at = obj["respondedAt"]
    if not isinstance(responded_at, str):
        raise ValueError(f"{repr(responded_at)} is not str")
    return PaymentWebhookResponse(code, header, body, responded_at)
