from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.company.b2b_business_info_result import B2bBusinessInfoResult, _deserialize_b2b_business_info_result, _serialize_b2b_business_info_result

@dataclass
class GetB2bBusinessInfosResponse:
    """사업자등록 정보 조회 성공 응답
    """
    result: list[B2bBusinessInfoResult]
    """사업자등록 정보 리스트
    """


def _serialize_get_b2b_business_infos_response(obj: GetB2bBusinessInfosResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["result"] = list(map(_serialize_b2b_business_info_result, obj.result))
    return entity


def _deserialize_get_b2b_business_infos_response(obj: Any) -> GetB2bBusinessInfosResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "result" not in obj:
        raise KeyError(f"'result' is not in {obj}")
    result = obj["result"]
    if not isinstance(result, list):
        raise ValueError(f"{repr(result)} is not list")
    for i, item in enumerate(result):
        item = _deserialize_b2b_business_info_result(item)
        result[i] = item
    return GetB2bBusinessInfosResponse(result)
