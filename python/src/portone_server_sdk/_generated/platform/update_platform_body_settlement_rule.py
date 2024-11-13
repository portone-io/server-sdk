from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class UpdatePlatformBodySettlementRule:
    """플랫폼 업데이트 시 변경할 정산 규칙 정보

    값이 명시되지 않은 필드는 업데이트하지 않습니다.
    """
    supports_multiple_order_transfers_per_partner: Optional[bool] = field(default=None)
    """paymentId, storeId, partnerId가 같은 주문 정산건에 대한 중복 정산 지원 여부
    """
    adjust_settlement_date_after_holiday_if_earlier: Optional[bool] = field(default=None)
    """정산일이 정산시작일보다 작거나 같을 경우 공휴일 후 영업일로 정산일 다시 계산 여부
    """
    subtract_wht_in_payout_amount: Optional[bool] = field(default=None)
    """지급 금액에서 원천징수세 차감 여부
    """


def _serialize_update_platform_body_settlement_rule(obj: UpdatePlatformBodySettlementRule) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.supports_multiple_order_transfers_per_partner is not None:
        entity["supportsMultipleOrderTransfersPerPartner"] = obj.supports_multiple_order_transfers_per_partner
    if obj.adjust_settlement_date_after_holiday_if_earlier is not None:
        entity["adjustSettlementDateAfterHolidayIfEarlier"] = obj.adjust_settlement_date_after_holiday_if_earlier
    if obj.subtract_wht_in_payout_amount is not None:
        entity["subtractWhtInPayoutAmount"] = obj.subtract_wht_in_payout_amount
    return entity


def _deserialize_update_platform_body_settlement_rule(obj: Any) -> UpdatePlatformBodySettlementRule:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "supportsMultipleOrderTransfersPerPartner" in obj:
        supports_multiple_order_transfers_per_partner = obj["supportsMultipleOrderTransfersPerPartner"]
        if not isinstance(supports_multiple_order_transfers_per_partner, bool):
            raise ValueError(f"{repr(supports_multiple_order_transfers_per_partner)} is not bool")
    else:
        supports_multiple_order_transfers_per_partner = None
    if "adjustSettlementDateAfterHolidayIfEarlier" in obj:
        adjust_settlement_date_after_holiday_if_earlier = obj["adjustSettlementDateAfterHolidayIfEarlier"]
        if not isinstance(adjust_settlement_date_after_holiday_if_earlier, bool):
            raise ValueError(f"{repr(adjust_settlement_date_after_holiday_if_earlier)} is not bool")
    else:
        adjust_settlement_date_after_holiday_if_earlier = None
    if "subtractWhtInPayoutAmount" in obj:
        subtract_wht_in_payout_amount = obj["subtractWhtInPayoutAmount"]
        if not isinstance(subtract_wht_in_payout_amount, bool):
            raise ValueError(f"{repr(subtract_wht_in_payout_amount)} is not bool")
    else:
        subtract_wht_in_payout_amount = None
    return UpdatePlatformBodySettlementRule(supports_multiple_order_transfers_per_partner, adjust_settlement_date_after_holiday_if_earlier, subtract_wht_in_payout_amount)
