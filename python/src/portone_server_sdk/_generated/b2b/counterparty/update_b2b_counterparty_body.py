from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.counterparty.b2b_counterparty_create_options import B2bCounterpartyCreateOptions, _deserialize_b2b_counterparty_create_options, _serialize_b2b_counterparty_create_options
from ...b2b.counterparty.b2b_counterparty_input import B2bCounterpartyInput, _deserialize_b2b_counterparty_input, _serialize_b2b_counterparty_input

@dataclass
class UpdateB2bCounterpartyBody:
    """거래처 정보 수정 요청
    """
    counterparty: B2bCounterpartyInput
    """거래처 정보
    """
    options: Optional[B2bCounterpartyCreateOptions] = field(default=None)
    """확인 옵션

    사업자 정보 및 휴폐업 상태 조회 옵션입니다.
    """


def _serialize_update_b2b_counterparty_body(obj: UpdateB2bCounterpartyBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["counterparty"] = _serialize_b2b_counterparty_input(obj.counterparty)
    if obj.options is not None:
        entity["options"] = _serialize_b2b_counterparty_create_options(obj.options)
    return entity


def _deserialize_update_b2b_counterparty_body(obj: Any) -> UpdateB2bCounterpartyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "counterparty" not in obj:
        raise KeyError(f"'counterparty' is not in {obj}")
    counterparty = obj["counterparty"]
    counterparty = _deserialize_b2b_counterparty_input(counterparty)
    if "options" in obj:
        options = obj["options"]
        options = _deserialize_b2b_counterparty_create_options(options)
    else:
        options = None
    return UpdateB2bCounterpartyBody(counterparty, options)
