from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class GetB2bContactIdExistenceResponse:
    """담당자 ID 존재 여부 응답 정보
    """
    exists: bool
    """존재 여부
    """


def _serialize_get_b2b_contact_id_existence_response(obj: GetB2bContactIdExistenceResponse) -> Any:
    entity = {}
    entity["exists"] = obj.exists
    return entity


def _deserialize_get_b2b_contact_id_existence_response(obj: Any) -> GetB2bContactIdExistenceResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "exists" not in obj:
        raise KeyError(f"'exists' is not in {obj}")
    exists = obj["exists"]
    if not isinstance(exists, bool):
        raise ValueError(f"{repr(exists)} is not bool")
    return GetB2bContactIdExistenceResponse(exists)
