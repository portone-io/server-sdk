from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.counterparty.b2b_counterparty import B2bCounterparty, _deserialize_b2b_counterparty, _serialize_b2b_counterparty

@dataclass
class CreateB2bCounterpartyResponse:
    """거래처 생성 응답 정보
    """
    counterparty: B2bCounterparty
    """거래처 정보
    """


def _serialize_create_b2b_counterparty_response(obj: CreateB2bCounterpartyResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["counterparty"] = _serialize_b2b_counterparty(obj.counterparty)
    return entity


def _deserialize_create_b2b_counterparty_response(obj: Any) -> CreateB2bCounterpartyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "counterparty" not in obj:
        raise KeyError(f"'counterparty' is not in {obj}")
    counterparty = obj["counterparty"]
    counterparty = _deserialize_b2b_counterparty(counterparty)
    return CreateB2bCounterpartyResponse(counterparty)
