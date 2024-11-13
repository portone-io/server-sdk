from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class RefreshTokenBody:
    """토큰 재발급을 위한 입력 정보
    """
    refresh_token: str
    """리프레시 토큰
    """


def _serialize_refresh_token_body(obj: RefreshTokenBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["refreshToken"] = obj.refresh_token
    return entity


def _deserialize_refresh_token_body(obj: Any) -> RefreshTokenBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "refreshToken" not in obj:
        raise KeyError(f"'refreshToken' is not in {obj}")
    refresh_token = obj["refreshToken"]
    if not isinstance(refresh_token, str):
        raise ValueError(f"{repr(refresh_token)} is not str")
    return RefreshTokenBody(refresh_token)
