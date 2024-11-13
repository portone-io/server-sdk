from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementFormulaPosition:
    start_line: int
    """(int32)
    """
    start_index: int
    """(int32)
    """
    end_line: int
    """(int32)
    """
    end_index: int
    """(int32)
    """


def _serialize_platform_settlement_formula_position(obj: PlatformSettlementFormulaPosition) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["startLine"] = obj.start_line
    entity["startIndex"] = obj.start_index
    entity["endLine"] = obj.end_line
    entity["endIndex"] = obj.end_index
    return entity


def _deserialize_platform_settlement_formula_position(obj: Any) -> PlatformSettlementFormulaPosition:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "startLine" not in obj:
        raise KeyError(f"'startLine' is not in {obj}")
    start_line = obj["startLine"]
    if not isinstance(start_line, int):
        raise ValueError(f"{repr(start_line)} is not int")
    if "startIndex" not in obj:
        raise KeyError(f"'startIndex' is not in {obj}")
    start_index = obj["startIndex"]
    if not isinstance(start_index, int):
        raise ValueError(f"{repr(start_index)} is not int")
    if "endLine" not in obj:
        raise KeyError(f"'endLine' is not in {obj}")
    end_line = obj["endLine"]
    if not isinstance(end_line, int):
        raise ValueError(f"{repr(end_line)} is not int")
    if "endIndex" not in obj:
        raise KeyError(f"'endIndex' is not in {obj}")
    end_index = obj["endIndex"]
    if not isinstance(end_index, int):
        raise ValueError(f"{repr(end_index)} is not int")
    return PlatformSettlementFormulaPosition(start_line, start_index, end_line, end_index)
