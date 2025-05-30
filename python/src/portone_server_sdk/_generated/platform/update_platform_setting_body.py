from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.settlement_amount_type import SettlementAmountType, _deserialize_settlement_amount_type, _serialize_settlement_amount_type

@dataclass
class UpdatePlatformSettingBody:
    """플랫폼 설정 업데이트를 위한 입력 정보
    """
    default_withdrawal_memo: Optional[str] = field(default=None)
    """기본 보내는 이 통장 메모
    """
    default_deposit_memo: Optional[str] = field(default=None)
    """기본 받는 이 통장 메모
    """
    supports_multiple_order_transfers_per_partner: Optional[bool] = field(default=None)
    """paymentId, storeId, partnerId가 같은 주문 정산건에 대한 중복 정산 지원 여부
    """
    adjust_settlement_date_after_holiday_if_earlier: Optional[bool] = field(default=None)
    """정산일이 정산시작일보다 작거나 같을 경우 공휴일 후 영업일로 정산일 다시 계산 여부
    """
    deduct_wht: Optional[bool] = field(default=None)
    """지급 금액에서 원천징수세 차감 여부
    """
    settlement_amount_type: Optional[SettlementAmountType] = field(default=None)
    """정산 금액 취급 기준
    """


def _serialize_update_platform_setting_body(obj: UpdatePlatformSettingBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.default_withdrawal_memo is not None:
        entity["defaultWithdrawalMemo"] = obj.default_withdrawal_memo
    if obj.default_deposit_memo is not None:
        entity["defaultDepositMemo"] = obj.default_deposit_memo
    if obj.supports_multiple_order_transfers_per_partner is not None:
        entity["supportsMultipleOrderTransfersPerPartner"] = obj.supports_multiple_order_transfers_per_partner
    if obj.adjust_settlement_date_after_holiday_if_earlier is not None:
        entity["adjustSettlementDateAfterHolidayIfEarlier"] = obj.adjust_settlement_date_after_holiday_if_earlier
    if obj.deduct_wht is not None:
        entity["deductWht"] = obj.deduct_wht
    if obj.settlement_amount_type is not None:
        entity["settlementAmountType"] = _serialize_settlement_amount_type(obj.settlement_amount_type)
    return entity


def _deserialize_update_platform_setting_body(obj: Any) -> UpdatePlatformSettingBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
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
    if "deductWht" in obj:
        deduct_wht = obj["deductWht"]
        if not isinstance(deduct_wht, bool):
            raise ValueError(f"{repr(deduct_wht)} is not bool")
    else:
        deduct_wht = None
    if "settlementAmountType" in obj:
        settlement_amount_type = obj["settlementAmountType"]
        settlement_amount_type = _deserialize_settlement_amount_type(settlement_amount_type)
    else:
        settlement_amount_type = None
    return UpdatePlatformSettingBody(default_withdrawal_memo, default_deposit_memo, supports_multiple_order_transfers_per_partner, adjust_settlement_date_after_holiday_if_earlier, deduct_wht, settlement_amount_type)
