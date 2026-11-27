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
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PG_PROVIDER":
        raise ValueError("Expected 'PG_PROVIDER' for type")
    if "channel" not in obj:
        raise KeyError("Missing required field 'channel'")
    channel = obj["channel"]
    channel = _deserialize_selected_channel(channel)
    if "pgCode" not in obj:
        raise KeyError("Missing required field 'pgCode'")
    pg_code = obj["pgCode"]
    if not isinstance(pg_code, str):
        raise ValueError("Expected str for pg_code")
    if "pgMessage" not in obj:
        raise KeyError("Missing required field 'pgMessage'")
    pg_message = obj["pgMessage"]
    if not isinstance(pg_message, str):
        raise ValueError("Expected str for pg_message")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return ChannelSpecificFailurePgProvider(channel, pg_code, pg_message, message)
