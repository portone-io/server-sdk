from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformMemberCompanyNotConnectableStatusError:
    """파트너 연동 사업자 연동 상태가 연동 가능한 상태가 아닌 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_member_company_not_connectable_status_error(obj: PlatformMemberCompanyNotConnectableStatusError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_MEMBER_COMPANY_NOT_CONNECTABLE_STATUS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_member_company_not_connectable_status_error(obj: Any) -> PlatformMemberCompanyNotConnectableStatusError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_MEMBER_COMPANY_NOT_CONNECTABLE_STATUS":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_MEMBER_COMPANY_NOT_CONNECTABLE_STATUS'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformMemberCompanyNotConnectableStatusError(message)
