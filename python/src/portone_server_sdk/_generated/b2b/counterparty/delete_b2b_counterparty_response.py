from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class DeleteB2bCounterpartyResponse:
    """거래처 삭제 응답
    """
    pass


def _serialize_delete_b2b_counterparty_response(obj: DeleteB2bCounterpartyResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_delete_b2b_counterparty_response(obj: Any) -> DeleteB2bCounterpartyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return DeleteB2bCounterpartyResponse()
