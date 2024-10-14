from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_settlement_formula_position import PlatformSettlementFormulaPosition, _deserialize_platform_settlement_formula_position, _serialize_platform_settlement_formula_position

@dataclass
class PlatformSettlementFormulaInvalidFunction:
    type: Literal["INVALID_FUNCTION"] = field(repr=False)
    name: str
    position: PlatformSettlementFormulaPosition


def _serialize_platform_settlement_formula_invalid_function(obj: PlatformSettlementFormulaInvalidFunction) -> Any:
    entity = {}
    entity["type"] = "INVALID_FUNCTION"
    entity["name"] = obj.name
    entity["position"] = _serialize_platform_settlement_formula_position(obj.position)
    return entity


def _deserialize_platform_settlement_formula_invalid_function(obj: Any) -> PlatformSettlementFormulaInvalidFunction:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "INVALID_FUNCTION":
        raise ValueError(f"{repr(type)} is not 'INVALID_FUNCTION'")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "position" not in obj:
        raise KeyError(f"'position' is not in {obj}")
    position = obj["position"]
    position = _deserialize_platform_settlement_formula_position(position)
    return PlatformSettlementFormulaInvalidFunction(type, name, position)
