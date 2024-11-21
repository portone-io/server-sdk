from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform import Platform, _deserialize_platform, _serialize_platform

@dataclass
class UpdatePlatformResponse:
    """플랫폼 업데이트 결과 정보
    """
    platform: Platform
    """업데이트된 플랫폼 정보
    """


def _serialize_update_platform_response(obj: UpdatePlatformResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["platform"] = _serialize_platform(obj.platform)
    return entity


def _deserialize_update_platform_response(obj: Any) -> UpdatePlatformResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "platform" not in obj:
        raise KeyError(f"'platform' is not in {obj}")
    platform = obj["platform"]
    platform = _deserialize_platform(platform)
    return UpdatePlatformResponse(platform)
