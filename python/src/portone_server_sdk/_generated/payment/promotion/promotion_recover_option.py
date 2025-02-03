from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.promotion.promotion_recover_option_no_recover import PromotionRecoverOptionNoRecover, _deserialize_promotion_recover_option_no_recover, _serialize_promotion_recover_option_no_recover
from ...payment.promotion.promotion_recover_option_recover import PromotionRecoverOptionRecover, _deserialize_promotion_recover_option_recover, _serialize_promotion_recover_option_recover

PromotionRecoverOption = Union[PromotionRecoverOptionNoRecover, PromotionRecoverOptionRecover, dict]


def _serialize_promotion_recover_option(obj: PromotionRecoverOption) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, PromotionRecoverOptionNoRecover):
        return _serialize_promotion_recover_option_no_recover(obj)
    if isinstance(obj, PromotionRecoverOptionRecover):
        return _serialize_promotion_recover_option_recover(obj)


def _deserialize_promotion_recover_option(obj: Any) -> PromotionRecoverOption:
    try:
        return _deserialize_promotion_recover_option_no_recover(obj)
    except Exception:
        pass
    try:
        return _deserialize_promotion_recover_option_recover(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PromotionRecoverOption")
