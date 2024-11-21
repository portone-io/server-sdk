from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.platform_settlement_parameter_value import PlatformSettlementParameterValue, _deserialize_platform_settlement_parameter_value, _serialize_platform_settlement_parameter_value

@dataclass
class TransferParameters(PlatformSettlementParameterValue):
    pass


def _serialize_transfer_parameters(obj: TransferParameters) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = _serialize_platform_settlement_parameter_value(obj)
    return entity


def _deserialize_transfer_parameters(obj: Any) -> TransferParameters:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    additional = _deserialize_platform_settlement_parameter_value(obj)
    decimal = additional.decimal
    decimal_scale = additional.decimal_scale
    return TransferParameters(decimal, decimal_scale)
