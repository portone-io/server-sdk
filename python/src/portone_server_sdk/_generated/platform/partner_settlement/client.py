from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import ForbiddenError, InvalidRequestError, PlatformNotEnabledError, UnauthorizedError, UnknownError
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...platform.platform_not_enabled_error import _deserialize_platform_not_enabled_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...platform.partner_settlement.get_platform_partner_settlements_response import GetPlatformPartnerSettlementsResponse, _deserialize_get_platform_partner_settlements_response, _serialize_get_platform_partner_settlements_response
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...platform.partner_settlement.platform_partner_settlement_filter_input import PlatformPartnerSettlementFilterInput, _deserialize_platform_partner_settlement_filter_input, _serialize_platform_partner_settlement_filter_input
from urllib.parse import quote
class PartnerSettlementClient:
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
            GetPlatformPartnerSettlementsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            GetPlatformPartnerSettlementsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_get_platform_partner_settlements_response(response.json())
