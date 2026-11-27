from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformMemberCompanyConnectedPartnersCannotBeScheduledError:
    """연동 사업자로 연동된 파트너들을 예약 수정하려고 시도한 경우
    """
    ids: list[str]
    graphql_ids: list[str]
    message: Optional[str] = field(default=None)


def _serialize_platform_member_company_connected_partners_cannot_be_scheduled_error(obj: PlatformMemberCompanyConnectedPartnersCannotBeScheduledError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_MEMBER_COMPANY_CONNECTED_PARTNERS_CANNOT_BE_SCHEDULED"
    entity["ids"] = obj.ids
    entity["graphqlIds"] = obj.graphql_ids
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_member_company_connected_partners_cannot_be_scheduled_error(obj: Any) -> PlatformMemberCompanyConnectedPartnersCannotBeScheduledError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_MEMBER_COMPANY_CONNECTED_PARTNERS_CANNOT_BE_SCHEDULED":
        raise ValueError("Expected 'PLATFORM_MEMBER_COMPANY_CONNECTED_PARTNERS_CANNOT_BE_SCHEDULED' for type")
    if "ids" not in obj:
        raise KeyError("Missing required field 'ids'")
    ids = obj["ids"]
    if not isinstance(ids, list):
        raise ValueError("Expected list for ids")
    for i, item in enumerate(ids):
        if not isinstance(item, str):
            raise ValueError("Expected str for item")
    if "graphqlIds" not in obj:
        raise KeyError("Missing required field 'graphqlIds'")
    graphql_ids = obj["graphqlIds"]
    if not isinstance(graphql_ids, list):
        raise ValueError("Expected list for graphql_ids")
    for i, item in enumerate(graphql_ids):
        if not isinstance(item, str):
            raise ValueError("Expected str for item")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformMemberCompanyConnectedPartnersCannotBeScheduledError(ids, graphql_ids, message)
