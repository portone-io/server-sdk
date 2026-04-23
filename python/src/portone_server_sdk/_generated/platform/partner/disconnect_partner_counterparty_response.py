from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner

@dataclass
class DisconnectPartnerCounterpartyResponse:
    """파트너 거래처 연동 해제 응답
    """
    partner: PlatformPartner


def _serialize_disconnect_partner_counterparty_response(obj: DisconnectPartnerCounterpartyResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["partner"] = _serialize_platform_partner(obj.partner)
    return entity


def _deserialize_disconnect_partner_counterparty_response(obj: Any) -> DisconnectPartnerCounterpartyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "partner" not in obj:
        raise KeyError(f"'partner' is not in {obj}")
    partner = obj["partner"]
    partner = _deserialize_platform_partner(partner)
    return DisconnectPartnerCounterpartyResponse(partner)
