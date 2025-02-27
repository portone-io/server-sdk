from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner

@dataclass
class DisconnectPartnerMemberCompanyResponse:
    """연동 사업자 연동 해제 요청 응답
    """
    partner: PlatformPartner


def _serialize_disconnect_partner_member_company_response(obj: DisconnectPartnerMemberCompanyResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["partner"] = _serialize_platform_partner(obj.partner)
    return entity


def _deserialize_disconnect_partner_member_company_response(obj: Any) -> DisconnectPartnerMemberCompanyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "partner" not in obj:
        raise KeyError(f"'partner' is not in {obj}")
    partner = obj["partner"]
    partner = _deserialize_platform_partner(partner)
    return DisconnectPartnerMemberCompanyResponse(partner)
