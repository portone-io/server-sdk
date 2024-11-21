from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_round_type import PlatformRoundType, _deserialize_platform_round_type, _serialize_platform_round_type
from ..platform.platform_settlement_formula import PlatformSettlementFormula, _deserialize_platform_settlement_formula, _serialize_platform_settlement_formula
from ..platform.platform_settlement_rule import PlatformSettlementRule, _deserialize_platform_settlement_rule, _serialize_platform_settlement_rule

@dataclass
class Platform:
    """고객사의 플랫폼 기능 관련 정보
    """
    merchant_id: str
    """해당 플랫폼의 고객사 아이디
    """
    graphql_id: str
    round_type: PlatformRoundType
    """파트너 정산금액의 소수점 처리 방식
    """
    settlement_formula: PlatformSettlementFormula
    """수수료 및 할인 분담 정책 관련 계산식
    """
    settlement_rule: PlatformSettlementRule
    """정산 규칙
    """


def _serialize_platform(obj: Platform) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["merchantId"] = obj.merchant_id
    entity["graphqlId"] = obj.graphql_id
    entity["roundType"] = _serialize_platform_round_type(obj.round_type)
    entity["settlementFormula"] = _serialize_platform_settlement_formula(obj.settlement_formula)
    entity["settlementRule"] = _serialize_platform_settlement_rule(obj.settlement_rule)
    return entity


def _deserialize_platform(obj: Any) -> Platform:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "merchantId" not in obj:
        raise KeyError(f"'merchantId' is not in {obj}")
    merchant_id = obj["merchantId"]
    if not isinstance(merchant_id, str):
        raise ValueError(f"{repr(merchant_id)} is not str")
    if "graphqlId" not in obj:
        raise KeyError(f"'graphqlId' is not in {obj}")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError(f"{repr(graphql_id)} is not str")
    if "roundType" not in obj:
        raise KeyError(f"'roundType' is not in {obj}")
    round_type = obj["roundType"]
    round_type = _deserialize_platform_round_type(round_type)
    if "settlementFormula" not in obj:
        raise KeyError(f"'settlementFormula' is not in {obj}")
    settlement_formula = obj["settlementFormula"]
    settlement_formula = _deserialize_platform_settlement_formula(settlement_formula)
    if "settlementRule" not in obj:
        raise KeyError(f"'settlementRule' is not in {obj}")
    settlement_rule = obj["settlementRule"]
    settlement_rule = _deserialize_platform_settlement_rule(settlement_rule)
    return Platform(merchant_id, graphql_id, round_type, settlement_formula, settlement_rule)
