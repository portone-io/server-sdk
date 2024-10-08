from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class LoginViaApiSecretResponse:
    """API key 로그인 성공 응답
    """
    access_token: str
    """인증에 사용하는 엑세스 토큰

    하루의 유효기간을 가지고 있습니다.
    """
    refresh_token: str
    """토큰 재발급 및 유효기간 연장을 위해 사용하는 리프레시 토큰

    일주일의 유효기간을 가지고 있으며, 리프레시 토큰을 통해 유효기간이 연장된 새로운 엑세스 토큰을 발급받을 수 있습니다.
    """


def _serialize_login_via_api_secret_response(obj: LoginViaApiSecretResponse) -> Any:
    entity = {}
    entity["accessToken"] = obj.access_token
    entity["refreshToken"] = obj.refresh_token
    return entity


def _deserialize_login_via_api_secret_response(obj: Any) -> LoginViaApiSecretResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "accessToken" not in obj:
        raise KeyError(f"'accessToken' is not in {obj}")
    access_token = obj["accessToken"]
    if not isinstance(access_token, str):
        raise ValueError(f"{repr(access_token)} is not str")
    if "refreshToken" not in obj:
        raise KeyError(f"'refreshToken' is not in {obj}")
    refresh_token = obj["refreshToken"]
    if not isinstance(refresh_token, str):
        raise ValueError(f"{repr(refresh_token)} is not str")
    return LoginViaApiSecretResponse(access_token, refresh_token)
