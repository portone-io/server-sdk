from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.common.billing_key_already_deleted_error import BillingKeyAlreadyDeletedError, _deserialize_billing_key_already_deleted_error, _serialize_billing_key_already_deleted_error
from portone_server_sdk._generated.payment.billing_key.billing_key_filter_input import BillingKeyFilterInput, _deserialize_billing_key_filter_input, _serialize_billing_key_filter_input
from portone_server_sdk._generated.payment.billing_key.billing_key_info import BillingKeyInfo, _deserialize_billing_key_info, _serialize_billing_key_info
from portone_server_sdk._generated.common.billing_key_not_found_error import BillingKeyNotFoundError, _deserialize_billing_key_not_found_error, _serialize_billing_key_not_found_error
from portone_server_sdk._generated.payment.billing_key.billing_key_not_issued_error import BillingKeyNotIssuedError, _deserialize_billing_key_not_issued_error, _serialize_billing_key_not_issued_error
from portone_server_sdk._generated.payment.billing_key.billing_key_sort_input import BillingKeySortInput, _deserialize_billing_key_sort_input, _serialize_billing_key_sort_input
from portone_server_sdk._generated.common.channel_not_found_error import ChannelNotFoundError, _deserialize_channel_not_found_error, _serialize_channel_not_found_error
from portone_server_sdk._generated.payment.billing_key.channel_specific_error import ChannelSpecificError, _deserialize_channel_specific_error, _serialize_channel_specific_error
from portone_server_sdk._generated.common.customer_input import CustomerInput, _deserialize_customer_input, _serialize_customer_input
from portone_server_sdk._generated.payment.billing_key.delete_billing_key_response import DeleteBillingKeyResponse, _deserialize_delete_billing_key_response, _serialize_delete_billing_key_response
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.payment.billing_key.get_billing_key_infos_response import GetBillingKeyInfosResponse, _deserialize_get_billing_key_infos_response, _serialize_get_billing_key_infos_response
from portone_server_sdk._generated.payment.billing_key.instant_billing_key_payment_method_input import InstantBillingKeyPaymentMethodInput, _deserialize_instant_billing_key_payment_method_input, _serialize_instant_billing_key_payment_method_input
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.payment.billing_key.issue_billing_key_response import IssueBillingKeyResponse, _deserialize_issue_billing_key_response, _serialize_issue_billing_key_response
from portone_server_sdk._generated.common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from portone_server_sdk._generated.common.payment_schedule_already_exists_error import PaymentScheduleAlreadyExistsError, _deserialize_payment_schedule_already_exists_error, _serialize_payment_schedule_already_exists_error
from portone_server_sdk._generated.common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from urllib.parse import quote
from portone_server_sdk._generated import errors
class BillingKeyClient:
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
            BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
                빌링키가 존재하지 않는 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "BILLING_KEY_NOT_FOUND":
                raise errors.BillingKeyNotFoundError(_deserialize_billing_key_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
                빌링키가 존재하지 않는 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "BILLING_KEY_NOT_FOUND":
                raise errors.BillingKeyNotFoundError(_deserialize_billing_key_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_billing_key_info(response.json())
    def delete_billing_key(
        self,
        *,
        billing_key: str,
    ) -> DeleteBillingKeyResponse:
        """빌링키 삭제

        빌링키를 삭제합니다.

        Args:
            billing_key (str):
                삭제할 빌링키


        Raises:
            BillingKeyAlreadyDeletedError: 빌링키가 이미 삭제된 경우
                빌링키가 이미 삭제된 경우
            BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
                빌링키가 존재하지 않는 경우
            BillingKeyNotIssuedError: BillingKeyNotIssuedError
            ChannelSpecificError: 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
                여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentScheduleAlreadyExistsError: 결제 예약건이 이미 존재하는 경우
                결제 예약건이 이미 존재하는 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/billing-keys/{quote(billing_key, safe='')}",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "BILLING_KEY_ALREADY_DELETED":
                raise errors.BillingKeyAlreadyDeletedError(_deserialize_billing_key_already_deleted_error(error_response))
            if error_type == "BILLING_KEY_NOT_FOUND":
                raise errors.BillingKeyNotFoundError(_deserialize_billing_key_not_found_error(error_response))
            if error_type == "BILLING_KEY_NOT_ISSUED":
                raise errors.BillingKeyNotIssuedError(_deserialize_billing_key_not_issued_error(error_response))
            if error_type == "CHANNEL_SPECIFIC":
                raise errors.ChannelSpecificError(_deserialize_channel_specific_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_ALREADY_EXISTS":
                raise errors.PaymentScheduleAlreadyExistsError(_deserialize_payment_schedule_already_exists_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_delete_billing_key_response(response.json())
    async def delete_billing_key_async(
        self,
        *,
        billing_key: str,
    ) -> DeleteBillingKeyResponse:
        """빌링키 삭제

        빌링키를 삭제합니다.

        Args:
            billing_key (str):
                삭제할 빌링키


        Raises:
            BillingKeyAlreadyDeletedError: 빌링키가 이미 삭제된 경우
                빌링키가 이미 삭제된 경우
            BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
                빌링키가 존재하지 않는 경우
            BillingKeyNotIssuedError: BillingKeyNotIssuedError
            ChannelSpecificError: 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
                여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentScheduleAlreadyExistsError: 결제 예약건이 이미 존재하는 경우
                결제 예약건이 이미 존재하는 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/billing-keys/{quote(billing_key, safe='')}",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "BILLING_KEY_ALREADY_DELETED":
                raise errors.BillingKeyAlreadyDeletedError(_deserialize_billing_key_already_deleted_error(error_response))
            if error_type == "BILLING_KEY_NOT_FOUND":
                raise errors.BillingKeyNotFoundError(_deserialize_billing_key_not_found_error(error_response))
            if error_type == "BILLING_KEY_NOT_ISSUED":
                raise errors.BillingKeyNotIssuedError(_deserialize_billing_key_not_issued_error(error_response))
            if error_type == "CHANNEL_SPECIFIC":
                raise errors.ChannelSpecificError(_deserialize_channel_specific_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_ALREADY_EXISTS":
                raise errors.PaymentScheduleAlreadyExistsError(_deserialize_payment_schedule_already_exists_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
                요청된 채널이 존재하지 않는 경우
            ChannelSpecificError: 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
                여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "CHANNEL_NOT_FOUND":
                raise errors.ChannelNotFoundError(_deserialize_channel_not_found_error(error_response))
            if error_type == "CHANNEL_SPECIFIC":
                raise errors.ChannelSpecificError(_deserialize_channel_specific_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
                요청된 채널이 존재하지 않는 경우
            ChannelSpecificError: 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
                여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "CHANNEL_NOT_FOUND":
                raise errors.ChannelNotFoundError(_deserialize_channel_not_found_error(error_response))
            if error_type == "CHANNEL_SPECIFIC":
                raise errors.ChannelSpecificError(_deserialize_channel_specific_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_issue_billing_key_response(response.json())
