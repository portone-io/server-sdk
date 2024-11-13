from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PromotionRecoverOptionRecover:
    """결제 취소 시 프로모션 예산 복구
    """
    pass
    """결제 취소 시 프로모션 예산 복구 옵션
    """


def _serialize_promotion_recover_option_recover(obj: PromotionRecoverOptionRecover) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "RECOVER"
    return entity


def _deserialize_promotion_recover_option_recover(obj: Any) -> PromotionRecoverOptionRecover:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "RECOVER":
        raise ValueError(f"{repr(type)} is not 'RECOVER'")
    return PromotionRecoverOptionRecover()
