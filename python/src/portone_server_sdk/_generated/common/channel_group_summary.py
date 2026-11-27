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
        raise ValueError("Expected dict for obj")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "name" not in obj:
        raise KeyError("Missing required field 'name'")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError("Expected str for name")
    if "isForTest" not in obj:
        raise KeyError("Missing required field 'isForTest'")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError("Expected bool for is_for_test")
    return ChannelGroupSummary(id, name, is_for_test)
