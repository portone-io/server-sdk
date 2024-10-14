from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformContractScheduleAlreadyExistsError:
    type: Literal["PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_contract_schedule_already_exists_error(obj: PlatformContractScheduleAlreadyExistsError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_contract_schedule_already_exists_error(obj: Any) -> PlatformContractScheduleAlreadyExistsError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformContractScheduleAlreadyExistsError(type, message)
