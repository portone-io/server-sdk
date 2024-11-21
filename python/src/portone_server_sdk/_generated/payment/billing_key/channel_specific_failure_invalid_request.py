from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class ChannelSpecificFailureInvalidRequest:
    """요청된 입력 정보가 유효하지 않은 경우

    허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
    """
    channel: SelectedChannel
    message: Optional[str] = field(default=None)


def _serialize_channel_specific_failure_invalid_request(obj: ChannelSpecificFailureInvalidRequest) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "INVALID_REQUEST"
    entity["channel"] = _serialize_selected_channel(obj.channel)
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_channel_specific_failure_invalid_request(obj: Any) -> ChannelSpecificFailureInvalidRequest:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "INVALID_REQUEST":
        raise ValueError(f"{repr(type)} is not 'INVALID_REQUEST'")
    if "channel" not in obj:
        raise KeyError(f"'channel' is not in {obj}")
    channel = obj["channel"]
    channel = _deserialize_selected_channel(channel)
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return ChannelSpecificFailureInvalidRequest(channel, message)
