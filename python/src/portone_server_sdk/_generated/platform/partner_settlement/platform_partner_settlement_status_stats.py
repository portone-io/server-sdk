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
    payout_excluded: int
    """(int64)
    """
    payout_failed: int
    """(int64)
    """
    payout_cancelled: int
    """(int64)
    """
    payout_confirmed: int
    """(int64)
    """
    in_payout: int
    """(int64)
    """
    paid_out: int
    """(int64)
    """


def _serialize_platform_partner_settlement_status_stats(obj: PlatformPartnerSettlementStatusStats) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["payoutScheduled"] = obj.payout_scheduled
    entity["payoutPrepared"] = obj.payout_prepared
    entity["payoutWithheld"] = obj.payout_withheld
    entity["payoutExcluded"] = obj.payout_excluded
    entity["payoutFailed"] = obj.payout_failed
    entity["payoutCancelled"] = obj.payout_cancelled
    entity["payoutConfirmed"] = obj.payout_confirmed
    entity["inPayout"] = obj.in_payout
    entity["paidOut"] = obj.paid_out
    return entity


def _deserialize_platform_partner_settlement_status_stats(obj: Any) -> PlatformPartnerSettlementStatusStats:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "payoutScheduled" not in obj:
        raise KeyError("Missing required field 'payoutScheduled'")
    payout_scheduled = obj["payoutScheduled"]
    if not isinstance(payout_scheduled, int):
        raise ValueError("Expected int for payout_scheduled")
    if "payoutPrepared" not in obj:
        raise KeyError("Missing required field 'payoutPrepared'")
    payout_prepared = obj["payoutPrepared"]
    if not isinstance(payout_prepared, int):
        raise ValueError("Expected int for payout_prepared")
    if "payoutWithheld" not in obj:
        raise KeyError("Missing required field 'payoutWithheld'")
    payout_withheld = obj["payoutWithheld"]
    if not isinstance(payout_withheld, int):
        raise ValueError("Expected int for payout_withheld")
    if "payoutExcluded" not in obj:
        raise KeyError("Missing required field 'payoutExcluded'")
    payout_excluded = obj["payoutExcluded"]
    if not isinstance(payout_excluded, int):
        raise ValueError("Expected int for payout_excluded")
    if "payoutFailed" not in obj:
        raise KeyError("Missing required field 'payoutFailed'")
    payout_failed = obj["payoutFailed"]
    if not isinstance(payout_failed, int):
        raise ValueError("Expected int for payout_failed")
    if "payoutCancelled" not in obj:
        raise KeyError("Missing required field 'payoutCancelled'")
    payout_cancelled = obj["payoutCancelled"]
    if not isinstance(payout_cancelled, int):
        raise ValueError("Expected int for payout_cancelled")
    if "payoutConfirmed" not in obj:
        raise KeyError("Missing required field 'payoutConfirmed'")
    payout_confirmed = obj["payoutConfirmed"]
    if not isinstance(payout_confirmed, int):
        raise ValueError("Expected int for payout_confirmed")
    if "inPayout" not in obj:
        raise KeyError("Missing required field 'inPayout'")
    in_payout = obj["inPayout"]
    if not isinstance(in_payout, int):
        raise ValueError("Expected int for in_payout")
    if "paidOut" not in obj:
        raise KeyError("Missing required field 'paidOut'")
    paid_out = obj["paidOut"]
    if not isinstance(paid_out, int):
        raise ValueError("Expected int for paid_out")
    return PlatformPartnerSettlementStatusStats(payout_scheduled, payout_prepared, payout_withheld, payout_excluded, payout_failed, payout_cancelled, payout_confirmed, in_payout, paid_out)
