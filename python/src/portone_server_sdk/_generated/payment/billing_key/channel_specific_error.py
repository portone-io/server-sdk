from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.billing_key.channel_specific_failure import ChannelSpecificFailure, _deserialize_channel_specific_failure, _serialize_channel_specific_failure
from portone_server_sdk._generated.common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class ChannelSpecificError:
    """여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
    """
    type: Literal["CHANNEL_SPECIFIC"] = field(repr=False)
    failures: list[ChannelSpecificFailure]
    succeeded_channels: list[SelectedChannel]
    """(결제, 본인인증 등에) 선택된 채널 정보
    """
    message: Optional[str]


def _serialize_channel_specific_error(obj: ChannelSpecificError) -> Any:
    entity = {}
    entity["type"] = "CHANNEL_SPECIFIC"
    entity["failures"] = list(map(_serialize_channel_specific_failure, obj.failures))
    entity["succeededChannels"] = list(map(_serialize_selected_channel, obj.succeeded_channels))
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_channel_specific_error(obj: Any) -> ChannelSpecificError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "CHANNEL_SPECIFIC":
        raise ValueError(f"{repr(type)} is not 'CHANNEL_SPECIFIC'")
    if "failures" not in obj:
        raise KeyError(f"'failures' is not in {obj}")
    failures = obj["failures"]
    if not isinstance(failures, list):
        raise ValueError(f"{repr(failures)} is not list")
    for i, item in enumerate(failures):
        item = _deserialize_channel_specific_failure(item)
        failures[i] = item
    if "succeededChannels" not in obj:
        raise KeyError(f"'succeededChannels' is not in {obj}")
    succeeded_channels = obj["succeededChannels"]
    if not isinstance(succeeded_channels, list):
        raise ValueError(f"{repr(succeeded_channels)} is not list")
    for i, item in enumerate(succeeded_channels):
        item = _deserialize_selected_channel(item)
        succeeded_channels[i] = item
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return ChannelSpecificError(type, failures, succeeded_channels, message)
