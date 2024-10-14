from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_settlement_formula_position import PlatformSettlementFormulaPosition, _deserialize_platform_settlement_formula_position, _serialize_platform_settlement_formula_position

@dataclass
class PlatformSettlementFormulaInvalidOperator:
    type: Literal["INVALID_OPERATOR"] = field(repr=False)
    operator: str
    position: PlatformSettlementFormulaPosition


def _serialize_platform_settlement_formula_invalid_operator(obj: PlatformSettlementFormulaInvalidOperator) -> Any:
    entity = {}
    entity["type"] = "INVALID_OPERATOR"
    entity["operator"] = obj.operator
    entity["position"] = _serialize_platform_settlement_formula_position(obj.position)
    return entity


def _deserialize_platform_settlement_formula_invalid_operator(obj: Any) -> PlatformSettlementFormulaInvalidOperator:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "INVALID_OPERATOR":
        raise ValueError(f"{repr(type)} is not 'INVALID_OPERATOR'")
    if "operator" not in obj:
        raise KeyError(f"'operator' is not in {obj}")
    operator = obj["operator"]
    if not isinstance(operator, str):
        raise ValueError(f"{repr(operator)} is not str")
    if "position" not in obj:
        raise KeyError(f"'position' is not in {obj}")
    position = obj["position"]
    position = _deserialize_platform_settlement_formula_position(position)
    return PlatformSettlementFormulaInvalidOperator(type, operator, position)
