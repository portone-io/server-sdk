from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_settlement_formula_error import PlatformSettlementFormulaError, _deserialize_platform_settlement_formula_error, _serialize_platform_settlement_formula_error

@dataclass
class PlatformInvalidSettlementFormulaError:
    platform_fee: Optional[PlatformSettlementFormulaError] = field(default=None)
    discount_share: Optional[PlatformSettlementFormulaError] = field(default=None)
    additional_fee: Optional[PlatformSettlementFormulaError] = field(default=None)
    message: Optional[str] = field(default=None)


def _serialize_platform_invalid_settlement_formula_error(obj: PlatformInvalidSettlementFormulaError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_INVALID_SETTLEMENT_FORMULA"
    if obj.platform_fee is not None:
        entity["platformFee"] = _serialize_platform_settlement_formula_error(obj.platform_fee)
    if obj.discount_share is not None:
        entity["discountShare"] = _serialize_platform_settlement_formula_error(obj.discount_share)
    if obj.additional_fee is not None:
        entity["additionalFee"] = _serialize_platform_settlement_formula_error(obj.additional_fee)
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_invalid_settlement_formula_error(obj: Any) -> PlatformInvalidSettlementFormulaError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_INVALID_SETTLEMENT_FORMULA":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_INVALID_SETTLEMENT_FORMULA'")
    if "platformFee" in obj:
        platform_fee = obj["platformFee"]
        platform_fee = _deserialize_platform_settlement_formula_error(platform_fee)
    else:
        platform_fee = None
    if "discountShare" in obj:
        discount_share = obj["discountShare"]
        discount_share = _deserialize_platform_settlement_formula_error(discount_share)
    else:
        discount_share = None
    if "additionalFee" in obj:
        additional_fee = obj["additionalFee"]
        additional_fee = _deserialize_platform_settlement_formula_error(additional_fee)
    else:
        additional_fee = None
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformInvalidSettlementFormulaError(platform_fee, discount_share, additional_fee, message)
