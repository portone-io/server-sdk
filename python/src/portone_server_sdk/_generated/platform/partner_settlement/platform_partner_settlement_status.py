from __future__ import annotations
from typing import Any, Literal, Optional

PlatformPartnerSettlementStatus = Literal["PAYOUT_SCHEDULED", "PAYOUT_PREPARED", "PAYOUT_WITHHELD", "PAYOUT_FAILED", "IN_PAYOUT", "PAID_OUT"]
"""정산 상태
"""


def _serialize_platform_partner_settlement_status(obj: PlatformPartnerSettlementStatus) -> Any:
    return obj


def _deserialize_platform_partner_settlement_status(obj: Any) -> PlatformPartnerSettlementStatus:
    if obj not in ["PAYOUT_SCHEDULED", "PAYOUT_PREPARED", "PAYOUT_WITHHELD", "PAYOUT_FAILED", "IN_PAYOUT", "PAID_OUT"]:
        raise ValueError(f"{repr(obj)} is not PlatformPartnerSettlementStatus")
    return obj
