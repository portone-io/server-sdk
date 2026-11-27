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
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["apiSecret"] = obj.api_secret
    return entity


def _deserialize_login_via_api_secret_body(obj: Any) -> LoginViaApiSecretBody:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "apiSecret" not in obj:
        raise KeyError("Missing required field 'apiSecret'")
    api_secret = obj["apiSecret"]
    if not isinstance(api_secret, str):
        raise ValueError("Expected str for api_secret")
    return LoginViaApiSecretBody(api_secret)
