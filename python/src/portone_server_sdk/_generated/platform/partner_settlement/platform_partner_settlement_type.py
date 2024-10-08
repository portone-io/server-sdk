from __future__ import annotations
from typing import Any, Literal, Optional

PlatformPartnerSettlementType = Literal["MANUAL", "ORDER", "ORDER_CANCEL"]
"""정산 유형
"""


def _serialize_platform_partner_settlement_type(obj: PlatformPartnerSettlementType) -> Any:
    return obj


def _deserialize_platform_partner_settlement_type(obj: Any) -> PlatformPartnerSettlementType:
    if obj not in ["MANUAL", "ORDER", "ORDER_CANCEL"]:
        raise ValueError(f"{repr(obj)} is not PlatformPartnerSettlementType")
    return obj
