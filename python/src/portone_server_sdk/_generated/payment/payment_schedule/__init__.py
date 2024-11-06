from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.payment.payment_schedule.already_paid_or_waiting_error import AlreadyPaidOrWaitingError, _deserialize_already_paid_or_waiting_error, _serialize_already_paid_or_waiting_error
from portone_server_sdk._generated.common.billing_key_already_deleted_error import BillingKeyAlreadyDeletedError, _deserialize_billing_key_already_deleted_error, _serialize_billing_key_already_deleted_error
from portone_server_sdk._generated.common.billing_key_not_found_error import BillingKeyNotFoundError, _deserialize_billing_key_not_found_error, _serialize_billing_key_not_found_error
from portone_server_sdk._generated.common.billing_key_payment_input import BillingKeyPaymentInput, _deserialize_billing_key_payment_input, _serialize_billing_key_payment_input
from portone_server_sdk._generated.payment.payment_schedule.create_payment_schedule_response import CreatePaymentScheduleResponse, _deserialize_create_payment_schedule_response, _serialize_create_payment_schedule_response
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.payment.payment_schedule.get_payment_schedules_response import GetPaymentSchedulesResponse, _deserialize_get_payment_schedules_response, _serialize_get_payment_schedules_response
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from portone_server_sdk._generated.payment.payment_schedule.payment_schedule import PaymentSchedule, _deserialize_payment_schedule, _serialize_payment_schedule
from portone_server_sdk._generated.common.payment_schedule_already_exists_error import PaymentScheduleAlreadyExistsError, _deserialize_payment_schedule_already_exists_error, _serialize_payment_schedule_already_exists_error
from portone_server_sdk._generated.payment.payment_schedule.payment_schedule_already_processed_error import PaymentScheduleAlreadyProcessedError, _deserialize_payment_schedule_already_processed_error, _serialize_payment_schedule_already_processed_error
from portone_server_sdk._generated.payment.payment_schedule.payment_schedule_already_revoked_error import PaymentScheduleAlreadyRevokedError, _deserialize_payment_schedule_already_revoked_error, _serialize_payment_schedule_already_revoked_error
from portone_server_sdk._generated.payment.payment_schedule.payment_schedule_filter_input import PaymentScheduleFilterInput, _deserialize_payment_schedule_filter_input, _serialize_payment_schedule_filter_input
from portone_server_sdk._generated.payment.payment_schedule.payment_schedule_not_found_error import PaymentScheduleNotFoundError, _deserialize_payment_schedule_not_found_error, _serialize_payment_schedule_not_found_error
from portone_server_sdk._generated.payment.payment_schedule.payment_schedule_sort_input import PaymentScheduleSortInput, _deserialize_payment_schedule_sort_input, _serialize_payment_schedule_sort_input
from portone_server_sdk._generated.payment.payment_schedule.revoke_payment_schedules_response import RevokePaymentSchedulesResponse, _deserialize_revoke_payment_schedules_response, _serialize_revoke_payment_schedules_response
from portone_server_sdk._generated.common.sum_of_parts_exceeds_total_amount_error import SumOfPartsExceedsTotalAmountError, _deserialize_sum_of_parts_exceeds_total_amount_error, _serialize_sum_of_parts_exceeds_total_amount_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from urllib.parse import quote
from portone_server_sdk._generated import errors
class PaymentScheduleClient:
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentScheduleNotFoundError: 결제 예약건이 존재하지 않는 경우
                결제 예약건이 존재하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
            if error_type == "PAYMENT_SCHEDULE_NOT_FOUND":
                raise errors.PaymentScheduleNotFoundError(_deserialize_payment_schedule_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentScheduleNotFoundError: 결제 예약건이 존재하지 않는 경우
                결제 예약건이 존재하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
            if error_type == "PAYMENT_SCHEDULE_NOT_FOUND":
                raise errors.PaymentScheduleNotFoundError(_deserialize_payment_schedule_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            BillingKeyAlreadyDeletedError: 빌링키가 이미 삭제된 경우
                빌링키가 이미 삭제된 경우
            BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
                빌링키가 존재하지 않는 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentScheduleAlreadyProcessedError: 결제 예약건이 이미 처리된 경우
                결제 예약건이 이미 처리된 경우
            PaymentScheduleAlreadyRevokedError: 결제 예약건이 이미 취소된 경우
                결제 예약건이 이미 취소된 경우
            PaymentScheduleNotFoundError: 결제 예약건이 존재하지 않는 경우
                결제 예약건이 존재하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_ALREADY_PROCESSED":
                raise errors.PaymentScheduleAlreadyProcessedError(_deserialize_payment_schedule_already_processed_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_ALREADY_REVOKED":
                raise errors.PaymentScheduleAlreadyRevokedError(_deserialize_payment_schedule_already_revoked_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_NOT_FOUND":
                raise errors.PaymentScheduleNotFoundError(_deserialize_payment_schedule_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            BillingKeyAlreadyDeletedError: 빌링키가 이미 삭제된 경우
                빌링키가 이미 삭제된 경우
            BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
                빌링키가 존재하지 않는 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentScheduleAlreadyProcessedError: 결제 예약건이 이미 처리된 경우
                결제 예약건이 이미 처리된 경우
            PaymentScheduleAlreadyRevokedError: 결제 예약건이 이미 취소된 경우
                결제 예약건이 이미 취소된 경우
            PaymentScheduleNotFoundError: 결제 예약건이 존재하지 않는 경우
                결제 예약건이 존재하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_ALREADY_PROCESSED":
                raise errors.PaymentScheduleAlreadyProcessedError(_deserialize_payment_schedule_already_processed_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_ALREADY_REVOKED":
                raise errors.PaymentScheduleAlreadyRevokedError(_deserialize_payment_schedule_already_revoked_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_NOT_FOUND":
                raise errors.PaymentScheduleNotFoundError(_deserialize_payment_schedule_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            AlreadyPaidOrWaitingError: 결제가 이미 완료되었거나 대기중인 경우
                결제가 이미 완료되었거나 대기중인 경우
            BillingKeyAlreadyDeletedError: 빌링키가 이미 삭제된 경우
                빌링키가 이미 삭제된 경우
            BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
                빌링키가 존재하지 않는 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentScheduleAlreadyExistsError: 결제 예약건이 이미 존재하는 경우
                결제 예약건이 이미 존재하는 경우
            SumOfPartsExceedsTotalAmountError: 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
                면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "ALREADY_PAID_OR_WAITING":
                raise errors.AlreadyPaidOrWaitingError(_deserialize_already_paid_or_waiting_error(error_response))
            if error_type == "BILLING_KEY_ALREADY_DELETED":
                raise errors.BillingKeyAlreadyDeletedError(_deserialize_billing_key_already_deleted_error(error_response))
            if error_type == "BILLING_KEY_NOT_FOUND":
                raise errors.BillingKeyNotFoundError(_deserialize_billing_key_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_ALREADY_EXISTS":
                raise errors.PaymentScheduleAlreadyExistsError(_deserialize_payment_schedule_already_exists_error(error_response))
            if error_type == "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT":
                raise errors.SumOfPartsExceedsTotalAmountError(_deserialize_sum_of_parts_exceeds_total_amount_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            AlreadyPaidOrWaitingError: 결제가 이미 완료되었거나 대기중인 경우
                결제가 이미 완료되었거나 대기중인 경우
            BillingKeyAlreadyDeletedError: 빌링키가 이미 삭제된 경우
                빌링키가 이미 삭제된 경우
            BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
                빌링키가 존재하지 않는 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentScheduleAlreadyExistsError: 결제 예약건이 이미 존재하는 경우
                결제 예약건이 이미 존재하는 경우
            SumOfPartsExceedsTotalAmountError: 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
                면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "ALREADY_PAID_OR_WAITING":
                raise errors.AlreadyPaidOrWaitingError(_deserialize_already_paid_or_waiting_error(error_response))
            if error_type == "BILLING_KEY_ALREADY_DELETED":
                raise errors.BillingKeyAlreadyDeletedError(_deserialize_billing_key_already_deleted_error(error_response))
            if error_type == "BILLING_KEY_NOT_FOUND":
                raise errors.BillingKeyNotFoundError(_deserialize_billing_key_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_ALREADY_EXISTS":
                raise errors.PaymentScheduleAlreadyExistsError(_deserialize_payment_schedule_already_exists_error(error_response))
            if error_type == "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT":
                raise errors.SumOfPartsExceedsTotalAmountError(_deserialize_sum_of_parts_exceeds_total_amount_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_create_payment_schedule_response(response.json())
