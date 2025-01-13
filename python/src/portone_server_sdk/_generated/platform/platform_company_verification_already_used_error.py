from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCompanyVerificationAlreadyUsedError:
    """파트너 사업자 검증 아이디를 이미 사용한 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_company_verification_already_used_error(obj: PlatformCompanyVerificationAlreadyUsedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_COMPANY_VERIFICATION_ALREADY_USED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_company_verification_already_used_error(obj: Any) -> PlatformCompanyVerificationAlreadyUsedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_COMPANY_VERIFICATION_ALREADY_USED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_COMPANY_VERIFICATION_ALREADY_USED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformCompanyVerificationAlreadyUsedError(message)
