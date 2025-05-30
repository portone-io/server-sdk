from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class Platform:
    """고객사의 플랫폼 기능 관련 정보
    """
    merchant_id: str
    """해당 플랫폼의 고객사 아이디
    """
    graphql_id: str


def _serialize_platform(obj: Platform) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["merchantId"] = obj.merchant_id
    entity["graphqlId"] = obj.graphql_id
    return entity


def _deserialize_platform(obj: Any) -> Platform:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "merchantId" not in obj:
        raise KeyError(f"'merchantId' is not in {obj}")
    merchant_id = obj["merchantId"]
    if not isinstance(merchant_id, str):
        raise ValueError(f"{repr(merchant_id)} is not str")
    if "graphqlId" not in obj:
        raise KeyError(f"'graphqlId' is not in {obj}")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError(f"{repr(graphql_id)} is not str")
    return Platform(merchant_id, graphql_id)
