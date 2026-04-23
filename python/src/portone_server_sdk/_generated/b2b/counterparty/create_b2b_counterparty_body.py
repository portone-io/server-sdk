from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.counterparty.b2b_counterparty_create_options import B2bCounterpartyCreateOptions, _deserialize_b2b_counterparty_create_options, _serialize_b2b_counterparty_create_options
from ...b2b.counterparty.b2b_counterparty_input import B2bCounterpartyInput, _deserialize_b2b_counterparty_input, _serialize_b2b_counterparty_input

@dataclass
class CreateB2bCounterpartyBody:
    """거래처 생성 요청 정보
    """
    counterparty: B2bCounterpartyInput
    """거래처 정보
    """
    counterparty_id: Optional[str] = field(default=None)
    """거래처 아이디

    입력하지 않으면 임의의 ID가 채번됩니다.
    """
    options: Optional[B2bCounterpartyCreateOptions] = field(default=None)
    """거래처 생성 옵션
    """


def _serialize_create_b2b_counterparty_body(obj: CreateB2bCounterpartyBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["counterparty"] = _serialize_b2b_counterparty_input(obj.counterparty)
    if obj.counterparty_id is not None:
        entity["counterpartyId"] = obj.counterparty_id
    if obj.options is not None:
        entity["options"] = _serialize_b2b_counterparty_create_options(obj.options)
    return entity


def _deserialize_create_b2b_counterparty_body(obj: Any) -> CreateB2bCounterpartyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "counterparty" not in obj:
        raise KeyError(f"'counterparty' is not in {obj}")
    counterparty = obj["counterparty"]
    counterparty = _deserialize_b2b_counterparty_input(counterparty)
    if "counterpartyId" in obj:
        counterparty_id = obj["counterpartyId"]
        if not isinstance(counterparty_id, str):
            raise ValueError(f"{repr(counterparty_id)} is not str")
    else:
        counterparty_id = None
    if "options" in obj:
        options = obj["options"]
        options = _deserialize_b2b_counterparty_create_options(options)
    else:
        options = None
    return CreateB2bCounterpartyBody(counterparty, counterparty_id, options)
