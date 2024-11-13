from __future__ import annotations
from typing import Any, Literal, Optional, Union

PromotionStatus = Union[Literal["SCHEDULED", "IN_PROGRESS", "PAUSED", "BUDGET_EXHAUSTED", "TERMINATED", "COMPLETED"], str]


def _serialize_promotion_status(obj: PromotionStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_promotion_status(obj: Any) -> PromotionStatus:
    return obj
