from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformAdditionalFeePolicyScheduleAlreadyExistsError:
    message: Optional[str] = field(default=None)


def _serialize_platform_additional_fee_policy_schedule_already_exists_error(obj: PlatformAdditionalFeePolicyScheduleAlreadyExistsError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_ADDITIONAL_FEE_POLICY_SCHEDULE_ALREADY_EXISTS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_additional_fee_policy_schedule_already_exists_error(obj: Any) -> PlatformAdditionalFeePolicyScheduleAlreadyExistsError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_ADDITIONAL_FEE_POLICY_SCHEDULE_ALREADY_EXISTS":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_ADDITIONAL_FEE_POLICY_SCHEDULE_ALREADY_EXISTS'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformAdditionalFeePolicyScheduleAlreadyExistsError(message)
