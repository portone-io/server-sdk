from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPartnerSettlementStatusStats:
    payout_scheduled: int
    """(int64)
    """
    payout_prepared: int
    """(int64)
    """
    payout_withheld: int
    """(int64)
    """
    payout_failed: int
    """(int64)
    """
    in_payout: int
    """(int64)
    """
    paid_out: int
    """(int64)
    """


def _serialize_platform_partner_settlement_status_stats(obj: PlatformPartnerSettlementStatusStats) -> Any:
    entity = {}
    entity["payoutScheduled"] = obj.payout_scheduled
    entity["payoutPrepared"] = obj.payout_prepared
    entity["payoutWithheld"] = obj.payout_withheld
    entity["payoutFailed"] = obj.payout_failed
    entity["inPayout"] = obj.in_payout
    entity["paidOut"] = obj.paid_out
    return entity


def _deserialize_platform_partner_settlement_status_stats(obj: Any) -> PlatformPartnerSettlementStatusStats:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "payoutScheduled" not in obj:
        raise KeyError(f"'payoutScheduled' is not in {obj}")
    payout_scheduled = obj["payoutScheduled"]
    if not isinstance(payout_scheduled, int):
        raise ValueError(f"{repr(payout_scheduled)} is not int")
    if "payoutPrepared" not in obj:
        raise KeyError(f"'payoutPrepared' is not in {obj}")
    payout_prepared = obj["payoutPrepared"]
    if not isinstance(payout_prepared, int):
        raise ValueError(f"{repr(payout_prepared)} is not int")
    if "payoutWithheld" not in obj:
        raise KeyError(f"'payoutWithheld' is not in {obj}")
    payout_withheld = obj["payoutWithheld"]
    if not isinstance(payout_withheld, int):
        raise ValueError(f"{repr(payout_withheld)} is not int")
    if "payoutFailed" not in obj:
        raise KeyError(f"'payoutFailed' is not in {obj}")
    payout_failed = obj["payoutFailed"]
    if not isinstance(payout_failed, int):
        raise ValueError(f"{repr(payout_failed)} is not int")
    if "inPayout" not in obj:
        raise KeyError(f"'inPayout' is not in {obj}")
    in_payout = obj["inPayout"]
    if not isinstance(in_payout, int):
        raise ValueError(f"{repr(in_payout)} is not int")
    if "paidOut" not in obj:
        raise KeyError(f"'paidOut' is not in {obj}")
    paid_out = obj["paidOut"]
    if not isinstance(paid_out, int):
        raise ValueError(f"{repr(paid_out)} is not int")
    return PlatformPartnerSettlementStatusStats(payout_scheduled, payout_prepared, payout_withheld, payout_failed, in_payout, paid_out)
