from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformDiscountSharePolicyNotFoundError:
    message: Optional[str] = field(default=None)


def _serialize_platform_discount_share_policy_not_found_error(obj: PlatformDiscountSharePolicyNotFoundError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_discount_share_policy_not_found_error(obj: Any) -> PlatformDiscountSharePolicyNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformDiscountSharePolicyNotFoundError(message)
