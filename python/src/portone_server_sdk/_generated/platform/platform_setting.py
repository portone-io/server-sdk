from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.settlement_amount_type import SettlementAmountType, _deserialize_settlement_amount_type, _serialize_settlement_amount_type

@dataclass
class PlatformSetting:
    """플랫폼 설정
    """
    supports_multiple_order_transfers_per_partner: bool
    """paymentId, storeId, partnerId가 같은 주문 정산건에 대한 중복 정산 지원 여부
    """
    adjust_settlement_date_after_holiday_if_earlier: bool
    """정산일이 정산시작일보다 작거나 같을 경우 공휴일 후 영업일로 정산일 다시 계산 여부
    """
    deduct_wht: bool
    """지급 금액에서 원천징수세 차감 여부
    """
    settlement_amount_type: SettlementAmountType
    """정산 금액 취급 기준
    """
    is_for_test: bool
    default_withdrawal_memo: Optional[str] = field(default=None)
    """기본 보내는 이 통장 메모
    """
    default_deposit_memo: Optional[str] = field(default=None)
    """기본 받는 이 통장 메모
    """


def _serialize_platform_setting(obj: PlatformSetting) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["supportsMultipleOrderTransfersPerPartner"] = obj.supports_multiple_order_transfers_per_partner
    entity["adjustSettlementDateAfterHolidayIfEarlier"] = obj.adjust_settlement_date_after_holiday_if_earlier
    entity["deductWht"] = obj.deduct_wht
    entity["settlementAmountType"] = _serialize_settlement_amount_type(obj.settlement_amount_type)
    entity["isForTest"] = obj.is_for_test
    if obj.default_withdrawal_memo is not None:
        entity["defaultWithdrawalMemo"] = obj.default_withdrawal_memo
    if obj.default_deposit_memo is not None:
        entity["defaultDepositMemo"] = obj.default_deposit_memo
    return entity


def _deserialize_platform_setting(obj: Any) -> PlatformSetting:
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
    if "deductWht" not in obj:
        raise KeyError(f"'deductWht' is not in {obj}")
    deduct_wht = obj["deductWht"]
    if not isinstance(deduct_wht, bool):
        raise ValueError(f"{repr(deduct_wht)} is not bool")
    if "settlementAmountType" not in obj:
        raise KeyError(f"'settlementAmountType' is not in {obj}")
    settlement_amount_type = obj["settlementAmountType"]
    settlement_amount_type = _deserialize_settlement_amount_type(settlement_amount_type)
    if "isForTest" not in obj:
        raise KeyError(f"'isForTest' is not in {obj}")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError(f"{repr(is_for_test)} is not bool")
    if "defaultWithdrawalMemo" in obj:
        default_withdrawal_memo = obj["defaultWithdrawalMemo"]
        if not isinstance(default_withdrawal_memo, str):
            raise ValueError(f"{repr(default_withdrawal_memo)} is not str")
    else:
        default_withdrawal_memo = None
    if "defaultDepositMemo" in obj:
        default_deposit_memo = obj["defaultDepositMemo"]
        if not isinstance(default_deposit_memo, str):
            raise ValueError(f"{repr(default_deposit_memo)} is not str")
    else:
        default_deposit_memo = None
    return PlatformSetting(supports_multiple_order_transfers_per_partner, adjust_settlement_date_after_holiday_if_earlier, deduct_wht, settlement_amount_type, is_for_test, default_withdrawal_memo, default_deposit_memo)
