from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_fee_input import PlatformFeeInput, _deserialize_platform_fee_input, _serialize_platform_fee_input
from ...platform.platform_payer import PlatformPayer, _deserialize_platform_payer, _serialize_platform_payer
from ...platform.platform_settlement_cycle_input import PlatformSettlementCycleInput, _deserialize_platform_settlement_cycle_input, _serialize_platform_settlement_cycle_input

@dataclass
class CreatePlatformContractBody:
    """계약 객체 생성을 위한 입력 정보
    """
    name: str
    """계약 이름
    """
    platform_fee: PlatformFeeInput
    """중개수수료
    """
    settlement_cycle: PlatformSettlementCycleInput
    """정산 주기
    """
    platform_fee_vat_payer: PlatformPayer
    """중개수수료에 대한 부가세 부담 주체
    """
    subtract_payment_vat_amount: bool
    """정산 시 결제금액 부가세 감액 여부
    """
    id: Optional[str] = field(default=None)
    """계약에 부여할 고유 아이디

    명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
    """
    memo: Optional[str] = field(default=None)
    """계약 내부 표기를 위한 메모
    """


def _serialize_create_platform_contract_body(obj: CreatePlatformContractBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["name"] = obj.name
    entity["platformFee"] = _serialize_platform_fee_input(obj.platform_fee)
    entity["settlementCycle"] = _serialize_platform_settlement_cycle_input(obj.settlement_cycle)
    entity["platformFeeVatPayer"] = _serialize_platform_payer(obj.platform_fee_vat_payer)
    entity["subtractPaymentVatAmount"] = obj.subtract_payment_vat_amount
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_create_platform_contract_body(obj: Any) -> CreatePlatformContractBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "platformFee" not in obj:
        raise KeyError(f"'platformFee' is not in {obj}")
    platform_fee = obj["platformFee"]
    platform_fee = _deserialize_platform_fee_input(platform_fee)
    if "settlementCycle" not in obj:
        raise KeyError(f"'settlementCycle' is not in {obj}")
    settlement_cycle = obj["settlementCycle"]
    settlement_cycle = _deserialize_platform_settlement_cycle_input(settlement_cycle)
    if "platformFeeVatPayer" not in obj:
        raise KeyError(f"'platformFeeVatPayer' is not in {obj}")
    platform_fee_vat_payer = obj["platformFeeVatPayer"]
    platform_fee_vat_payer = _deserialize_platform_payer(platform_fee_vat_payer)
    if "subtractPaymentVatAmount" not in obj:
        raise KeyError(f"'subtractPaymentVatAmount' is not in {obj}")
    subtract_payment_vat_amount = obj["subtractPaymentVatAmount"]
    if not isinstance(subtract_payment_vat_amount, bool):
        raise ValueError(f"{repr(subtract_payment_vat_amount)} is not bool")
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return CreatePlatformContractBody(name, platform_fee, settlement_cycle, platform_fee_vat_payer, subtract_payment_vat_amount, id, memo)
