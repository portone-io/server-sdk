from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformAdditionalFeePolicyNotFoundError:
    message: Optional[str] = field(default=None)


def _serialize_platform_additional_fee_policy_not_found_error(obj: PlatformAdditionalFeePolicyNotFoundError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_additional_fee_policy_not_found_error(obj: Any) -> PlatformAdditionalFeePolicyNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformAdditionalFeePolicyNotFoundError(message)
