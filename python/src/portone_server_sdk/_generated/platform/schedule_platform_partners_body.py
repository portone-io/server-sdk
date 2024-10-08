from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_partner_filter_input import PlatformPartnerFilterInput, _deserialize_platform_partner_filter_input, _serialize_platform_partner_filter_input
from portone_server_sdk._generated.platform.schedule_platform_partners_body_update import SchedulePlatformPartnersBodyUpdate, _deserialize_schedule_platform_partners_body_update, _serialize_schedule_platform_partners_body_update

@dataclass
class SchedulePlatformPartnersBody:
    update: SchedulePlatformPartnersBodyUpdate
    applied_at: str
    """(RFC 3339 date-time)
    """
    filter: Optional[PlatformPartnerFilterInput]


def _serialize_schedule_platform_partners_body(obj: SchedulePlatformPartnersBody) -> Any:
    entity = {}
    entity["update"] = _serialize_schedule_platform_partners_body_update(obj.update)
    entity["appliedAt"] = obj.applied_at
    if obj.filter is not None:
        entity["filter"] = _serialize_platform_partner_filter_input(obj.filter)
    return entity


def _deserialize_schedule_platform_partners_body(obj: Any) -> SchedulePlatformPartnersBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "update" not in obj:
        raise KeyError(f"'update' is not in {obj}")
    update = obj["update"]
    update = _deserialize_schedule_platform_partners_body_update(update)
    if "appliedAt" not in obj:
        raise KeyError(f"'appliedAt' is not in {obj}")
    applied_at = obj["appliedAt"]
    if not isinstance(applied_at, str):
        raise ValueError(f"{repr(applied_at)} is not str")
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_platform_partner_filter_input(filter)
    else:
        filter = None
    return SchedulePlatformPartnersBody(update, applied_at, filter)
