from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import BillingKeyAlreadyDeletedError, BillingKeyNotFoundError, BillingKeyNotIssuedError, ChannelNotFoundError, ChannelSpecificError, ForbiddenError, InvalidRequestError, PaymentScheduleAlreadyExistsError, PgProviderError, UnauthorizedError, UnknownError
from ...common.billing_key_already_deleted_error import _deserialize_billing_key_already_deleted_error
from ...common.billing_key_not_found_error import _deserialize_billing_key_not_found_error
from ...payment.billing_key.billing_key_not_issued_error import _deserialize_billing_key_not_issued_error
from ...common.channel_not_found_error import _deserialize_channel_not_found_error
from ...payment.billing_key.channel_specific_error import _deserialize_channel_specific_error
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...common.payment_schedule_already_exists_error import _deserialize_payment_schedule_already_exists_error
from ...common.pg_provider_error import _deserialize_pg_provider_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...payment.billing_key.billing_key_filter_input import BillingKeyFilterInput, _deserialize_billing_key_filter_input, _serialize_billing_key_filter_input
from ...payment.billing_key.billing_key_info import BillingKeyInfo, _deserialize_billing_key_info, _serialize_billing_key_info
from ...payment.billing_key.billing_key_sort_input import BillingKeySortInput, _deserialize_billing_key_sort_input, _serialize_billing_key_sort_input
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
    _client: AsyncClient

    def __init__(self, *, secret: str, base_url: str = "https://api.portone.io", store_id: Optional[str] = None):
        """API Secret을 사용해 포트원 API 클라이언트를 생성합니다."""
        self._secret = secret
        self._base_url = base_url
        self._store_id = store_id
        self._client = AsyncClient()
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
        response = httpx.request(
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
        response = await self._client.request(
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
    ) -> DeleteBillingKeyResponse:
        """빌링키 삭제

        빌링키를 삭제합니다.

        Args:
            billing_key (str):
                삭제할 빌링키
            reason (str, optional):
                사유

                네이버페이: 자동결제 해지 사유입니다. 명시가 필요합니다.


        Raises:
            DeleteBillingKeyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        if reason is not None:
            query.append(("reason", reason))
        response = httpx.request(
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
    ) -> DeleteBillingKeyResponse:
        """빌링키 삭제

        빌링키를 삭제합니다.

        Args:
            billing_key (str):
                삭제할 빌링키
            reason (str, optional):
                사유

                네이버페이: 자동결제 해지 사유입니다. 명시가 필요합니다.


        Raises:
            DeleteBillingKeyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        if reason is not None:
            query.append(("reason", reason))
        response = await self._client.request(
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
        response = httpx.request(
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
        response = await self._client.request(
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
        bypass: dict,
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
        response = httpx.request(
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
        bypass: dict,
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
        response = await self._client.request(
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
