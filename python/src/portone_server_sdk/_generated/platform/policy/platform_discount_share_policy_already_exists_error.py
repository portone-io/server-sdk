from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformDiscountSharePolicyAlreadyExistsError:
    message: Optional[str] = field(default=None)


def _serialize_platform_discount_share_policy_already_exists_error(obj: PlatformDiscountSharePolicyAlreadyExistsError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_DISCOUNT_SHARE_POLICY_ALREADY_EXISTS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_discount_share_policy_already_exists_error(obj: Any) -> PlatformDiscountSharePolicyAlreadyExistsError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_DISCOUNT_SHARE_POLICY_ALREADY_EXISTS":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_DISCOUNT_SHARE_POLICY_ALREADY_EXISTS'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformDiscountSharePolicyAlreadyExistsError(message)
