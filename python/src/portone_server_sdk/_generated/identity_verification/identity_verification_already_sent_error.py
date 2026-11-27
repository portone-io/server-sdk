from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class IdentityVerificationAlreadySentError:
    """본인인증 건이 이미 API로 요청된 상태인 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_identity_verification_already_sent_error(obj: IdentityVerificationAlreadySentError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "IDENTITY_VERIFICATION_ALREADY_SENT"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_identity_verification_already_sent_error(obj: Any) -> IdentityVerificationAlreadySentError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "IDENTITY_VERIFICATION_ALREADY_SENT":
        raise ValueError("Expected 'IDENTITY_VERIFICATION_ALREADY_SENT' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return IdentityVerificationAlreadySentError(message)
