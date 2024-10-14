from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformAccountVerificationNotFoundError:
    """파트너 계좌 검증 아이디를 찾을 수 없는 경우
    """
    type: Literal["PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_account_verification_not_found_error(obj: PlatformAccountVerificationNotFoundError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_account_verification_not_found_error(obj: Any) -> PlatformAccountVerificationNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformAccountVerificationNotFoundError(type, message)
