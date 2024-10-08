from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementFormula:
    """플랫폼 내 발생하는 여러 수수료 및 할인 분담에 관한 계산식 정보
    """
    platform_fee: str
    """플랫폼 수수료 계산식
    """
    discount_share: str
    """할인 분담액 계산식
    """
    additional_fee: str
    """추가 수수료 계산식
    """


def _serialize_platform_settlement_formula(obj: PlatformSettlementFormula) -> Any:
    entity = {}
    entity["platformFee"] = obj.platform_fee
    entity["discountShare"] = obj.discount_share
    entity["additionalFee"] = obj.additional_fee
    return entity


def _deserialize_platform_settlement_formula(obj: Any) -> PlatformSettlementFormula:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "platformFee" not in obj:
        raise KeyError(f"'platformFee' is not in {obj}")
    platform_fee = obj["platformFee"]
    if not isinstance(platform_fee, str):
        raise ValueError(f"{repr(platform_fee)} is not str")
    if "discountShare" not in obj:
        raise KeyError(f"'discountShare' is not in {obj}")
    discount_share = obj["discountShare"]
    if not isinstance(discount_share, str):
        raise ValueError(f"{repr(discount_share)} is not str")
    if "additionalFee" not in obj:
        raise KeyError(f"'additionalFee' is not in {obj}")
    additional_fee = obj["additionalFee"]
    if not isinstance(additional_fee, str):
        raise ValueError(f"{repr(additional_fee)} is not str")
    return PlatformSettlementFormula(platform_fee, discount_share, additional_fee)
