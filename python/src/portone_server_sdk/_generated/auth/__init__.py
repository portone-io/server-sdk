from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.auth.login_via_api_secret_response import LoginViaApiSecretResponse, _deserialize_login_via_api_secret_response, _serialize_login_via_api_secret_response
from portone_server_sdk._generated.auth.refresh_token_response import RefreshTokenResponse, _deserialize_refresh_token_response, _serialize_refresh_token_response
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from urllib.parse import quote
from portone_server_sdk._generated import errors
class AuthClient:
    _secret: str
    _user_agent: str
    _base_url: str
    _store_id: Optional[str]
    _client: AsyncClient

    def __init__(self, secret: str, user_agent: str, base_url: str, store_id: Optional[str]):
        self._secret = secret
        self._user_agent = user_agent
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
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_refresh_token_response(response.json())
