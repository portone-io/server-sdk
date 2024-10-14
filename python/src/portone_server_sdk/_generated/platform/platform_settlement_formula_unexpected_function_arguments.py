from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_settlement_formula_position import PlatformSettlementFormulaPosition, _deserialize_platform_settlement_formula_position, _serialize_platform_settlement_formula_position

@dataclass
class PlatformSettlementFormulaUnexpectedFunctionArguments:
    type: Literal["UNEXPECTED_FUNCTION_ARGUMENTS"] = field(repr=False)
    function_name: str
    expected_count: int
    """(int32)
    """
    current_count: int
    """(int32)
    """
    position: PlatformSettlementFormulaPosition


def _serialize_platform_settlement_formula_unexpected_function_arguments(obj: PlatformSettlementFormulaUnexpectedFunctionArguments) -> Any:
    entity = {}
    entity["type"] = "UNEXPECTED_FUNCTION_ARGUMENTS"
    entity["functionName"] = obj.function_name
    entity["expectedCount"] = obj.expected_count
    entity["currentCount"] = obj.current_count
    entity["position"] = _serialize_platform_settlement_formula_position(obj.position)
    return entity


def _deserialize_platform_settlement_formula_unexpected_function_arguments(obj: Any) -> PlatformSettlementFormulaUnexpectedFunctionArguments:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "UNEXPECTED_FUNCTION_ARGUMENTS":
        raise ValueError(f"{repr(type)} is not 'UNEXPECTED_FUNCTION_ARGUMENTS'")
    if "functionName" not in obj:
        raise KeyError(f"'functionName' is not in {obj}")
    function_name = obj["functionName"]
    if not isinstance(function_name, str):
        raise ValueError(f"{repr(function_name)} is not str")
    if "expectedCount" not in obj:
        raise KeyError(f"'expectedCount' is not in {obj}")
    expected_count = obj["expectedCount"]
    if not isinstance(expected_count, int):
        raise ValueError(f"{repr(expected_count)} is not int")
    if "currentCount" not in obj:
        raise KeyError(f"'currentCount' is not in {obj}")
    current_count = obj["currentCount"]
    if not isinstance(current_count, int):
        raise ValueError(f"{repr(current_count)} is not int")
    if "position" not in obj:
        raise KeyError(f"'position' is not in {obj}")
    position = obj["position"]
    position = _deserialize_platform_settlement_formula_position(position)
    return PlatformSettlementFormulaUnexpectedFunctionArguments(type, function_name, expected_count, current_count, position)
