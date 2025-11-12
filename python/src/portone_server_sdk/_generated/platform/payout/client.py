from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import ForbiddenError, InvalidRequestError, PlatformNotEnabledError, UnauthorizedError, UnknownError
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...platform.platform_not_enabled_error import _deserialize_platform_not_enabled_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...platform.payout.get_platform_payouts_response import GetPlatformPayoutsResponse, _deserialize_get_platform_payouts_response, _serialize_get_platform_payouts_response
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...platform.payout.platform_payout_filter_input import PlatformPayoutFilterInput, _deserialize_platform_payout_filter_input, _serialize_platform_payout_filter_input
from urllib.parse import quote
class PayoutClient:
    _secret: str
    _base_url: str
    _store_id: Optional[str]
    _async_client: AsyncClient
    _sync_client: SyncClient

    def __init__(self, *, secret: str, base_url: str = "https://api.portone.io", store_id: Optional[str] = None):
        """
        API Secret을 사용해 포트원 API 클라이언트를 생성합니다.

        Args:
            secret (str): 포트원 API Secret입니다.
            base_url (str, optional): 포트원 REST API 주소입니다. 기본값은 `"https://api.portone.io"`입니다.
            store_id: 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.
            """
        self._secret = secret
        self._base_url = base_url
        self._store_id = store_id
        self._async_client = AsyncClient(timeout=60.0)
        self._sync_client = SyncClient(timeout=60.0)
    def get_platform_payouts(
        self,
        *,
        test: Optional[bool] = None,
        is_for_test: Optional[bool] = None,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformPayoutFilterInput] = None,
    ) -> GetPlatformPayoutsResponse:
        """지급 내역 다건 조회

        여러 지급 내역을 조회합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            is_for_test (bool, optional):
                Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
                Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            page (PageInput, optional):

            filter (PlatformPayoutFilterInput, optional):



        Raises:
            GetPlatformPayoutsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_payout_filter_input(filter)
        query = []
        if test is not None:
            query.append(("test", test))
        query.append(("requestBody", json.dumps(request_body)))
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/platform/payouts",
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
        return _deserialize_get_platform_payouts_response(response.json())
    async def get_platform_payouts_async(
        self,
        *,
        test: Optional[bool] = None,
        is_for_test: Optional[bool] = None,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformPayoutFilterInput] = None,
    ) -> GetPlatformPayoutsResponse:
        """지급 내역 다건 조회

        여러 지급 내역을 조회합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            is_for_test (bool, optional):
                Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
                Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            page (PageInput, optional):

            filter (PlatformPayoutFilterInput, optional):



        Raises:
            GetPlatformPayoutsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_payout_filter_input(filter)
        query = []
        if test is not None:
            query.append(("test", test))
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/platform/payouts",
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
        return _deserialize_get_platform_payouts_response(response.json())
