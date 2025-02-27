from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformUserDefinedFormulaResults:
    additional_properties: dict[str, int]
    """추가 데이터
    """


def _serialize_platform_user_defined_formula_results(obj: PlatformUserDefinedFormulaResults) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity.update(obj.additional_properties)
    return entity


def _deserialize_platform_user_defined_formula_results(obj: Any) -> PlatformUserDefinedFormulaResults:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    additional_properties = {}
    for key, value in obj.items():
        if key in []:
            continue
        if not isinstance(value, int):
            raise ValueError(f"{repr(value)} is not int")
        additional_properties[key] = value
    return PlatformUserDefinedFormulaResults(additional_properties)
