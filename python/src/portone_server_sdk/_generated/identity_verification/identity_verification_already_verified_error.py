from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class IdentityVerificationAlreadyVerifiedError:
    """본인인증 건이 이미 인증 완료된 상태인 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_identity_verification_already_verified_error(obj: IdentityVerificationAlreadyVerifiedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "IDENTITY_VERIFICATION_ALREADY_VERIFIED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_identity_verification_already_verified_error(obj: Any) -> IdentityVerificationAlreadyVerifiedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
        raise ValueError(f"{repr(type)} is not 'IDENTITY_VERIFICATION_ALREADY_VERIFIED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return IdentityVerificationAlreadyVerifiedError(message)
