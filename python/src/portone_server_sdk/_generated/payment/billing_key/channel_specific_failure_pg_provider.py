from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class ChannelSpecificFailurePgProvider:
    """PG사에서 오류를 전달한 경우
    """
    channel: SelectedChannel
    pg_code: str
    pg_message: str
    message: Optional[str] = field(default=None)


def _serialize_channel_specific_failure_pg_provider(obj: ChannelSpecificFailurePgProvider) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PG_PROVIDER"
    entity["channel"] = _serialize_selected_channel(obj.channel)
    entity["pgCode"] = obj.pg_code
    entity["pgMessage"] = obj.pg_message
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_channel_specific_failure_pg_provider(obj: Any) -> ChannelSpecificFailurePgProvider:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PG_PROVIDER":
        raise ValueError(f"{repr(type)} is not 'PG_PROVIDER'")
    if "channel" not in obj:
        raise KeyError(f"'channel' is not in {obj}")
    channel = obj["channel"]
    channel = _deserialize_selected_channel(channel)
    if "pgCode" not in obj:
        raise KeyError(f"'pgCode' is not in {obj}")
    pg_code = obj["pgCode"]
    if not isinstance(pg_code, str):
        raise ValueError(f"{repr(pg_code)} is not str")
    if "pgMessage" not in obj:
        raise KeyError(f"'pgMessage' is not in {obj}")
    pg_message = obj["pgMessage"]
    if not isinstance(pg_message, str):
        raise ValueError(f"{repr(pg_message)} is not str")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return ChannelSpecificFailurePgProvider(channel, pg_code, pg_message, message)
