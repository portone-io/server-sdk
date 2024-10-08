from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class LoginViaApiSecretBody:
    """API Secret 로그인을 위한 입력 정보
    """
    api_secret: str
    """발급받은 API secret
    """


def _serialize_login_via_api_secret_body(obj: LoginViaApiSecretBody) -> Any:
    entity = {}
    entity["apiSecret"] = obj.api_secret
    return entity


def _deserialize_login_via_api_secret_body(obj: Any) -> LoginViaApiSecretBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "apiSecret" not in obj:
        raise KeyError(f"'apiSecret' is not in {obj}")
    api_secret = obj["apiSecret"]
    if not isinstance(api_secret, str):
        raise ValueError(f"{repr(api_secret)} is not str")
    return LoginViaApiSecretBody(api_secret)
