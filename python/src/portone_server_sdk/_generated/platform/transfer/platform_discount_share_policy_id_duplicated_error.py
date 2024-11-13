from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformDiscountSharePolicyIdDuplicatedError:
    id: str
    graphql_id: str
    message: Optional[str] = field(default=None)


def _serialize_platform_discount_share_policy_id_duplicated_error(obj: PlatformDiscountSharePolicyIdDuplicatedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_DISCOUNT_SHARE_POLICY_ID_DUPLICATED"
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_discount_share_policy_id_duplicated_error(obj: Any) -> PlatformDiscountSharePolicyIdDuplicatedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_DISCOUNT_SHARE_POLICY_ID_DUPLICATED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_DISCOUNT_SHARE_POLICY_ID_DUPLICATED'")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "graphqlId" not in obj:
        raise KeyError(f"'graphqlId' is not in {obj}")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError(f"{repr(graphql_id)} is not str")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformDiscountSharePolicyIdDuplicatedError(id, graphql_id, message)
