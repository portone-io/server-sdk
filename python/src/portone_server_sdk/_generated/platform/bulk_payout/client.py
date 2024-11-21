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
from ...platform.bulk_payout.get_platform_bulk_payouts_response import GetPlatformBulkPayoutsResponse, _deserialize_get_platform_bulk_payouts_response, _serialize_get_platform_bulk_payouts_response
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...platform.bulk_payout.platform_bulk_payout_filter_input import PlatformBulkPayoutFilterInput, _deserialize_platform_bulk_payout_filter_input, _serialize_platform_bulk_payout_filter_input
from urllib.parse import quote
class BulkPayoutClient:
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
    def get_platform_bulk_payouts(
        self,
        *,
        is_for_test: Optional[bool] = None,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformBulkPayoutFilterInput] = None,
    ) -> GetPlatformBulkPayoutsResponse:
        """일괄 지급 내역 다건 조회

        성공 응답으로 조회된 일괄 지급 내역 리스트와 페이지 정보 및 상태 별 개수 정보를 반환합니다.

        Args:
            is_for_test (bool, optional):

            page (PageInput, optional):

            filter (PlatformBulkPayoutFilterInput, optional):



        Raises:
            GetPlatformBulkPayoutsError
        """
        request_body = {}
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_bulk_payout_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/bulk-payouts",
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
        return _deserialize_get_platform_bulk_payouts_response(response.json())
    async def get_platform_bulk_payouts_async(
        self,
        *,
        is_for_test: Optional[bool] = None,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformBulkPayoutFilterInput] = None,
    ) -> GetPlatformBulkPayoutsResponse:
        """일괄 지급 내역 다건 조회

        성공 응답으로 조회된 일괄 지급 내역 리스트와 페이지 정보 및 상태 별 개수 정보를 반환합니다.

        Args:
            is_for_test (bool, optional):

            page (PageInput, optional):

            filter (PlatformBulkPayoutFilterInput, optional):



        Raises:
            GetPlatformBulkPayoutsError
        """
        request_body = {}
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_bulk_payout_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/bulk-payouts",
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
        return _deserialize_get_platform_bulk_payouts_response(response.json())
