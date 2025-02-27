from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.update_platform_body_settlement_rule import UpdatePlatformBodySettlementRule, _deserialize_update_platform_body_settlement_rule, _serialize_update_platform_body_settlement_rule

@dataclass
class UpdatePlatformBody:
    """플랫폼 업데이트를 위한 입력 정보

    값이 명시되지 않은 필드는 업데이트하지 않습니다.
    """
    settlement_rule: Optional[UpdatePlatformBodySettlementRule] = field(default=None)
    """정산 규칙
    """


def _serialize_update_platform_body(obj: UpdatePlatformBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.settlement_rule is not None:
        entity["settlementRule"] = _serialize_update_platform_body_settlement_rule(obj.settlement_rule)
    return entity


def _deserialize_update_platform_body(obj: Any) -> UpdatePlatformBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "settlementRule" in obj:
        settlement_rule = obj["settlementRule"]
        settlement_rule = _deserialize_update_platform_body_settlement_rule(settlement_rule)
    else:
        settlement_rule = None
    return UpdatePlatformBody(settlement_rule)
