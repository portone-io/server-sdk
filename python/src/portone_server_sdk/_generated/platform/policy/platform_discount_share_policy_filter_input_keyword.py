from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformDiscountSharePolicyFilterInputKeyword:
    """검색 키워드 입력 정보

    검색 키워드 적용을 위한 옵션으로, 명시된 키워드를 포함하는 할인 분담 정책만 조회합니다. 하위 필드는 명시된 값 중 한 가지만 적용됩니다.
    """
    id: Optional[str] = field(default=None)
    """해당 값이 포함된 id 를 가진 할인 분담 정책만 조회합니다.
    """
    name: Optional[str] = field(default=None)
    """해당 값이 포함된 name 을 가진 할인 분담만 조회합니다.
    """


def _serialize_platform_discount_share_policy_filter_input_keyword(obj: PlatformDiscountSharePolicyFilterInputKeyword) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.name is not None:
        entity["name"] = obj.name
    return entity


def _deserialize_platform_discount_share_policy_filter_input_keyword(obj: Any) -> PlatformDiscountSharePolicyFilterInputKeyword:
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
    return PlatformDiscountSharePolicyFilterInputKeyword(id, name)
