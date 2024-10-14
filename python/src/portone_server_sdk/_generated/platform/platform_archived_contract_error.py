from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformArchivedContractError:
    """보관된 계약을 업데이트하려고 하는 경우
    """
    type: Literal["PLATFORM_ARCHIVED_CONTRACT"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_archived_contract_error(obj: PlatformArchivedContractError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_ARCHIVED_CONTRACT"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_archived_contract_error(obj: Any) -> PlatformArchivedContractError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_ARCHIVED_CONTRACT":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_ARCHIVED_CONTRACT'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformArchivedContractError(type, message)
