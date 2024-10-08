from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformAdditionalFeePolicyFilterInputKeyword:
    """검색 키워드 입력 정보

    검색 키워드 적용을 위한 옵션으로, 명시된 키워드를 포함하는 추가 수수료 정책만 조회합니다. 하위 필드는 명시된 값 중 한 가지만 적용됩니다.
    """
    name: Optional[str]
    """해당 값이 포함된 name 을 가진 추가 수수료 정책만 조회합니다.
    """
    id: Optional[str]
    """해당 값이 포함된 id 를 가진 추가 수수료 정책만 조회합니다.
    """
    fee: Optional[str]
    """해당 값과 같은 수수료 를 가진 추가 수수료 정책만 조회합니다.
    """


def _serialize_platform_additional_fee_policy_filter_input_keyword(obj: PlatformAdditionalFeePolicyFilterInputKeyword) -> Any:
    entity = {}
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.fee is not None:
        entity["fee"] = obj.fee
    return entity


def _deserialize_platform_additional_fee_policy_filter_input_keyword(obj: Any) -> PlatformAdditionalFeePolicyFilterInputKeyword:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "fee" in obj:
        fee = obj["fee"]
        if not isinstance(fee, str):
            raise ValueError(f"{repr(fee)} is not str")
    else:
        fee = None
    return PlatformAdditionalFeePolicyFilterInputKeyword(name, id, fee)
