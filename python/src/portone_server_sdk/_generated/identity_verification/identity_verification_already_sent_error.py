from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class IdentityVerificationAlreadySentError:
    """본인인증 건이 이미 API로 요청된 상태인 경우
    """
    type: Literal["IDENTITY_VERIFICATION_ALREADY_SENT"] = field(repr=False)
    message: Optional[str]


def _serialize_identity_verification_already_sent_error(obj: IdentityVerificationAlreadySentError) -> Any:
    entity = {}
    entity["type"] = "IDENTITY_VERIFICATION_ALREADY_SENT"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_identity_verification_already_sent_error(obj: Any) -> IdentityVerificationAlreadySentError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "IDENTITY_VERIFICATION_ALREADY_SENT":
        raise ValueError(f"{repr(type)} is not 'IDENTITY_VERIFICATION_ALREADY_SENT'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return IdentityVerificationAlreadySentError(type, message)
