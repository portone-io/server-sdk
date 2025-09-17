from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import BillingKeyAlreadyDeletedError, BillingKeyAlreadyIssuedError, BillingKeyNotFoundError, BillingKeyNotIssuedError, ChannelNotFoundError, ChannelSpecificError, ForbiddenError, InformationMismatchError, InvalidRequestError, PaymentScheduleAlreadyExistsError, PgProviderError, UnauthorizedError, UnknownError
from ...common.billing_key_already_deleted_error import _deserialize_billing_key_already_deleted_error
from ...payment.billing_key.billing_key_already_issued_error import _deserialize_billing_key_already_issued_error
from ...common.billing_key_not_found_error import _deserialize_billing_key_not_found_error
from ...payment.billing_key.billing_key_not_issued_error import _deserialize_billing_key_not_issued_error
from ...common.channel_not_found_error import _deserialize_channel_not_found_error
from ...payment.billing_key.channel_specific_error import _deserialize_channel_specific_error
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.information_mismatch_error import _deserialize_information_mismatch_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...common.payment_schedule_already_exists_error import _deserialize_payment_schedule_already_exists_error
from ...common.pg_provider_error import _deserialize_pg_provider_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...payment.billing_key.billing_key_delete_requester import BillingKeyDeleteRequester, _deserialize_billing_key_delete_requester, _serialize_billing_key_delete_requester
from ...payment.billing_key.billing_key_filter_input import BillingKeyFilterInput, _deserialize_billing_key_filter_input, _serialize_billing_key_filter_input
from ...payment.billing_key.billing_key_info import BillingKeyInfo, _deserialize_billing_key_info, _serialize_billing_key_info
from ...payment.billing_key.billing_key_sort_input import BillingKeySortInput, _deserialize_billing_key_sort_input, _serialize_billing_key_sort_input
from ...payment.billing_key.confirmed_billing_key_issue_and_pay_summary import ConfirmedBillingKeyIssueAndPaySummary, _deserialize_confirmed_billing_key_issue_and_pay_summary, _serialize_confirmed_billing_key_issue_and_pay_summary
from ...payment.billing_key.confirmed_billing_key_summary import ConfirmedBillingKeySummary, _deserialize_confirmed_billing_key_summary, _serialize_confirmed_billing_key_summary
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...common.customer_input import CustomerInput, _deserialize_customer_input, _serialize_customer_input
from ...payment.billing_key.delete_billing_key_response import DeleteBillingKeyResponse, _deserialize_delete_billing_key_response, _serialize_delete_billing_key_response
from ...payment.billing_key.get_billing_key_infos_response import GetBillingKeyInfosResponse, _deserialize_get_billing_key_infos_response, _serialize_get_billing_key_infos_response
from ...payment.billing_key.instant_billing_key_payment_method_input import InstantBillingKeyPaymentMethodInput, _deserialize_instant_billing_key_payment_method_input, _serialize_instant_billing_key_payment_method_input
from ...payment.billing_key.issue_billing_key_response import IssueBillingKeyResponse, _deserialize_issue_billing_key_response, _serialize_issue_billing_key_response
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from urllib.parse import quote
class BillingKeyClient:
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
    def get_billing_key_infos(
        self,
        *,
        page: Optional[PageInput] = None,
        sort: Optional[BillingKeySortInput] = None,
        filter: Optional[BillingKeyFilterInput] = None,
    ) -> GetBillingKeyInfosResponse:
        """빌링키 다건 조회

        주어진 조건에 맞는 빌링키들을 페이지 기반으로 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보

                미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
            sort (BillingKeySortInput, optional):
                정렬 조건

                미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
            filter (BillingKeyFilterInput, optional):
                조회할 빌링키 조건 필터

                V1 빌링키 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.


        Raises:
            GetBillingKeyInfosError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if sort is not None:
            request_body["sort"] = _serialize_billing_key_sort_input(sort)
        if filter is not None:
            request_body["filter"] = _serialize_billing_key_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/billing-keys",
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
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_get_billing_key_infos_response(response.json())
    async def get_billing_key_infos_async(
        self,
        *,
        page: Optional[PageInput] = None,
        sort: Optional[BillingKeySortInput] = None,
        filter: Optional[BillingKeyFilterInput] = None,
    ) -> GetBillingKeyInfosResponse:
        """빌링키 다건 조회

        주어진 조건에 맞는 빌링키들을 페이지 기반으로 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보

                미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
            sort (BillingKeySortInput, optional):
                정렬 조건

                미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
            filter (BillingKeyFilterInput, optional):
                조회할 빌링키 조건 필터

                V1 빌링키 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.


        Raises:
            GetBillingKeyInfosError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if sort is not None:
            request_body["sort"] = _serialize_billing_key_sort_input(sort)
        if filter is not None:
            request_body["filter"] = _serialize_billing_key_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/billing-keys",
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
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_get_billing_key_infos_response(response.json())
    def issue_billing_key(
        self,
        *,
        method: InstantBillingKeyPaymentMethodInput,
        channel_key: Optional[str] = None,
        channel_group_id: Optional[str] = None,
        customer: Optional[CustomerInput] = None,
        custom_data: Optional[str] = None,
        bypass: Optional[dict] = None,
        notice_urls: Optional[list[str]] = None,
    ) -> IssueBillingKeyResponse:
        """빌링키 발급

        빌링키 발급을 요청합니다.

        Args:
            method (InstantBillingKeyPaymentMethodInput):
                빌링키 결제 수단 정보
            channel_key (str, optional):
                채널 키

                채널 키 또는 채널 그룹 ID 필수
            channel_group_id (str, optional):
                채널 그룹 ID

                채널 키 또는 채널 그룹 ID 필수
            customer (CustomerInput, optional):
                고객 정보
            custom_data (str, optional):
                사용자 지정 데이터
            bypass (dict, optional):
                PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)
            notice_urls (list[str], optional):
                웹훅 주소

                빌링키 발급 시 요청을 받을 웹훅 주소입니다.
                상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.


        Raises:
            IssueBillingKeyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        request_body["method"] = _serialize_instant_billing_key_payment_method_input(method)
        if channel_key is not None:
            request_body["channelKey"] = channel_key
        if channel_group_id is not None:
            request_body["channelGroupId"] = channel_group_id
        if customer is not None:
            request_body["customer"] = _serialize_customer_input(customer)
        if custom_data is not None:
            request_body["customData"] = custom_data
        if bypass is not None:
            request_body["bypass"] = bypass
        if notice_urls is not None:
            request_body["noticeUrls"] = notice_urls
        query = []
        response = self._sync_client.request(
            "POST",
            f"{self._base_url}/billing-keys",
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
                error = _deserialize_channel_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelNotFoundError(error)
            try:
                error = _deserialize_channel_specific_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelSpecificError(error)
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
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_issue_billing_key_response(response.json())
    async def issue_billing_key_async(
        self,
        *,
        method: InstantBillingKeyPaymentMethodInput,
        channel_key: Optional[str] = None,
        channel_group_id: Optional[str] = None,
        customer: Optional[CustomerInput] = None,
        custom_data: Optional[str] = None,
        bypass: Optional[dict] = None,
        notice_urls: Optional[list[str]] = None,
    ) -> IssueBillingKeyResponse:
        """빌링키 발급

        빌링키 발급을 요청합니다.

        Args:
            method (InstantBillingKeyPaymentMethodInput):
                빌링키 결제 수단 정보
            channel_key (str, optional):
                채널 키

                채널 키 또는 채널 그룹 ID 필수
            channel_group_id (str, optional):
                채널 그룹 ID

                채널 키 또는 채널 그룹 ID 필수
            customer (CustomerInput, optional):
                고객 정보
            custom_data (str, optional):
                사용자 지정 데이터
            bypass (dict, optional):
                PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)
            notice_urls (list[str], optional):
                웹훅 주소

                빌링키 발급 시 요청을 받을 웹훅 주소입니다.
                상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.


        Raises:
            IssueBillingKeyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        request_body["method"] = _serialize_instant_billing_key_payment_method_input(method)
        if channel_key is not None:
            request_body["channelKey"] = channel_key
        if channel_group_id is not None:
            request_body["channelGroupId"] = channel_group_id
        if customer is not None:
            request_body["customer"] = _serialize_customer_input(customer)
        if custom_data is not None:
            request_body["customData"] = custom_data
        if bypass is not None:
            request_body["bypass"] = bypass
        if notice_urls is not None:
            request_body["noticeUrls"] = notice_urls
        query = []
        response = await self._async_client.request(
            "POST",
            f"{self._base_url}/billing-keys",
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
                error = _deserialize_channel_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelNotFoundError(error)
            try:
                error = _deserialize_channel_specific_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelSpecificError(error)
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
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_issue_billing_key_response(response.json())
    def confirm_billing_key(
        self,
        *,
        billing_issue_token: str,
        is_test: Optional[bool] = None,
    ) -> ConfirmedBillingKeySummary:
        """빌링키 발급 수동 승인

        수동 승인으로 설정된 빌링키 발급에 대해, 빌링키 발급을 완료 처리합니다.

        Args:
            billing_issue_token (str):
                빌링키 발급 토큰

                빌링키 발급 요청 완료 시 발급된 토큰입니다.
            is_test (bool, optional):
                테스트 결제 여부

                검증용 파라미터로, 결제 건 테스트 여부와 일치하지 않을 경우 오류가 반환됩니다.


        Raises:
            ConfirmBillingKeyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        request_body["billingIssueToken"] = billing_issue_token
        if is_test is not None:
            request_body["isTest"] = is_test
        query = []
        response = self._sync_client.request(
            "POST",
            f"{self._base_url}/billing-keys/confirm",
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
                error = _deserialize_billing_key_already_issued_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyAlreadyIssuedError(error)
            try:
                error = _deserialize_billing_key_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyNotFoundError(error)
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_information_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InformationMismatchError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_confirmed_billing_key_summary(response.json())
    async def confirm_billing_key_async(
        self,
        *,
        billing_issue_token: str,
        is_test: Optional[bool] = None,
    ) -> ConfirmedBillingKeySummary:
        """빌링키 발급 수동 승인

        수동 승인으로 설정된 빌링키 발급에 대해, 빌링키 발급을 완료 처리합니다.

        Args:
            billing_issue_token (str):
                빌링키 발급 토큰

                빌링키 발급 요청 완료 시 발급된 토큰입니다.
            is_test (bool, optional):
                테스트 결제 여부

                검증용 파라미터로, 결제 건 테스트 여부와 일치하지 않을 경우 오류가 반환됩니다.


        Raises:
            ConfirmBillingKeyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        request_body["billingIssueToken"] = billing_issue_token
        if is_test is not None:
            request_body["isTest"] = is_test
        query = []
        response = await self._async_client.request(
            "POST",
            f"{self._base_url}/billing-keys/confirm",
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
                error = _deserialize_billing_key_already_issued_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyAlreadyIssuedError(error)
            try:
                error = _deserialize_billing_key_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyNotFoundError(error)
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_information_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InformationMismatchError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_confirmed_billing_key_summary(response.json())
    def confirm_billing_key_issue_and_pay(
        self,
        *,
        billing_issue_token: str,
        payment_id: Optional[str] = None,
        currency: Optional[Currency] = None,
        total_amount: Optional[int] = None,
        tax_free_amount: Optional[int] = None,
        is_test: Optional[bool] = None,
    ) -> ConfirmedBillingKeyIssueAndPaySummary:
        """빌링키 발급 및 초회 결제 수동 승인

        수동 승인으로 설정된 빌링키 발급 및 초회 결제에 대해, 빌링키 발급과 결제를 완료 처리합니다.

        Args:
            billing_issue_token (str):
                빌링키 발급 토큰

                빌링키 발급 및 초회 결제 요청 완료 시 발급된 토큰입니다.
            payment_id (str, optional):
                결제 건 아이디

                검증용 파라미터로, 결제 건 아이디와 일치하지 않을 경우 오류가 반환됩니다.
            currency (Currency, optional):
                통화

                검증용 파라미터로, 결제 건 화폐와 일치하지 않을 경우 오류가 반환됩니다.
            total_amount (int, optional):
                결제 금액

                검증용 파라미터로, 결제 건 총 금액과 일치하지 않을 경우 오류가 반환됩니다.
                (int64)
            tax_free_amount (int, optional):
                면세 금액

                검증용 파라미터로, 결제 건 면세 금액과 일치하지 않을 경우 오류가 반환됩니다.
                (int64)
            is_test (bool, optional):
                테스트 결제 여부

                검증용 파라미터로, 결제 건 테스트 여부와 일치하지 않을 경우 오류가 반환됩니다.


        Raises:
            ConfirmBillingKeyIssueAndPayError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        request_body["billingIssueToken"] = billing_issue_token
        if payment_id is not None:
            request_body["paymentId"] = payment_id
        if currency is not None:
            request_body["currency"] = _serialize_currency(currency)
        if total_amount is not None:
            request_body["totalAmount"] = total_amount
        if tax_free_amount is not None:
            request_body["taxFreeAmount"] = tax_free_amount
        if is_test is not None:
            request_body["isTest"] = is_test
        query = []
        response = self._sync_client.request(
            "POST",
            f"{self._base_url}/billing-keys/confirm-issue-and-pay",
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
                error = _deserialize_billing_key_already_issued_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyAlreadyIssuedError(error)
            try:
                error = _deserialize_billing_key_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyNotFoundError(error)
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_information_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InformationMismatchError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_confirmed_billing_key_issue_and_pay_summary(response.json())
    async def confirm_billing_key_issue_and_pay_async(
        self,
        *,
        billing_issue_token: str,
        payment_id: Optional[str] = None,
        currency: Optional[Currency] = None,
        total_amount: Optional[int] = None,
        tax_free_amount: Optional[int] = None,
        is_test: Optional[bool] = None,
    ) -> ConfirmedBillingKeyIssueAndPaySummary:
        """빌링키 발급 및 초회 결제 수동 승인

        수동 승인으로 설정된 빌링키 발급 및 초회 결제에 대해, 빌링키 발급과 결제를 완료 처리합니다.

        Args:
            billing_issue_token (str):
                빌링키 발급 토큰

                빌링키 발급 및 초회 결제 요청 완료 시 발급된 토큰입니다.
            payment_id (str, optional):
                결제 건 아이디

                검증용 파라미터로, 결제 건 아이디와 일치하지 않을 경우 오류가 반환됩니다.
            currency (Currency, optional):
                통화

                검증용 파라미터로, 결제 건 화폐와 일치하지 않을 경우 오류가 반환됩니다.
            total_amount (int, optional):
                결제 금액

                검증용 파라미터로, 결제 건 총 금액과 일치하지 않을 경우 오류가 반환됩니다.
                (int64)
            tax_free_amount (int, optional):
                면세 금액

                검증용 파라미터로, 결제 건 면세 금액과 일치하지 않을 경우 오류가 반환됩니다.
                (int64)
            is_test (bool, optional):
                테스트 결제 여부

                검증용 파라미터로, 결제 건 테스트 여부와 일치하지 않을 경우 오류가 반환됩니다.


        Raises:
            ConfirmBillingKeyIssueAndPayError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        request_body["billingIssueToken"] = billing_issue_token
        if payment_id is not None:
            request_body["paymentId"] = payment_id
        if currency is not None:
            request_body["currency"] = _serialize_currency(currency)
        if total_amount is not None:
            request_body["totalAmount"] = total_amount
        if tax_free_amount is not None:
            request_body["taxFreeAmount"] = tax_free_amount
        if is_test is not None:
            request_body["isTest"] = is_test
        query = []
        response = await self._async_client.request(
            "POST",
            f"{self._base_url}/billing-keys/confirm-issue-and-pay",
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
                error = _deserialize_billing_key_already_issued_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyAlreadyIssuedError(error)
            try:
                error = _deserialize_billing_key_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyNotFoundError(error)
            try:
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_information_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InformationMismatchError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_confirmed_billing_key_issue_and_pay_summary(response.json())
    def get_billing_key_info(
        self,
        *,
        billing_key: str,
    ) -> BillingKeyInfo:
        """빌링키 단건 조회

        주어진 빌링키에 대응되는 빌링키 정보를 조회합니다.

        Args:
            billing_key (str):
                조회할 빌링키


        Raises:
            GetBillingKeyInfoError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/billing-keys/{quote(billing_key, safe='')}",
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
                error = _deserialize_billing_key_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyNotFoundError(error)
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
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_billing_key_info(response.json())
    async def get_billing_key_info_async(
        self,
        *,
        billing_key: str,
    ) -> BillingKeyInfo:
        """빌링키 단건 조회

        주어진 빌링키에 대응되는 빌링키 정보를 조회합니다.

        Args:
            billing_key (str):
                조회할 빌링키


        Raises:
            GetBillingKeyInfoError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/billing-keys/{quote(billing_key, safe='')}",
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
                error = _deserialize_billing_key_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyNotFoundError(error)
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
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_billing_key_info(response.json())
    def delete_billing_key(
        self,
        *,
        billing_key: str,
        reason: Optional[str] = None,
        requester: Optional[BillingKeyDeleteRequester] = None,
    ) -> DeleteBillingKeyResponse:
        """빌링키 삭제

        빌링키를 삭제합니다.

        Args:
            billing_key (str):
                삭제할 빌링키
            reason (str, optional):
                사유

                네이버페이: 자동결제 해지 사유입니다. 명시가 필요합니다.
            requester (BillingKeyDeleteRequester, optional):
                요청 주체

                네이버페이: 자동결제 해지 요청 주체입니다. 명시가 필요합니다.


        Raises:
            DeleteBillingKeyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        if reason is not None:
            query.append(("reason", reason))
        if requester is not None:
            query.append(("requester", requester))
        response = self._sync_client.request(
            "DELETE",
            f"{self._base_url}/billing-keys/{quote(billing_key, safe='')}",
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
                error = _deserialize_billing_key_already_deleted_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyAlreadyDeletedError(error)
            try:
                error = _deserialize_billing_key_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyNotFoundError(error)
            try:
                error = _deserialize_billing_key_not_issued_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyNotIssuedError(error)
            try:
                error = _deserialize_channel_specific_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelSpecificError(error)
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
                error = _deserialize_payment_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_delete_billing_key_response(response.json())
    async def delete_billing_key_async(
        self,
        *,
        billing_key: str,
        reason: Optional[str] = None,
        requester: Optional[BillingKeyDeleteRequester] = None,
    ) -> DeleteBillingKeyResponse:
        """빌링키 삭제

        빌링키를 삭제합니다.

        Args:
            billing_key (str):
                삭제할 빌링키
            reason (str, optional):
                사유

                네이버페이: 자동결제 해지 사유입니다. 명시가 필요합니다.
            requester (BillingKeyDeleteRequester, optional):
                요청 주체

                네이버페이: 자동결제 해지 요청 주체입니다. 명시가 필요합니다.


        Raises:
            DeleteBillingKeyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        if reason is not None:
            query.append(("reason", reason))
        if requester is not None:
            query.append(("requester", requester))
        response = await self._async_client.request(
            "DELETE",
            f"{self._base_url}/billing-keys/{quote(billing_key, safe='')}",
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
                error = _deserialize_billing_key_already_deleted_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyAlreadyDeletedError(error)
            try:
                error = _deserialize_billing_key_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyNotFoundError(error)
            try:
                error = _deserialize_billing_key_not_issued_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyNotIssuedError(error)
            try:
                error = _deserialize_channel_specific_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelSpecificError(error)
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
                error = _deserialize_payment_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_delete_billing_key_response(response.json())
