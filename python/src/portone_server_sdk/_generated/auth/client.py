from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ..._user_agent import USER_AGENT
from typing import Optional
from ..errors import InvalidRequestError, UnauthorizedError, UnknownError
from ..common.invalid_request_error import _deserialize_invalid_request_error
from ..common.unauthorized_error import _deserialize_unauthorized_error
from ..auth.login_via_api_secret_response import LoginViaApiSecretResponse, _deserialize_login_via_api_secret_response, _serialize_login_via_api_secret_response
from ..auth.refresh_token_response import RefreshTokenResponse, _deserialize_refresh_token_response, _serialize_refresh_token_response
from urllib.parse import quote
class AuthClient:
    _secret: str
    _base_url: str
    _store_id: Optional[str]
    _client: AsyncClient

    def __init__(self, *, secret: str, base_url: str = "https://api.portone.io", store_id: Optional[str] = None):
        """API Secret을 사용해 포트원 API 클라이언트를 생성합니다."""
        self._secret = secret
        self._base_url = base_url
        self._store_id = store_id
        self._client = AsyncClient()
    def login_via_api_secret(
        self,
        *,
        api_secret: str,
    ) -> LoginViaApiSecretResponse:
        """API secret 를 사용한 토큰 발급

        API secret 를 통해 API 인증에 사용할 토큰을 가져옵니다.

        Args:
            api_secret (str):
                발급받은 API secret


        Raises:
            LoginViaApiSecretError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["apiSecret"] = api_secret
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/login/api-secret",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_login_via_api_secret_response(response.json())
    async def login_via_api_secret_async(
        self,
        *,
        api_secret: str,
    ) -> LoginViaApiSecretResponse:
        """API secret 를 사용한 토큰 발급

        API secret 를 통해 API 인증에 사용할 토큰을 가져옵니다.

        Args:
            api_secret (str):
                발급받은 API secret


        Raises:
            LoginViaApiSecretError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["apiSecret"] = api_secret
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/login/api-secret",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_login_via_api_secret_response(response.json())
    def refresh_token(
        self,
        *,
        refresh_token: str,
    ) -> RefreshTokenResponse:
        """토큰 갱신

        리프레시 토큰을 사용해 유효기간이 연장된 새로운 토큰을 재발급합니다.

        Args:
            refresh_token (str):
                리프레시 토큰


        Raises:
            RefreshTokenError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["refreshToken"] = refresh_token
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/token/refresh",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_refresh_token_response(response.json())
    async def refresh_token_async(
        self,
        *,
        refresh_token: str,
    ) -> RefreshTokenResponse:
        """토큰 갱신

        리프레시 토큰을 사용해 유효기간이 연장된 새로운 토큰을 재발급합니다.

        Args:
            refresh_token (str):
                리프레시 토큰


        Raises:
            RefreshTokenError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["refreshToken"] = refresh_token
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/token/refresh",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_refresh_token_response(response.json())
