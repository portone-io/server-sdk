from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_setting import PlatformSetting, _deserialize_platform_setting, _serialize_platform_setting

@dataclass
class UpdatePlatformSettingResponse:
    """플랫폼 설정 업데이트 결과
    """
    setting: PlatformSetting


def _serialize_update_platform_setting_response(obj: UpdatePlatformSettingResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["setting"] = _serialize_platform_setting(obj.setting)
    return entity


def _deserialize_update_platform_setting_response(obj: Any) -> UpdatePlatformSettingResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "setting" not in obj:
        raise KeyError(f"'setting' is not in {obj}")
    setting = obj["setting"]
    setting = _deserialize_platform_setting(setting)
    return UpdatePlatformSettingResponse(setting)
