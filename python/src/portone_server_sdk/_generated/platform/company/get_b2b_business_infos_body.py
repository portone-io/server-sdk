from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class GetB2bBusinessInfosBody:
    """사업자등록 정보 조회를 위한 입력 정보
    """
    brn_list: list[str]
    """조회할 사업자등록번호 리스트
    """


def _serialize_get_b2b_business_infos_body(obj: GetB2bBusinessInfosBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["brnList"] = obj.brn_list
    return entity


def _deserialize_get_b2b_business_infos_body(obj: Any) -> GetB2bBusinessInfosBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "brnList" not in obj:
        raise KeyError(f"'brnList' is not in {obj}")
    brn_list = obj["brnList"]
    if not isinstance(brn_list, list):
        raise ValueError(f"{repr(brn_list)} is not list")
    for i, item in enumerate(brn_list):
        if not isinstance(item, str):
            raise ValueError(f"{repr(item)} is not str")
    return GetB2bBusinessInfosBody(brn_list)
