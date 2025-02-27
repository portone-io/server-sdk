from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformMemberCompanyNotConnectedError:
    """파트너가 연동 사업자로 연동 되어있지 않은 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_member_company_not_connected_error(obj: PlatformMemberCompanyNotConnectedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_MEMBER_COMPANY_NOT_CONNECTED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_member_company_not_connected_error(obj: Any) -> PlatformMemberCompanyNotConnectedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_MEMBER_COMPANY_NOT_CONNECTED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_MEMBER_COMPANY_NOT_CONNECTED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformMemberCompanyNotConnectedError(message)
