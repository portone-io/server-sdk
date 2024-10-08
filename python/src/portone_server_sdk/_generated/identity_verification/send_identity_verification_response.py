from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class SendIdentityVerificationResponse:
    """본인인증 요청 전송 성공 응답
    """
    pass


def _serialize_send_identity_verification_response(obj: SendIdentityVerificationResponse) -> Any:
    entity = {}
    return entity


def _deserialize_send_identity_verification_response(obj: Any) -> SendIdentityVerificationResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return SendIdentityVerificationResponse()
