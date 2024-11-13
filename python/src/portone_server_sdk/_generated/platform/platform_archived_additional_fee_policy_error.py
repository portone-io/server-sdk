from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformArchivedAdditionalFeePolicyError:
    """보관된 추가 수수료 정책을 업데이트하려고 하는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_archived_additional_fee_policy_error(obj: PlatformArchivedAdditionalFeePolicyError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_ARCHIVED_ADDITIONAL_FEE_POLICY"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_archived_additional_fee_policy_error(obj: Any) -> PlatformArchivedAdditionalFeePolicyError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_ARCHIVED_ADDITIONAL_FEE_POLICY":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_ARCHIVED_ADDITIONAL_FEE_POLICY'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformArchivedAdditionalFeePolicyError(message)
