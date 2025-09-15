from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_partner_filter_input import PlatformPartnerFilterInput, _deserialize_platform_partner_filter_input, _serialize_platform_partner_filter_input

@dataclass
class DisconnectBulkPartnerMemberCompanyBody:
    """파트너 일괄 국세청 연동 해제 요청 정보

    파트너들을 일괄 국세청 연동 해제합니다.
    """
    filter: Optional[PlatformPartnerFilterInput] = field(default=None)
    """일괄 국세청 연동 해제할 파트너 조건 필터
    """


def _serialize_disconnect_bulk_partner_member_company_body(obj: DisconnectBulkPartnerMemberCompanyBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.filter is not None:
        entity["filter"] = _serialize_platform_partner_filter_input(obj.filter)
    return entity


def _deserialize_disconnect_bulk_partner_member_company_body(obj: Any) -> DisconnectBulkPartnerMemberCompanyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_platform_partner_filter_input(filter)
    else:
        filter = None
    return DisconnectBulkPartnerMemberCompanyBody(filter)
