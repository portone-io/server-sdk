from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.platform_settlement_parameter_value import PlatformSettlementParameterValue, _deserialize_platform_settlement_parameter_value, _serialize_platform_settlement_parameter_value

@dataclass
class TransferParameters:
    additional_properties: dict[str, PlatformSettlementParameterValue]
    """추가 데이터
    """


def _serialize_transfer_parameters(obj: TransferParameters) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    for key, value in obj.additional_properties.items():
        entity[key] = _serialize_platform_settlement_parameter_value(value)
    return entity


def _deserialize_transfer_parameters(obj: Any) -> TransferParameters:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    additional_properties = {}
    for key, value in obj.items():
        if key in []:
            continue
        additional_properties[key] = _deserialize_platform_settlement_parameter_value(value)
    return TransferParameters(additional_properties)
