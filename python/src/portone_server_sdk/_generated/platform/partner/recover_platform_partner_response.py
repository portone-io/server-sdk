from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner

@dataclass
class RecoverPlatformPartnerResponse:
    """파트너 복원 성공 응답
    """
    partner: PlatformPartner
    """복원된 파트너
    """


def _serialize_recover_platform_partner_response(obj: RecoverPlatformPartnerResponse) -> Any:
    entity = {}
    entity["partner"] = _serialize_platform_partner(obj.partner)
    return entity


def _deserialize_recover_platform_partner_response(obj: Any) -> RecoverPlatformPartnerResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "partner" not in obj:
        raise KeyError(f"'partner' is not in {obj}")
    partner = obj["partner"]
    partner = _deserialize_platform_partner(partner)
    return RecoverPlatformPartnerResponse(partner)