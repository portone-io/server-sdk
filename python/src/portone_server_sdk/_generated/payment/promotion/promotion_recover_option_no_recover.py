from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.promotion.promotion_spare_budget import PromotionSpareBudget, _deserialize_promotion_spare_budget, _serialize_promotion_spare_budget

@dataclass
class PromotionRecoverOptionNoRecover:
    """결제 취소 시 프로모션 예산 미복구
    """
    """결제 취소 시 프로모션 예산 복구 옵션
    """
    spare_budget: Optional[PromotionSpareBudget] = field(default=None)


def _serialize_promotion_recover_option_no_recover(obj: PromotionRecoverOptionNoRecover) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "NO_RECOVER"
    if obj.spare_budget is not None:
        entity["spareBudget"] = _serialize_promotion_spare_budget(obj.spare_budget)
    return entity


def _deserialize_promotion_recover_option_no_recover(obj: Any) -> PromotionRecoverOptionNoRecover:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "NO_RECOVER":
        raise ValueError(f"{repr(type)} is not 'NO_RECOVER'")
    if "spareBudget" in obj:
        spare_budget = obj["spareBudget"]
        spare_budget = _deserialize_promotion_spare_budget(spare_budget)
    else:
        spare_budget = None
    return PromotionRecoverOptionNoRecover(spare_budget)
