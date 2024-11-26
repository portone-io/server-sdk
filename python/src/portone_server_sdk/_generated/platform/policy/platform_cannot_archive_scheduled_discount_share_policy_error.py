from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCannotArchiveScheduledDiscountSharePolicyError:
    """예약된 업데이트가 있는 할인 분담 정책을 보관하려고 하는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_cannot_archive_scheduled_discount_share_policy_error(obj: PlatformCannotArchiveScheduledDiscountSharePolicyError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_DISCOUNT_SHARE_POLICY"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cannot_archive_scheduled_discount_share_policy_error(obj: Any) -> PlatformCannotArchiveScheduledDiscountSharePolicyError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_DISCOUNT_SHARE_POLICY":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_CANNOT_ARCHIVE_SCHEDULED_DISCOUNT_SHARE_POLICY'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformCannotArchiveScheduledDiscountSharePolicyError(message)
