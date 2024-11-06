from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.common.channel_not_found_error import ChannelNotFoundError, _deserialize_channel_not_found_error, _serialize_channel_not_found_error
from portone_server_sdk._generated.identity_verification.confirm_identity_verification_response import ConfirmIdentityVerificationResponse, _deserialize_confirm_identity_verification_response, _serialize_confirm_identity_verification_response
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.identity_verification.identity_verification import IdentityVerification, _deserialize_identity_verification, _serialize_identity_verification
from portone_server_sdk._generated.identity_verification.identity_verification_already_sent_error import IdentityVerificationAlreadySentError, _deserialize_identity_verification_already_sent_error, _serialize_identity_verification_already_sent_error
from portone_server_sdk._generated.identity_verification.identity_verification_already_verified_error import IdentityVerificationAlreadyVerifiedError, _deserialize_identity_verification_already_verified_error, _serialize_identity_verification_already_verified_error
from portone_server_sdk._generated.identity_verification.identity_verification_method import IdentityVerificationMethod, _deserialize_identity_verification_method, _serialize_identity_verification_method
from portone_server_sdk._generated.identity_verification.identity_verification_not_found_error import IdentityVerificationNotFoundError, _deserialize_identity_verification_not_found_error, _serialize_identity_verification_not_found_error
from portone_server_sdk._generated.identity_verification.identity_verification_not_sent_error import IdentityVerificationNotSentError, _deserialize_identity_verification_not_sent_error, _serialize_identity_verification_not_sent_error
from portone_server_sdk._generated.identity_verification.identity_verification_operator import IdentityVerificationOperator, _deserialize_identity_verification_operator, _serialize_identity_verification_operator
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.max_transaction_count_reached_error import MaxTransactionCountReachedError, _deserialize_max_transaction_count_reached_error, _serialize_max_transaction_count_reached_error
from portone_server_sdk._generated.common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from portone_server_sdk._generated.identity_verification.resend_identity_verification_response import ResendIdentityVerificationResponse, _deserialize_resend_identity_verification_response, _serialize_resend_identity_verification_response
from portone_server_sdk._generated.identity_verification.send_identity_verification_body_customer import SendIdentityVerificationBodyCustomer, _deserialize_send_identity_verification_body_customer, _serialize_send_identity_verification_body_customer
from portone_server_sdk._generated.identity_verification.send_identity_verification_response import SendIdentityVerificationResponse, _deserialize_send_identity_verification_response, _serialize_send_identity_verification_response
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from urllib.parse import quote
from portone_server_sdk._generated import errors
class IdentityVerificationClient:
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
    def get_identity_verification(
        self,
        *,
        identity_verification_id: str,
    ) -> IdentityVerification:
        """본인인증 단건 조회

        주어진 아이디에 대응되는 본인인증 내역을 조회합니다.

        Args:
            identity_verification_id (str):
                조회할 본인인증 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            IdentityVerificationNotFoundError: 요청된 본인인증 건이 존재하지 않는 경우
                요청된 본인인증 건이 존재하지 않는 경우
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
            f"{self._base_url}/identity-verifications/{quote(identity_verification_id, safe='')}",
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
            if error_type == "IDENTITY_VERIFICATION_NOT_FOUND":
                raise errors.IdentityVerificationNotFoundError(_deserialize_identity_verification_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_identity_verification(response.json())
    async def get_identity_verification_async(
        self,
        *,
        identity_verification_id: str,
    ) -> IdentityVerification:
        """본인인증 단건 조회

        주어진 아이디에 대응되는 본인인증 내역을 조회합니다.

        Args:
            identity_verification_id (str):
                조회할 본인인증 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            IdentityVerificationNotFoundError: 요청된 본인인증 건이 존재하지 않는 경우
                요청된 본인인증 건이 존재하지 않는 경우
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
            f"{self._base_url}/identity-verifications/{quote(identity_verification_id, safe='')}",
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
            if error_type == "IDENTITY_VERIFICATION_NOT_FOUND":
                raise errors.IdentityVerificationNotFoundError(_deserialize_identity_verification_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_identity_verification(response.json())
    def send_identity_verification(
        self,
        *,
        identity_verification_id: str,
        channel_key: str,
        customer: SendIdentityVerificationBodyCustomer,
        custom_data: Optional[str] = None,
        bypass: dict,
        operator: IdentityVerificationOperator,
        method: IdentityVerificationMethod,
    ) -> SendIdentityVerificationResponse:
        """본인인증 요청 전송

        SMS 또는 APP 방식을 이용하여 본인인증 요청을 전송합니다.

        Args:
            identity_verification_id (str):
                본인인증 아이디
            channel_key (str):
                채널 키
            customer (SendIdentityVerificationBodyCustomer):
                고객 정보
            custom_data (str, optional):
                사용자 지정 데이터
            bypass (dict, optional):
                PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)
            operator (IdentityVerificationOperator):
                통신사
            method (IdentityVerificationMethod):
                본인인증 방식


        Raises:
            ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
                요청된 채널이 존재하지 않는 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            IdentityVerificationAlreadySentError: 본인인증 건이 이미 API로 요청된 상태인 경우
                본인인증 건이 이미 API로 요청된 상태인 경우
            IdentityVerificationAlreadyVerifiedError: 본인인증 건이 이미 인증 완료된 상태인 경우
                본인인증 건이 이미 인증 완료된 상태인 경우
            IdentityVerificationNotFoundError: 요청된 본인인증 건이 존재하지 않는 경우
                요청된 본인인증 건이 존재하지 않는 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            MaxTransactionCountReachedError: 결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
                결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        request_body["channelKey"] = channel_key
        request_body["customer"] = _serialize_send_identity_verification_body_customer(customer)
        if custom_data is not None:
            request_body["customData"] = custom_data
        if bypass is not None:
            request_body["bypass"] = bypass
        request_body["operator"] = _serialize_identity_verification_operator(operator)
        request_body["method"] = _serialize_identity_verification_method(method)
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/identity-verifications/{quote(identity_verification_id, safe='')}/send",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_ALREADY_SENT":
                raise errors.IdentityVerificationAlreadySentError(_deserialize_identity_verification_already_sent_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
                raise errors.IdentityVerificationAlreadyVerifiedError(_deserialize_identity_verification_already_verified_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_NOT_FOUND":
                raise errors.IdentityVerificationNotFoundError(_deserialize_identity_verification_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "MAX_TRANSACTION_COUNT_REACHED":
                raise errors.MaxTransactionCountReachedError(_deserialize_max_transaction_count_reached_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_send_identity_verification_response(response.json())
    async def send_identity_verification_async(
        self,
        *,
        identity_verification_id: str,
        channel_key: str,
        customer: SendIdentityVerificationBodyCustomer,
        custom_data: Optional[str] = None,
        bypass: dict,
        operator: IdentityVerificationOperator,
        method: IdentityVerificationMethod,
    ) -> SendIdentityVerificationResponse:
        """본인인증 요청 전송

        SMS 또는 APP 방식을 이용하여 본인인증 요청을 전송합니다.

        Args:
            identity_verification_id (str):
                본인인증 아이디
            channel_key (str):
                채널 키
            customer (SendIdentityVerificationBodyCustomer):
                고객 정보
            custom_data (str, optional):
                사용자 지정 데이터
            bypass (dict, optional):
                PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)
            operator (IdentityVerificationOperator):
                통신사
            method (IdentityVerificationMethod):
                본인인증 방식


        Raises:
            ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
                요청된 채널이 존재하지 않는 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            IdentityVerificationAlreadySentError: 본인인증 건이 이미 API로 요청된 상태인 경우
                본인인증 건이 이미 API로 요청된 상태인 경우
            IdentityVerificationAlreadyVerifiedError: 본인인증 건이 이미 인증 완료된 상태인 경우
                본인인증 건이 이미 인증 완료된 상태인 경우
            IdentityVerificationNotFoundError: 요청된 본인인증 건이 존재하지 않는 경우
                요청된 본인인증 건이 존재하지 않는 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            MaxTransactionCountReachedError: 결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
                결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        request_body["channelKey"] = channel_key
        request_body["customer"] = _serialize_send_identity_verification_body_customer(customer)
        if custom_data is not None:
            request_body["customData"] = custom_data
        if bypass is not None:
            request_body["bypass"] = bypass
        request_body["operator"] = _serialize_identity_verification_operator(operator)
        request_body["method"] = _serialize_identity_verification_method(method)
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/identity-verifications/{quote(identity_verification_id, safe='')}/send",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_ALREADY_SENT":
                raise errors.IdentityVerificationAlreadySentError(_deserialize_identity_verification_already_sent_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
                raise errors.IdentityVerificationAlreadyVerifiedError(_deserialize_identity_verification_already_verified_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_NOT_FOUND":
                raise errors.IdentityVerificationNotFoundError(_deserialize_identity_verification_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "MAX_TRANSACTION_COUNT_REACHED":
                raise errors.MaxTransactionCountReachedError(_deserialize_max_transaction_count_reached_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_send_identity_verification_response(response.json())
    def confirm_identity_verification(
        self,
        *,
        identity_verification_id: str,
        otp: Optional[str] = None,
    ) -> ConfirmIdentityVerificationResponse:
        """본인인증 확인

        요청된 본인인증에 대한 확인을 진행합니다.

        Args:
            identity_verification_id (str):
                본인인증 아이디
            otp (str, optional):
                OTP (One-Time Password)

                SMS 방식에서만 사용됩니다.


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            IdentityVerificationAlreadyVerifiedError: 본인인증 건이 이미 인증 완료된 상태인 경우
                본인인증 건이 이미 인증 완료된 상태인 경우
            IdentityVerificationNotFoundError: 요청된 본인인증 건이 존재하지 않는 경우
                요청된 본인인증 건이 존재하지 않는 경우
            IdentityVerificationNotSentError: 본인인증 건이 API로 요청된 상태가 아닌 경우
                본인인증 건이 API로 요청된 상태가 아닌 경우
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
        if otp is not None:
            request_body["otp"] = otp
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/identity-verifications/{quote(identity_verification_id, safe='')}/confirm",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
                raise errors.IdentityVerificationAlreadyVerifiedError(_deserialize_identity_verification_already_verified_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_NOT_FOUND":
                raise errors.IdentityVerificationNotFoundError(_deserialize_identity_verification_not_found_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_NOT_SENT":
                raise errors.IdentityVerificationNotSentError(_deserialize_identity_verification_not_sent_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_confirm_identity_verification_response(response.json())
    async def confirm_identity_verification_async(
        self,
        *,
        identity_verification_id: str,
        otp: Optional[str] = None,
    ) -> ConfirmIdentityVerificationResponse:
        """본인인증 확인

        요청된 본인인증에 대한 확인을 진행합니다.

        Args:
            identity_verification_id (str):
                본인인증 아이디
            otp (str, optional):
                OTP (One-Time Password)

                SMS 방식에서만 사용됩니다.


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            IdentityVerificationAlreadyVerifiedError: 본인인증 건이 이미 인증 완료된 상태인 경우
                본인인증 건이 이미 인증 완료된 상태인 경우
            IdentityVerificationNotFoundError: 요청된 본인인증 건이 존재하지 않는 경우
                요청된 본인인증 건이 존재하지 않는 경우
            IdentityVerificationNotSentError: 본인인증 건이 API로 요청된 상태가 아닌 경우
                본인인증 건이 API로 요청된 상태가 아닌 경우
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
        if otp is not None:
            request_body["otp"] = otp
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/identity-verifications/{quote(identity_verification_id, safe='')}/confirm",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
                raise errors.IdentityVerificationAlreadyVerifiedError(_deserialize_identity_verification_already_verified_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_NOT_FOUND":
                raise errors.IdentityVerificationNotFoundError(_deserialize_identity_verification_not_found_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_NOT_SENT":
                raise errors.IdentityVerificationNotSentError(_deserialize_identity_verification_not_sent_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_confirm_identity_verification_response(response.json())
    def resend_identity_verification(
        self,
        *,
        identity_verification_id: str,
    ) -> ResendIdentityVerificationResponse:
        """SMS 본인인증 요청 재전송

        SMS 본인인증 요청을 재전송합니다.

        Args:
            identity_verification_id (str):
                본인인증 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            IdentityVerificationAlreadyVerifiedError: 본인인증 건이 이미 인증 완료된 상태인 경우
                본인인증 건이 이미 인증 완료된 상태인 경우
            IdentityVerificationNotFoundError: 요청된 본인인증 건이 존재하지 않는 경우
                요청된 본인인증 건이 존재하지 않는 경우
            IdentityVerificationNotSentError: 본인인증 건이 API로 요청된 상태가 아닌 경우
                본인인증 건이 API로 요청된 상태가 아닌 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
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
            "POST",
            f"{self._base_url}/identity-verifications/{quote(identity_verification_id, safe='')}/resend",
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
            if error_type == "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
                raise errors.IdentityVerificationAlreadyVerifiedError(_deserialize_identity_verification_already_verified_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_NOT_FOUND":
                raise errors.IdentityVerificationNotFoundError(_deserialize_identity_verification_not_found_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_NOT_SENT":
                raise errors.IdentityVerificationNotSentError(_deserialize_identity_verification_not_sent_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_resend_identity_verification_response(response.json())
    async def resend_identity_verification_async(
        self,
        *,
        identity_verification_id: str,
    ) -> ResendIdentityVerificationResponse:
        """SMS 본인인증 요청 재전송

        SMS 본인인증 요청을 재전송합니다.

        Args:
            identity_verification_id (str):
                본인인증 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            IdentityVerificationAlreadyVerifiedError: 본인인증 건이 이미 인증 완료된 상태인 경우
                본인인증 건이 이미 인증 완료된 상태인 경우
            IdentityVerificationNotFoundError: 요청된 본인인증 건이 존재하지 않는 경우
                요청된 본인인증 건이 존재하지 않는 경우
            IdentityVerificationNotSentError: 본인인증 건이 API로 요청된 상태가 아닌 경우
                본인인증 건이 API로 요청된 상태가 아닌 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
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
            "POST",
            f"{self._base_url}/identity-verifications/{quote(identity_verification_id, safe='')}/resend",
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
            if error_type == "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
                raise errors.IdentityVerificationAlreadyVerifiedError(_deserialize_identity_verification_already_verified_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_NOT_FOUND":
                raise errors.IdentityVerificationNotFoundError(_deserialize_identity_verification_not_found_error(error_response))
            if error_type == "IDENTITY_VERIFICATION_NOT_SENT":
                raise errors.IdentityVerificationNotSentError(_deserialize_identity_verification_not_sent_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_resend_identity_verification_response(response.json())
