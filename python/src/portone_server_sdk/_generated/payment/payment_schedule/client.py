from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import AlreadyPaidOrWaitingError, BillingKeyAlreadyDeletedError, BillingKeyNotFoundError, ForbiddenError, InvalidRequestError, PaymentScheduleAlreadyExistsError, PaymentScheduleAlreadyProcessedError, PaymentScheduleAlreadyRevokedError, PaymentScheduleNotFoundError, SumOfPartsExceedsTotalAmountError, UnauthorizedError, UnknownError
from ...payment.payment_schedule.already_paid_or_waiting_error import _deserialize_already_paid_or_waiting_error
from ...common.billing_key_already_deleted_error import _deserialize_billing_key_already_deleted_error
from ...common.billing_key_not_found_error import _deserialize_billing_key_not_found_error
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...common.payment_schedule_already_exists_error import _deserialize_payment_schedule_already_exists_error
from ...payment.payment_schedule.payment_schedule_already_processed_error import _deserialize_payment_schedule_already_processed_error
from ...payment.payment_schedule.payment_schedule_already_revoked_error import _deserialize_payment_schedule_already_revoked_error
from ...payment.payment_schedule.payment_schedule_not_found_error import _deserialize_payment_schedule_not_found_error
from ...common.sum_of_parts_exceeds_total_amount_error import _deserialize_sum_of_parts_exceeds_total_amount_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...common.billing_key_payment_input import BillingKeyPaymentInput, _deserialize_billing_key_payment_input, _serialize_billing_key_payment_input
from ...payment.payment_schedule.create_payment_schedule_response import CreatePaymentScheduleResponse, _deserialize_create_payment_schedule_response, _serialize_create_payment_schedule_response
from ...payment.payment_schedule.get_payment_schedules_response import GetPaymentSchedulesResponse, _deserialize_get_payment_schedules_response, _serialize_get_payment_schedules_response
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...payment.payment_schedule.payment_schedule import PaymentSchedule, _deserialize_payment_schedule, _serialize_payment_schedule
from ...payment.payment_schedule.payment_schedule_filter_input import PaymentScheduleFilterInput, _deserialize_payment_schedule_filter_input, _serialize_payment_schedule_filter_input
from ...payment.payment_schedule.payment_schedule_sort_input import PaymentScheduleSortInput, _deserialize_payment_schedule_sort_input, _serialize_payment_schedule_sort_input
from ...payment.payment_schedule.revoke_payment_schedules_response import RevokePaymentSchedulesResponse, _deserialize_revoke_payment_schedules_response, _serialize_revoke_payment_schedules_response
from urllib.parse import quote
class PaymentScheduleClient:
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
    def get_payment_schedule(
        self,
        *,
        payment_schedule_id: str,
    ) -> PaymentSchedule:
        """결제 예약 단건 조회

        주어진 아이디에 대응되는 결제 예약 건을 조회합니다.

        Args:
            payment_schedule_id (str):
                조회할 결제 예약 건 아이디


        Raises:
            GetPaymentScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = httpx.request(
            "GET",
            f"{self._base_url}/payment-schedules/{quote(payment_schedule_id, safe='')}",
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
                error = _deserialize_payment_schedule_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_payment_schedule(response.json())
    async def get_payment_schedule_async(
        self,
        *,
        payment_schedule_id: str,
    ) -> PaymentSchedule:
        """결제 예약 단건 조회

        주어진 아이디에 대응되는 결제 예약 건을 조회합니다.

        Args:
            payment_schedule_id (str):
                조회할 결제 예약 건 아이디


        Raises:
            GetPaymentScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/payment-schedules/{quote(payment_schedule_id, safe='')}",
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
                error = _deserialize_payment_schedule_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_payment_schedule(response.json())
    def get_payment_schedules(
        self,
        *,
        page: Optional[PageInput] = None,
        sort: Optional[PaymentScheduleSortInput] = None,
        filter: Optional[PaymentScheduleFilterInput] = None,
    ) -> GetPaymentSchedulesResponse:
        """결제 예약 다건 조회

        주어진 조건에 맞는 결제 예약 건들을 조회합니다.
        `filter.from`, `filter.until` 파라미터의 기본값이 결제 시점 기준 지난 90일에 속하는 건을 조회하도록 되어 있으니, 미래 예약 상태의 건을 조회하기 위해서는 해당 파라미터를 직접 설정해 주셔야 합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보

                미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
            sort (PaymentScheduleSortInput, optional):
                정렬 조건

                미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
            filter (PaymentScheduleFilterInput, optional):
                조회할 결제 예약 건의 조건 필터


        Raises:
            GetPaymentSchedulesError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if sort is not None:
            request_body["sort"] = _serialize_payment_schedule_sort_input(sort)
        if filter is not None:
            request_body["filter"] = _serialize_payment_schedule_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/payment-schedules",
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
        return _deserialize_get_payment_schedules_response(response.json())
    async def get_payment_schedules_async(
        self,
        *,
        page: Optional[PageInput] = None,
        sort: Optional[PaymentScheduleSortInput] = None,
        filter: Optional[PaymentScheduleFilterInput] = None,
    ) -> GetPaymentSchedulesResponse:
        """결제 예약 다건 조회

        주어진 조건에 맞는 결제 예약 건들을 조회합니다.
        `filter.from`, `filter.until` 파라미터의 기본값이 결제 시점 기준 지난 90일에 속하는 건을 조회하도록 되어 있으니, 미래 예약 상태의 건을 조회하기 위해서는 해당 파라미터를 직접 설정해 주셔야 합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보

                미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
            sort (PaymentScheduleSortInput, optional):
                정렬 조건

                미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
            filter (PaymentScheduleFilterInput, optional):
                조회할 결제 예약 건의 조건 필터


        Raises:
            GetPaymentSchedulesError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if sort is not None:
            request_body["sort"] = _serialize_payment_schedule_sort_input(sort)
        if filter is not None:
            request_body["filter"] = _serialize_payment_schedule_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/payment-schedules",
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
        return _deserialize_get_payment_schedules_response(response.json())
    def revoke_payment_schedules(
        self,
        *,
        billing_key: Optional[str] = None,
        schedule_ids: Optional[list[str]] = None,
    ) -> RevokePaymentSchedulesResponse:
        """결제 예약 취소

        결제 예약 건을 취소합니다.
        billingKey, scheduleIds 중 하나 이상은 필수로 입력합니다.
        billingKey 만 입력된 경우 -> 해당 빌링키로 예약된 모든 결제 예약 건들이 취소됩니다.
        scheduleIds 만 입력된 경우 -> 입력된 결제 예약 건 아이디에 해당하는 예약 건들이 취소됩니다.
        billingKey, scheduleIds 모두 입력된 경우 -> 입력된 결제 예약 건 아이디에 해당하는 예약 건들이 취소됩니다. 단, 예약한 빌링키가 입력된 빌링키와 일치하지 않으면 실패합니다.
        위 정책에 따라 선택된 결제 예약 건들 중 하나라도 취소에 실패할 경우, 모든 취소 요청이 실패합니다.

        Args:
            billing_key (str, optional):
                빌링키
            schedule_ids (list[str], optional):
                결제 예약 건 아이디 목록


        Raises:
            RevokePaymentSchedulesError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if billing_key is not None:
            request_body["billingKey"] = billing_key
        if schedule_ids is not None:
            request_body["scheduleIds"] = schedule_ids
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/payment-schedules",
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
                error = _deserialize_payment_schedule_already_processed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleAlreadyProcessedError(error)
            try:
                error = _deserialize_payment_schedule_already_revoked_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleAlreadyRevokedError(error)
            try:
                error = _deserialize_payment_schedule_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_revoke_payment_schedules_response(response.json())
    async def revoke_payment_schedules_async(
        self,
        *,
        billing_key: Optional[str] = None,
        schedule_ids: Optional[list[str]] = None,
    ) -> RevokePaymentSchedulesResponse:
        """결제 예약 취소

        결제 예약 건을 취소합니다.
        billingKey, scheduleIds 중 하나 이상은 필수로 입력합니다.
        billingKey 만 입력된 경우 -> 해당 빌링키로 예약된 모든 결제 예약 건들이 취소됩니다.
        scheduleIds 만 입력된 경우 -> 입력된 결제 예약 건 아이디에 해당하는 예약 건들이 취소됩니다.
        billingKey, scheduleIds 모두 입력된 경우 -> 입력된 결제 예약 건 아이디에 해당하는 예약 건들이 취소됩니다. 단, 예약한 빌링키가 입력된 빌링키와 일치하지 않으면 실패합니다.
        위 정책에 따라 선택된 결제 예약 건들 중 하나라도 취소에 실패할 경우, 모든 취소 요청이 실패합니다.

        Args:
            billing_key (str, optional):
                빌링키
            schedule_ids (list[str], optional):
                결제 예약 건 아이디 목록


        Raises:
            RevokePaymentSchedulesError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if billing_key is not None:
            request_body["billingKey"] = billing_key
        if schedule_ids is not None:
            request_body["scheduleIds"] = schedule_ids
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/payment-schedules",
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
                error = _deserialize_payment_schedule_already_processed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleAlreadyProcessedError(error)
            try:
                error = _deserialize_payment_schedule_already_revoked_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleAlreadyRevokedError(error)
            try:
                error = _deserialize_payment_schedule_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_revoke_payment_schedules_response(response.json())
    def create_payment_schedule(
        self,
        *,
        payment_id: str,
        payment: BillingKeyPaymentInput,
        time_to_pay: str,
    ) -> CreatePaymentScheduleResponse:
        """결제 예약

        결제를 예약합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            payment (BillingKeyPaymentInput):
                빌링키 결제 입력 정보
            time_to_pay (str):
                결제 예정 시점


        Raises:
            CreatePaymentScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["payment"] = _serialize_billing_key_payment_input(payment)
        request_body["timeToPay"] = time_to_pay
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/schedule",
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
                error = _deserialize_already_paid_or_waiting_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise AlreadyPaidOrWaitingError(error)
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
                error = _deserialize_sum_of_parts_exceeds_total_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SumOfPartsExceedsTotalAmountError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_create_payment_schedule_response(response.json())
    async def create_payment_schedule_async(
        self,
        *,
        payment_id: str,
        payment: BillingKeyPaymentInput,
        time_to_pay: str,
    ) -> CreatePaymentScheduleResponse:
        """결제 예약

        결제를 예약합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            payment (BillingKeyPaymentInput):
                빌링키 결제 입력 정보
            time_to_pay (str):
                결제 예정 시점


        Raises:
            CreatePaymentScheduleError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["payment"] = _serialize_billing_key_payment_input(payment)
        request_body["timeToPay"] = time_to_pay
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/schedule",
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
                error = _deserialize_already_paid_or_waiting_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise AlreadyPaidOrWaitingError(error)
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
                error = _deserialize_sum_of_parts_exceeds_total_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SumOfPartsExceedsTotalAmountError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_create_payment_schedule_response(response.json())
