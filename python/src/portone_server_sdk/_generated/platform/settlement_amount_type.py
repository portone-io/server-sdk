from __future__ import annotations
from typing import Any, Literal, Optional, Union

SettlementAmountType = Union[Literal["NET", "GROSS"], str]


def _serialize_settlement_amount_type(obj: SettlementAmountType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_settlement_amount_type(obj: Any) -> SettlementAmountType:
    return obj
