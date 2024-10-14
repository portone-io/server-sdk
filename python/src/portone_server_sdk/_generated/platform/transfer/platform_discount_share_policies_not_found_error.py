from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformDiscountSharePoliciesNotFoundError:
    type: Literal["PLATFORM_DISCOUNT_SHARE_POLICIES_NOT_FOUND"] = field(repr=False)
    ids: list[str]
    graphql_ids: list[str]
    message: Optional[str]


def _serialize_platform_discount_share_policies_not_found_error(obj: PlatformDiscountSharePoliciesNotFoundError) -> Any:
    entity = {}
    entity["type"] = obj.type
    entity["ids"] = obj.ids
    entity["graphqlIds"] = obj.graphql_ids
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_discount_share_policies_not_found_error(obj: Any) -> PlatformDiscountSharePoliciesNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_DISCOUNT_SHARE_POLICIES_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_DISCOUNT_SHARE_POLICIES_NOT_FOUND'")
    if "ids" not in obj:
        raise KeyError(f"'ids' is not in {obj}")
    ids = obj["ids"]
    if not isinstance(ids, list):
        raise ValueError(f"{repr(ids)} is not list")
    for i, item in enumerate(ids):
        if not isinstance(item, str):
            raise ValueError(f"{repr(item)} is not str")
    if "graphqlIds" not in obj:
        raise KeyError(f"'graphqlIds' is not in {obj}")
    graphql_ids = obj["graphqlIds"]
    if not isinstance(graphql_ids, list):
        raise ValueError(f"{repr(graphql_ids)} is not list")
    for i, item in enumerate(graphql_ids):
        if not isinstance(item, str):
            raise ValueError(f"{repr(item)} is not str")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformDiscountSharePoliciesNotFoundError(type, ids, graphql_ids, message)