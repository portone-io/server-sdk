from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformDiscountSharePolicyScheduleAlreadyExistsError:
    message: Optional[str] = field(default=None)


def _serialize_platform_discount_share_policy_schedule_already_exists_error(obj: PlatformDiscountSharePolicyScheduleAlreadyExistsError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_DISCOUNT_SHARE_POLICY_SCHEDULE_ALREADY_EXISTS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_discount_share_policy_schedule_already_exists_error(obj: Any) -> PlatformDiscountSharePolicyScheduleAlreadyExistsError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_DISCOUNT_SHARE_POLICY_SCHEDULE_ALREADY_EXISTS":
        raise ValueError("Expected 'PLATFORM_DISCOUNT_SHARE_POLICY_SCHEDULE_ALREADY_EXISTS' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformDiscountSharePolicyScheduleAlreadyExistsError(message)
