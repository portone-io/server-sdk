from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformContractFilterInputKeyword:
    """검색 키워드 입력 정보

    검색 키워드 적용을 위한 옵션으로, 명시된 키워드를 포함하는 계약만 조회합니다. 하나의 하위 필드에만 값을 명시하여 요청합니다.
    """
    id: Optional[str] = field(default=None)
    """해당 값이 포함된 id 를 가진 계약만 조회합니다.
    """
    name: Optional[str] = field(default=None)
    """해당 값이 포함된 name 을 가진 계약만 조회합니다.
    """


def _serialize_platform_contract_filter_input_keyword(obj: PlatformContractFilterInputKeyword) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.name is not None:
        entity["name"] = obj.name
    return entity


def _deserialize_platform_contract_filter_input_keyword(obj: Any) -> PlatformContractFilterInputKeyword:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    return PlatformContractFilterInputKeyword(id, name)
