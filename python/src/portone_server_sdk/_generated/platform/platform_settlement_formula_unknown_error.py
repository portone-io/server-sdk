from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementFormulaUnknownError:
    type: Literal["UNKNOWN_ERROR"] = field(repr=False)


def _serialize_platform_settlement_formula_unknown_error(obj: PlatformSettlementFormulaUnknownError) -> Any:
    entity = {}
    entity["type"] = "UNKNOWN_ERROR"
    return entity


def _deserialize_platform_settlement_formula_unknown_error(obj: Any) -> PlatformSettlementFormulaUnknownError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "UNKNOWN_ERROR":
        raise ValueError(f"{repr(type)} is not 'UNKNOWN_ERROR'")
    return PlatformSettlementFormulaUnknownError(type)
