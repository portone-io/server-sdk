from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_settlement_formula_position import PlatformSettlementFormulaPosition, _deserialize_platform_settlement_formula_position, _serialize_platform_settlement_formula_position

@dataclass
class PlatformSettlementFormulaUnsupportedVariable:
    type: Literal["UNSUPPORTED_VARIABLE"] = field(repr=False)
    name: str
    position: PlatformSettlementFormulaPosition


def _serialize_platform_settlement_formula_unsupported_variable(obj: PlatformSettlementFormulaUnsupportedVariable) -> Any:
    entity = {}
    entity["type"] = "UNSUPPORTED_VARIABLE"
    entity["name"] = obj.name
    entity["position"] = _serialize_platform_settlement_formula_position(obj.position)
    return entity


def _deserialize_platform_settlement_formula_unsupported_variable(obj: Any) -> PlatformSettlementFormulaUnsupportedVariable:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "UNSUPPORTED_VARIABLE":
        raise ValueError(f"{repr(type)} is not 'UNSUPPORTED_VARIABLE'")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "position" not in obj:
        raise KeyError(f"'position' is not in {obj}")
    position = obj["position"]
    position = _deserialize_platform_settlement_formula_position(position)
    return PlatformSettlementFormulaUnsupportedVariable(type, name, position)
