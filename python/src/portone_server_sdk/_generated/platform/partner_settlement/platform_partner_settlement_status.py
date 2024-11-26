from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformPartnerSettlementStatus = Union[Literal["PAYOUT_SCHEDULED", "PAYOUT_PREPARED", "PAYOUT_WITHHELD", "PAYOUT_FAILED", "IN_PAYOUT", "PAID_OUT"], str]
"""정산 상태
"""


def _serialize_platform_partner_settlement_status(obj: PlatformPartnerSettlementStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_partner_settlement_status(obj: Any) -> PlatformPartnerSettlementStatus:
    return obj
