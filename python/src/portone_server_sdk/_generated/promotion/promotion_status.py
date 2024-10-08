from __future__ import annotations
from typing import Any, Literal, Optional

PromotionStatus = Literal["SCHEDULED", "IN_PROGRESS", "PAUSED", "BUDGET_EXHAUSTED", "TERMINATED", "COMPLETED"]


def _serialize_promotion_status(obj: PromotionStatus) -> Any:
    return obj


def _deserialize_promotion_status(obj: Any) -> PromotionStatus:
    if obj not in ["SCHEDULED", "IN_PROGRESS", "PAUSED", "BUDGET_EXHAUSTED", "TERMINATED", "COMPLETED"]:
        raise ValueError(f"{repr(obj)} is not PromotionStatus")
    return obj
