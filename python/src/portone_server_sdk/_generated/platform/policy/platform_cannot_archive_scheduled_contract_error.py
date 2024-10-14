from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCannotArchiveScheduledContractError:
    """예약된 업데이트가 있는 계약을 보관하려고 하는 경우
    """
    type: Literal["PLATFORM_CANNOT_ARCHIVE_SCHEDULED_CONTRACT"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_cannot_archive_scheduled_contract_error(obj: PlatformCannotArchiveScheduledContractError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_CONTRACT"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cannot_archive_scheduled_contract_error(obj: Any) -> PlatformCannotArchiveScheduledContractError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_CONTRACT":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_CANNOT_ARCHIVE_SCHEDULED_CONTRACT'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformCannotArchiveScheduledContractError(type, message)
