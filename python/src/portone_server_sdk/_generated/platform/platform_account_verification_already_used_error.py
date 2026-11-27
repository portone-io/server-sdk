from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformAccountVerificationAlreadyUsedError:
    """파트너 계좌 검증 아이디를 이미 사용한 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_account_verification_already_used_error(obj: PlatformAccountVerificationAlreadyUsedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_account_verification_already_used_error(obj: Any) -> PlatformAccountVerificationAlreadyUsedError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED":
        raise ValueError("Expected 'PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformAccountVerificationAlreadyUsedError(message)
