from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ..._user_agent import USER_AGENT
from typing import Optional
from ..errors import ChannelNotFoundError, ForbiddenError, IdentityVerificationAlreadySentError, IdentityVerificationAlreadyVerifiedError, IdentityVerificationNotFoundError, IdentityVerificationNotSentError, InvalidRequestError, MaxTransactionCountReachedError, PgProviderError, UnauthorizedError, UnknownError
from ..common.channel_not_found_error import _deserialize_channel_not_found_error
from ..common.forbidden_error import _deserialize_forbidden_error
from ..identity_verification.identity_verification_already_sent_error import _deserialize_identity_verification_already_sent_error
from ..identity_verification.identity_verification_already_verified_error import _deserialize_identity_verification_already_verified_error
from ..identity_verification.identity_verification_not_found_error import _deserialize_identity_verification_not_found_error
from ..identity_verification.identity_verification_not_sent_error import _deserialize_identity_verification_not_sent_error
from ..common.invalid_request_error import _deserialize_invalid_request_error
from ..common.max_transaction_count_reached_error import _deserialize_max_transaction_count_reached_error
from ..common.pg_provider_error import _deserialize_pg_provider_error
from ..common.unauthorized_error import _deserialize_unauthorized_error
from ..identity_verification.confirm_identity_verification_response import ConfirmIdentityVerificationResponse, _deserialize_confirm_identity_verification_response, _serialize_confirm_identity_verification_response
from ..identity_verification.identity_verification import IdentityVerification, _deserialize_identity_verification, _serialize_identity_verification
from ..identity_verification.identity_verification_method import IdentityVerificationMethod, _deserialize_identity_verification_method, _serialize_identity_verification_method
from ..identity_verification.identity_verification_operator import IdentityVerificationOperator, _deserialize_identity_verification_operator, _serialize_identity_verification_operator
from ..identity_verification.resend_identity_verification_response import ResendIdentityVerificationResponse, _deserialize_resend_identity_verification_response, _serialize_resend_identity_verification_response
from ..identity_verification.send_identity_verification_body_customer import SendIdentityVerificationBodyCustomer, _deserialize_send_identity_verification_body_customer, _serialize_send_identity_verification_body_customer
from ..identity_verification.send_identity_verification_response import SendIdentityVerificationResponse, _deserialize_send_identity_verification_response, _serialize_send_identity_verification_response
from urllib.parse import quote
class IdentityVerificationClient:
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
            GetIdentityVerificationError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_identity_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationNotFoundError(error)
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
            GetIdentityVerificationError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_identity_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationNotFoundError(error)
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
            SendIdentityVerificationError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_identity_verification_already_sent_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationAlreadySentError(error)
            try:
                error = _deserialize_identity_verification_already_verified_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationAlreadyVerifiedError(error)
            try:
                error = _deserialize_identity_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationNotFoundError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_max_transaction_count_reached_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise MaxTransactionCountReachedError(error)
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
            SendIdentityVerificationError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_identity_verification_already_sent_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationAlreadySentError(error)
            try:
                error = _deserialize_identity_verification_already_verified_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationAlreadyVerifiedError(error)
            try:
                error = _deserialize_identity_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationNotFoundError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_max_transaction_count_reached_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise MaxTransactionCountReachedError(error)
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
            ConfirmIdentityVerificationError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_identity_verification_already_verified_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationAlreadyVerifiedError(error)
            try:
                error = _deserialize_identity_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationNotFoundError(error)
            try:
                error = _deserialize_identity_verification_not_sent_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationNotSentError(error)
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
            ConfirmIdentityVerificationError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_identity_verification_already_verified_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationAlreadyVerifiedError(error)
            try:
                error = _deserialize_identity_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationNotFoundError(error)
            try:
                error = _deserialize_identity_verification_not_sent_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationNotSentError(error)
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
            ResendIdentityVerificationError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_identity_verification_already_verified_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationAlreadyVerifiedError(error)
            try:
                error = _deserialize_identity_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationNotFoundError(error)
            try:
                error = _deserialize_identity_verification_not_sent_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationNotSentError(error)
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
            ResendIdentityVerificationError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_identity_verification_already_verified_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationAlreadyVerifiedError(error)
            try:
                error = _deserialize_identity_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationNotFoundError(error)
            try:
                error = _deserialize_identity_verification_not_sent_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise IdentityVerificationNotSentError(error)
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
        return _deserialize_resend_identity_verification_response(response.json())
