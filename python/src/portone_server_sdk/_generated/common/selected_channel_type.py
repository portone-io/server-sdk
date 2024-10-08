from __future__ import annotations
from typing import Any, Literal, Optional

SelectedChannelType = Literal["LIVE", "TEST"]
"""채널 타입
"""


def _serialize_selected_channel_type(obj: SelectedChannelType) -> Any:
    return obj


def _deserialize_selected_channel_type(obj: Any) -> SelectedChannelType:
    if obj not in ["LIVE", "TEST"]:
        raise ValueError(f"{repr(obj)} is not SelectedChannelType")
    return obj
