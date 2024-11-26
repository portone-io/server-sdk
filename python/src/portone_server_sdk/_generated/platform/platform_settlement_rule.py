from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementRule:
    """플랫폼 정산건 처리 방식에 관한 규칙
    """
    supports_multiple_order_transfers_per_partner: bool
    """paymentId, storeId, partnerId가 같은 주문 정산건에 대한 중복 정산 지원 여부
    """
    adjust_settlement_date_after_holiday_if_earlier: bool
    """정산일이 정산시작일보다 작거나 같을 경우 공휴일 후 영업일로 정산일 다시 계산 여부
    """
    subtract_wht_in_payout_amount: bool
    """지급 금액에서 원천징수세 차감 여부
    """


def _serialize_platform_settlement_rule(obj: PlatformSettlementRule) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["supportsMultipleOrderTransfersPerPartner"] = obj.supports_multiple_order_transfers_per_partner
    entity["adjustSettlementDateAfterHolidayIfEarlier"] = obj.adjust_settlement_date_after_holiday_if_earlier
    entity["subtractWhtInPayoutAmount"] = obj.subtract_wht_in_payout_amount
    return entity


def _deserialize_platform_settlement_rule(obj: Any) -> PlatformSettlementRule:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "supportsMultipleOrderTransfersPerPartner" not in obj:
        raise KeyError(f"'supportsMultipleOrderTransfersPerPartner' is not in {obj}")
    supports_multiple_order_transfers_per_partner = obj["supportsMultipleOrderTransfersPerPartner"]
    if not isinstance(supports_multiple_order_transfers_per_partner, bool):
        raise ValueError(f"{repr(supports_multiple_order_transfers_per_partner)} is not bool")
    if "adjustSettlementDateAfterHolidayIfEarlier" not in obj:
        raise KeyError(f"'adjustSettlementDateAfterHolidayIfEarlier' is not in {obj}")
    adjust_settlement_date_after_holiday_if_earlier = obj["adjustSettlementDateAfterHolidayIfEarlier"]
    if not isinstance(adjust_settlement_date_after_holiday_if_earlier, bool):
        raise ValueError(f"{repr(adjust_settlement_date_after_holiday_if_earlier)} is not bool")
    if "subtractWhtInPayoutAmount" not in obj:
        raise KeyError(f"'subtractWhtInPayoutAmount' is not in {obj}")
    subtract_wht_in_payout_amount = obj["subtractWhtInPayoutAmount"]
    if not isinstance(subtract_wht_in_payout_amount, bool):
        raise ValueError(f"{repr(subtract_wht_in_payout_amount)} is not bool")
    return PlatformSettlementRule(supports_multiple_order_transfers_per_partner, adjust_settlement_date_after_holiday_if_earlier, subtract_wht_in_payout_amount)
