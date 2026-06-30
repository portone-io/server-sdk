from __future__ import annotations
import httpx
import json
from types import TracebackType
from httpx import AsyncClient, Client as SyncClient
from ...._user_agent import USER_AGENT
from typing import Optional, Type
from ...errors import ForbiddenError, InvalidRequestError, PlatformBulkPayoutIdAlreadyExistsError, PlatformDuplicatedPartnerSettlementIdsError, PlatformNegativePayoutAmountPartnersError, PlatformNoSelectedPartnerSettlementsError, PlatformNonPayablePartnerSettlementsError, PlatformNotEnabledError, PlatformPartnerSettlementsNotFoundError, UnauthorizedError, UnknownError
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...platform.payout.platform_bulk_payout_id_already_exists_error import _deserialize_platform_bulk_payout_id_already_exists_error
from ...platform.payout.platform_duplicated_partner_settlement_ids_error import _deserialize_platform_duplicated_partner_settlement_ids_error
from ...platform.payout.platform_negative_payout_amount_partners_error import _deserialize_platform_negative_payout_amount_partners_error
from ...platform.payout.platform_no_selected_partner_settlements_error import _deserialize_platform_no_selected_partner_settlements_error
from ...platform.payout.platform_non_payable_partner_settlements_error import _deserialize_platform_non_payable_partner_settlements_error
from ...platform.platform_not_enabled_error import _deserialize_platform_not_enabled_error
from ...platform.platform_partner_settlements_not_found_error import _deserialize_platform_partner_settlements_not_found_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...platform.payout.complete_platform_payout_by_partner_settlement_ids_response import CompletePlatformPayoutByPartnerSettlementIdsResponse, _deserialize_complete_platform_payout_by_partner_settlement_ids_response, _serialize_complete_platform_payout_by_partner_settlement_ids_response
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

    def close(self) -> None:
        """Close the underlying synchronous HTTP client."""
        self._sync_client.close()

    async def aclose(self) -> None:
        """Close the underlying synchronous and asynchronous HTTP clients."""
        self._sync_client.close()
        await self._async_client.aclose()

    def __enter__(self) -> "PayoutClient":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        self.close()

    async def __aenter__(self) -> "PayoutClient":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        await self.aclose()

    def complete_platform_payout_by_partner_settlement_ids(
        self,
        *,
        test: Optional[bool] = None,
        bulk_payout_id: str,
        name: Optional[str] = None,
        partner_settlement_ids: list[str],
        completed_at: Optional[str] = None,
        is_for_test: Optional[bool] = None,
    ) -> CompletePlatformPayoutByPartnerSettlementIdsResponse:
        """일괄 지급 완료 처리

        선택한 정산내역 아이디들로 일괄 지급을 완료 처리 합니다.

        Warning:
            실험적 API입니다. 하위호환성 정책과 무관하게 변경 및 지원 종료될 수 있으니 이용에 유의하세요.


        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            bulk_payout_id (str):

            name (str, optional):

            partner_settlement_ids (list[str]):

            completed_at (str, optional):
                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
                (yyyy-MM-dd)
            is_for_test (bool, optional):
                Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
                Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            CompletePlatformPayoutByPartnerSettlementIdsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["bulkPayoutId"] = bulk_payout_id
        if name is not None:
            request_body["name"] = name
        request_body["partnerSettlementIds"] = partner_settlement_ids
        if completed_at is not None:
            request_body["completedAt"] = completed_at
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
            "POST",
            f"{self._base_url}/platform/partner-settlements/complete-payout",
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
                error = _deserialize_platform_bulk_payout_id_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformBulkPayoutIdAlreadyExistsError(error)
            try:
                error = _deserialize_platform_negative_payout_amount_partners_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNegativePayoutAmountPartnersError(error)
            try:
                error = _deserialize_platform_duplicated_partner_settlement_ids_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDuplicatedPartnerSettlementIdsError(error)
            try:
                error = _deserialize_platform_non_payable_partner_settlements_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNonPayablePartnerSettlementsError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_no_selected_partner_settlements_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNoSelectedPartnerSettlementsError(error)
            try:
                error = _deserialize_platform_partner_settlements_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerSettlementsNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_complete_platform_payout_by_partner_settlement_ids_response(response.json())
    async def complete_platform_payout_by_partner_settlement_ids_async(
        self,
        *,
        test: Optional[bool] = None,
        bulk_payout_id: str,
        name: Optional[str] = None,
        partner_settlement_ids: list[str],
        completed_at: Optional[str] = None,
        is_for_test: Optional[bool] = None,
    ) -> CompletePlatformPayoutByPartnerSettlementIdsResponse:
        """일괄 지급 완료 처리

        선택한 정산내역 아이디들로 일괄 지급을 완료 처리 합니다.

        Warning:
            실험적 API입니다. 하위호환성 정책과 무관하게 변경 및 지원 종료될 수 있으니 이용에 유의하세요.


        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            bulk_payout_id (str):

            name (str, optional):

            partner_settlement_ids (list[str]):

            completed_at (str, optional):
                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
                (yyyy-MM-dd)
            is_for_test (bool, optional):
                Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
                Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            CompletePlatformPayoutByPartnerSettlementIdsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["bulkPayoutId"] = bulk_payout_id
        if name is not None:
            request_body["name"] = name
        request_body["partnerSettlementIds"] = partner_settlement_ids
        if completed_at is not None:
            request_body["completedAt"] = completed_at
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
            "POST",
            f"{self._base_url}/platform/partner-settlements/complete-payout",
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
                error = _deserialize_platform_bulk_payout_id_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformBulkPayoutIdAlreadyExistsError(error)
            try:
                error = _deserialize_platform_negative_payout_amount_partners_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNegativePayoutAmountPartnersError(error)
            try:
                error = _deserialize_platform_duplicated_partner_settlement_ids_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDuplicatedPartnerSettlementIdsError(error)
            try:
                error = _deserialize_platform_non_payable_partner_settlements_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNonPayablePartnerSettlementsError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_no_selected_partner_settlements_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNoSelectedPartnerSettlementsError(error)
            try:
                error = _deserialize_platform_partner_settlements_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerSettlementsNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_complete_platform_payout_by_partner_settlement_ids_response(response.json())
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
