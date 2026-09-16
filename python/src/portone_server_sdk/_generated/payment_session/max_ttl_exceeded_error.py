from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class MaxTtlExceededError:
    """요청된 TTL이 정책 상한을 초과한 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_max_ttl_exceeded_error(obj: MaxTtlExceededError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "MAX_TTL_EXCEEDED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_max_ttl_exceeded_error(obj: Any) -> MaxTtlExceededError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "MAX_TTL_EXCEEDED":
        raise ValueError(f"{repr(type)} is not 'MAX_TTL_EXCEEDED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return MaxTtlExceededError(message)
