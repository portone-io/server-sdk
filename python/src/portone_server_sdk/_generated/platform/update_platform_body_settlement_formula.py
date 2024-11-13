from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class UpdatePlatformBodySettlementFormula:
    """플랫폼 업데이트 시 변경할 계산식 정보

    값이 명시되지 않은 필드는 업데이트하지 않습니다.
    """
    platform_fee: Optional[str] = field(default=None)
    """플랫폼 수수료 계산식
    """
    discount_share: Optional[str] = field(default=None)
    """할인 분담액 계산식
    """
    additional_fee: Optional[str] = field(default=None)
    """추가 수수료 계산식
    """


def _serialize_update_platform_body_settlement_formula(obj: UpdatePlatformBodySettlementFormula) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.platform_fee is not None:
        entity["platformFee"] = obj.platform_fee
    if obj.discount_share is not None:
        entity["discountShare"] = obj.discount_share
    if obj.additional_fee is not None:
        entity["additionalFee"] = obj.additional_fee
    return entity


def _deserialize_update_platform_body_settlement_formula(obj: Any) -> UpdatePlatformBodySettlementFormula:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "platformFee" in obj:
        platform_fee = obj["platformFee"]
        if not isinstance(platform_fee, str):
            raise ValueError(f"{repr(platform_fee)} is not str")
    else:
        platform_fee = None
    if "discountShare" in obj:
        discount_share = obj["discountShare"]
        if not isinstance(discount_share, str):
            raise ValueError(f"{repr(discount_share)} is not str")
    else:
        discount_share = None
    if "additionalFee" in obj:
        additional_fee = obj["additionalFee"]
        if not isinstance(additional_fee, str):
            raise ValueError(f"{repr(additional_fee)} is not str")
    else:
        additional_fee = None
    return UpdatePlatformBodySettlementFormula(platform_fee, discount_share, additional_fee)
