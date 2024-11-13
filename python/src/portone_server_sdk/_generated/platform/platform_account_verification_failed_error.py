from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformAccountVerificationFailedError:
    """파트너 계좌 인증이 실패한 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_account_verification_failed_error(obj: PlatformAccountVerificationFailedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_ACCOUNT_VERIFICATION_FAILED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_account_verification_failed_error(obj: Any) -> PlatformAccountVerificationFailedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_ACCOUNT_VERIFICATION_FAILED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_ACCOUNT_VERIFICATION_FAILED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformAccountVerificationFailedError(message)
