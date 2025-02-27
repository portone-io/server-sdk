from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.partner.platform_bulk_task import PlatformBulkTask, _deserialize_platform_bulk_task, _serialize_platform_bulk_task

@dataclass
class DisconnectBulkPartnerMemberCompanyResponse:
    """파트너 연동 사업자 일괄 연동 해제 요청 응답
    """
    bulk_task: PlatformBulkTask


def _serialize_disconnect_bulk_partner_member_company_response(obj: DisconnectBulkPartnerMemberCompanyResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["bulkTask"] = _serialize_platform_bulk_task(obj.bulk_task)
    return entity


def _deserialize_disconnect_bulk_partner_member_company_response(obj: Any) -> DisconnectBulkPartnerMemberCompanyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "bulkTask" not in obj:
        raise KeyError(f"'bulkTask' is not in {obj}")
    bulk_task = obj["bulkTask"]
    bulk_task = _deserialize_platform_bulk_task(bulk_task)
    return DisconnectBulkPartnerMemberCompanyResponse(bulk_task)
