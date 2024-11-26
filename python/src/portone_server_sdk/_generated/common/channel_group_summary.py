from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ChannelGroupSummary:
    """채널 그룹 정보
    """
    id: str
    """채널 그룹 아이디
    """
    name: str
    """채널 그룹 이름
    """
    is_for_test: bool
    """테스트 채널 그룹 여부
    """


def _serialize_channel_group_summary(obj: ChannelGroupSummary) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["name"] = obj.name
    entity["isForTest"] = obj.is_for_test
    return entity


def _deserialize_channel_group_summary(obj: Any) -> ChannelGroupSummary:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "isForTest" not in obj:
        raise KeyError(f"'isForTest' is not in {obj}")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError(f"{repr(is_for_test)} is not bool")
    return ChannelGroupSummary(id, name, is_for_test)
