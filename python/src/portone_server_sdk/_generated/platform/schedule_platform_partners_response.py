from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class SchedulePlatformPartnersResponse:
    pass


def _serialize_schedule_platform_partners_response(obj: SchedulePlatformPartnersResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_schedule_platform_partners_response(obj: Any) -> SchedulePlatformPartnersResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return SchedulePlatformPartnersResponse()
