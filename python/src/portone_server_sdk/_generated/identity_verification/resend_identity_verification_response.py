from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ResendIdentityVerificationResponse:
    """본인인증 요청 재전송 성공 응답
    """
    pass


def _serialize_resend_identity_verification_response(obj: ResendIdentityVerificationResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_resend_identity_verification_response(obj: Any) -> ResendIdentityVerificationResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return ResendIdentityVerificationResponse()
