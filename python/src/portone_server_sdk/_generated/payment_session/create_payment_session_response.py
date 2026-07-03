from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CreatePaymentSessionResponse:
    """결제 세션 생성 성공 응답
    """
    session_id: str
    """세션 아이디
    """
    url: str
    """호스티드 체크아웃 페이지 URL
    """
    expires_at: str
    """만료 시각
    (RFC 3339 date-time)
    """


def _serialize_create_payment_session_response(obj: CreatePaymentSessionResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["sessionId"] = obj.session_id
    entity["url"] = obj.url
    entity["expiresAt"] = obj.expires_at
    return entity


def _deserialize_create_payment_session_response(obj: Any) -> CreatePaymentSessionResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "sessionId" not in obj:
        raise KeyError(f"'sessionId' is not in {obj}")
    session_id = obj["sessionId"]
    if not isinstance(session_id, str):
        raise ValueError(f"{repr(session_id)} is not str")
    if "url" not in obj:
        raise KeyError(f"'url' is not in {obj}")
    url = obj["url"]
    if not isinstance(url, str):
        raise ValueError(f"{repr(url)} is not str")
    if "expiresAt" not in obj:
        raise KeyError(f"'expiresAt' is not in {obj}")
    expires_at = obj["expiresAt"]
    if not isinstance(expires_at, str):
        raise ValueError(f"{repr(expires_at)} is not str")
    return CreatePaymentSessionResponse(session_id, url, expires_at)
