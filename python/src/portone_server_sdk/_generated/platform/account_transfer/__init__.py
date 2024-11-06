from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.platform.account_transfer.get_platform_account_transfers_response import GetPlatformAccountTransfersResponse, _deserialize_get_platform_account_transfers_response, _serialize_get_platform_account_transfers_response
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from portone_server_sdk._generated.platform.account_transfer.platform_account_transfer_filter import PlatformAccountTransferFilter, _deserialize_platform_account_transfer_filter, _serialize_platform_account_transfer_filter
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from urllib.parse import quote
from portone_server_sdk._generated import errors
class AccountTransferClient:
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
    def get_platform_account_transfers(
        self,
        *,
        is_for_test: Optional[bool] = None,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformAccountTransferFilter] = None,
    ) -> GetPlatformAccountTransfersResponse:
        """이체 내역 다건 조회

        여러 이체 내역을 조회합니다.

        Args:
            is_for_test (bool, optional):

            page (PageInput, optional):

            filter (PlatformAccountTransferFilter, optional):



        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_account_transfer_filter(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/account-transfers",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_platform_account_transfers_response(response.json())
    async def get_platform_account_transfers_async(
        self,
        *,
        is_for_test: Optional[bool] = None,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformAccountTransferFilter] = None,
    ) -> GetPlatformAccountTransfersResponse:
        """이체 내역 다건 조회

        여러 이체 내역을 조회합니다.

        Args:
            is_for_test (bool, optional):

            page (PageInput, optional):

            filter (PlatformAccountTransferFilter, optional):



        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_account_transfer_filter(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/account-transfers",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_platform_account_transfers_response(response.json())
