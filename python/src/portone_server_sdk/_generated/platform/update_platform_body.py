from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_round_type import PlatformRoundType, _deserialize_platform_round_type, _serialize_platform_round_type
from ..platform.update_platform_body_settlement_formula import UpdatePlatformBodySettlementFormula, _deserialize_update_platform_body_settlement_formula, _serialize_update_platform_body_settlement_formula
from ..platform.update_platform_body_settlement_rule import UpdatePlatformBodySettlementRule, _deserialize_update_platform_body_settlement_rule, _serialize_update_platform_body_settlement_rule

@dataclass
class UpdatePlatformBody:
    """플랫폼 업데이트를 위한 입력 정보

    값이 명시되지 않은 필드는 업데이트하지 않습니다.
    """
    round_type: Optional[PlatformRoundType] = field(default=None)
    """파트너 정산금액의 소수점 처리 방식
    """
    settlement_formula: Optional[UpdatePlatformBodySettlementFormula] = field(default=None)
    """수수료 및 할인 분담 정책 관련 계산식
    """
    settlement_rule: Optional[UpdatePlatformBodySettlementRule] = field(default=None)
    """정산 규칙
    """


def _serialize_update_platform_body(obj: UpdatePlatformBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.round_type is not None:
        entity["roundType"] = _serialize_platform_round_type(obj.round_type)
    if obj.settlement_formula is not None:
        entity["settlementFormula"] = _serialize_update_platform_body_settlement_formula(obj.settlement_formula)
    if obj.settlement_rule is not None:
        entity["settlementRule"] = _serialize_update_platform_body_settlement_rule(obj.settlement_rule)
    return entity


def _deserialize_update_platform_body(obj: Any) -> UpdatePlatformBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "roundType" in obj:
        round_type = obj["roundType"]
        round_type = _deserialize_platform_round_type(round_type)
    else:
        round_type = None
    if "settlementFormula" in obj:
        settlement_formula = obj["settlementFormula"]
        settlement_formula = _deserialize_update_platform_body_settlement_formula(settlement_formula)
    else:
        settlement_formula = None
    if "settlementRule" in obj:
        settlement_rule = obj["settlementRule"]
        settlement_rule = _deserialize_update_platform_body_settlement_rule(settlement_rule)
    else:
        settlement_rule = None
    return UpdatePlatformBody(round_type, settlement_formula, settlement_rule)
