from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_settlement_formula_position import PlatformSettlementFormulaPosition, _deserialize_platform_settlement_formula_position, _serialize_platform_settlement_formula_position

@dataclass
class PlatformSettlementFormulaInvalidSyntax:
    syntax: str
    position: PlatformSettlementFormulaPosition


def _serialize_platform_settlement_formula_invalid_syntax(obj: PlatformSettlementFormulaInvalidSyntax) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "INVALID_SYNTAX"
    entity["syntax"] = obj.syntax
    entity["position"] = _serialize_platform_settlement_formula_position(obj.position)
    return entity


def _deserialize_platform_settlement_formula_invalid_syntax(obj: Any) -> PlatformSettlementFormulaInvalidSyntax:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "INVALID_SYNTAX":
        raise ValueError(f"{repr(type)} is not 'INVALID_SYNTAX'")
    if "syntax" not in obj:
        raise KeyError(f"'syntax' is not in {obj}")
    syntax = obj["syntax"]
    if not isinstance(syntax, str):
        raise ValueError(f"{repr(syntax)} is not str")
    if "position" not in obj:
        raise KeyError(f"'position' is not in {obj}")
    position = obj["position"]
    position = _deserialize_platform_settlement_formula_position(position)
    return PlatformSettlementFormulaInvalidSyntax(syntax, position)
