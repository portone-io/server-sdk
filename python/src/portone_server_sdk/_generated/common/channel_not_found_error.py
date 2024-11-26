from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ChannelNotFoundError:
    """요청된 채널이 존재하지 않는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_channel_not_found_error(obj: ChannelNotFoundError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "CHANNEL_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_channel_not_found_error(obj: Any) -> ChannelNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "CHANNEL_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'CHANNEL_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return ChannelNotFoundError(message)
