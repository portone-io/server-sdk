from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class DeleteB2bCounterpartyBody:
    """거래처 삭제 요청
    """
    pass


def _serialize_delete_b2b_counterparty_body(obj: DeleteB2bCounterpartyBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_delete_b2b_counterparty_body(obj: Any) -> DeleteB2bCounterpartyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return DeleteB2bCounterpartyBody()
