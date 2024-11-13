from __future__ import annotations
from typing import Any, Literal, Optional, Union

SelectedChannelType = Union[Literal["LIVE", "TEST"], str]
"""채널 타입
"""


def _serialize_selected_channel_type(obj: SelectedChannelType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_selected_channel_type(obj: Any) -> SelectedChannelType:
    return obj
