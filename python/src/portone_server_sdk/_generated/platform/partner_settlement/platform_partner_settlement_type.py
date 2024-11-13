from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformPartnerSettlementType = Union[Literal["MANUAL", "ORDER", "ORDER_CANCEL"], str]
"""정산 유형
"""


def _serialize_platform_partner_settlement_type(obj: PlatformPartnerSettlementType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_partner_settlement_type(obj: Any) -> PlatformPartnerSettlementType:
    return obj
