from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.platform.partner_settlement.get_platform_partner_settlements_response import GetPlatformPartnerSettlementsResponse, _deserialize_get_platform_partner_settlements_response, _serialize_get_platform_partner_settlements_response
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from portone_server_sdk._generated.platform.partner_settlement.platform_partner_settlement_filter_input import PlatformPartnerSettlementFilterInput, _deserialize_platform_partner_settlement_filter_input, _serialize_platform_partner_settlement_filter_input
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from urllib.parse import quote
from portone_server_sdk._generated import errors
class PartnerSettlementClient:
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
    def get_platform_partner_settlements(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: PlatformPartnerSettlementFilterInput,
        is_for_test: bool,
    ) -> GetPlatformPartnerSettlementsResponse:
        """정산 내역 다건 조회

        여러 정산 내역을 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보
            filter (PlatformPartnerSettlementFilterInput):
                조회할 정산내역 조건 필터
            is_for_test (bool):



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
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        request_body["filter"] = _serialize_platform_partner_settlement_filter_input(filter)
        request_body["isForTest"] = is_for_test
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/partner-settlements",
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
        return _deserialize_get_platform_partner_settlements_response(response.json())
    async def get_platform_partner_settlements_async(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: PlatformPartnerSettlementFilterInput,
        is_for_test: bool,
    ) -> GetPlatformPartnerSettlementsResponse:
        """정산 내역 다건 조회

        여러 정산 내역을 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보
            filter (PlatformPartnerSettlementFilterInput):
                조회할 정산내역 조건 필터
            is_for_test (bool):



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
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        request_body["filter"] = _serialize_platform_partner_settlement_filter_input(filter)
        request_body["isForTest"] = is_for_test
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/partner-settlements",
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
        return _deserialize_get_platform_partner_settlements_response(response.json())
