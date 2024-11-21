from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_fee_input import PlatformFeeInput, _deserialize_platform_fee_input, _serialize_platform_fee_input
from ..platform.platform_payer import PlatformPayer, _deserialize_platform_payer, _serialize_platform_payer
from ..platform.platform_settlement_cycle_input import PlatformSettlementCycleInput, _deserialize_platform_settlement_cycle_input, _serialize_platform_settlement_cycle_input

@dataclass
class UpdatePlatformContractBody:
    """계약 업데이트를 위한 입력 정보. 값이 명시되지 않은 필드는 업데이트되지 않습니다.

    값이 명시되지 않은 필드는 업데이트되지 않습니다.
    """
    name: Optional[str] = field(default=None)
    """계약 이름
    """
    memo: Optional[str] = field(default=None)
    """계약 내부 표기를 위한 메모
    """
    platform_fee: Optional[PlatformFeeInput] = field(default=None)
    """중개수수료
    """
    settlement_cycle: Optional[PlatformSettlementCycleInput] = field(default=None)
    """정산 주기
    """
    platform_fee_vat_payer: Optional[PlatformPayer] = field(default=None)
    """중개수수료에 대한 부가세 부담 주체
    """
    subtract_payment_vat_amount: Optional[bool] = field(default=None)
    """정산 시 결제금액 부가세 감액 여부
    """


def _serialize_update_platform_contract_body(obj: UpdatePlatformContractBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.platform_fee is not None:
        entity["platformFee"] = _serialize_platform_fee_input(obj.platform_fee)
    if obj.settlement_cycle is not None:
        entity["settlementCycle"] = _serialize_platform_settlement_cycle_input(obj.settlement_cycle)
    if obj.platform_fee_vat_payer is not None:
        entity["platformFeeVatPayer"] = _serialize_platform_payer(obj.platform_fee_vat_payer)
    if obj.subtract_payment_vat_amount is not None:
        entity["subtractPaymentVatAmount"] = obj.subtract_payment_vat_amount
    return entity


def _deserialize_update_platform_contract_body(obj: Any) -> UpdatePlatformContractBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    if "platformFee" in obj:
        platform_fee = obj["platformFee"]
        platform_fee = _deserialize_platform_fee_input(platform_fee)
    else:
        platform_fee = None
    if "settlementCycle" in obj:
        settlement_cycle = obj["settlementCycle"]
        settlement_cycle = _deserialize_platform_settlement_cycle_input(settlement_cycle)
    else:
        settlement_cycle = None
    if "platformFeeVatPayer" in obj:
        platform_fee_vat_payer = obj["platformFeeVatPayer"]
        platform_fee_vat_payer = _deserialize_platform_payer(platform_fee_vat_payer)
    else:
        platform_fee_vat_payer = None
    if "subtractPaymentVatAmount" in obj:
        subtract_payment_vat_amount = obj["subtractPaymentVatAmount"]
        if not isinstance(subtract_payment_vat_amount, bool):
            raise ValueError(f"{repr(subtract_payment_vat_amount)} is not bool")
    else:
        subtract_payment_vat_amount = None
    return UpdatePlatformContractBody(name, memo, platform_fee, settlement_cycle, platform_fee_vat_payer, subtract_payment_vat_amount)
