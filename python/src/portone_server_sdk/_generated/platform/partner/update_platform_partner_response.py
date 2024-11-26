from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner

@dataclass
class UpdatePlatformPartnerResponse:
    """파트너 업데이트 성공 응답
    """
    partner: PlatformPartner
    """업데이트된 파트너
    """


def _serialize_update_platform_partner_response(obj: UpdatePlatformPartnerResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["partner"] = _serialize_platform_partner(obj.partner)
    return entity


def _deserialize_update_platform_partner_response(obj: Any) -> UpdatePlatformPartnerResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "partner" not in obj:
        raise KeyError(f"'partner' is not in {obj}")
    partner = obj["partner"]
    partner = _deserialize_platform_partner(partner)
    return UpdatePlatformPartnerResponse(partner)
