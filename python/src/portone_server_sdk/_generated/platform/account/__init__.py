from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.common.bank import Bank, _deserialize_bank, _serialize_bank
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.platform.account.platform_account_holder import PlatformAccountHolder, _deserialize_platform_account_holder, _serialize_platform_account_holder
from portone_server_sdk._generated.platform.account.platform_external_api_failed_error import PlatformExternalApiFailedError, _deserialize_platform_external_api_failed_error, _serialize_platform_external_api_failed_error
from portone_server_sdk._generated.platform.account.platform_external_api_temporarily_failed_error import PlatformExternalApiTemporarilyFailedError, _deserialize_platform_external_api_temporarily_failed_error, _serialize_platform_external_api_temporarily_failed_error
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from portone_server_sdk._generated.platform.account.platform_not_supported_bank_error import PlatformNotSupportedBankError, _deserialize_platform_not_supported_bank_error, _serialize_platform_not_supported_bank_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from urllib.parse import quote
from portone_server_sdk._generated import errors
class AccountClient:
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
    def get_platform_account_holder(
        self,
        *,
        bank: Bank,
        account_number: str,
        birthdate: Optional[str] = None,
        business_registration_number: Optional[str] = None,
    ) -> PlatformAccountHolder:
        """예금주 조회

        계좌의 예금주를 조회합니다.

        Args:
            bank (Bank):
                은행
            account_number (str):
                '-'를 제외한 계좌 번호
            birthdate (str, optional):
                생년월일

                실명 조회를 위해 추가로 보낼 수 있습니다. birthdate과 businessRegistrationNumber 중 하나만 사용해야 합니다.
            business_registration_number (str, optional):
                사업자등록번호

                실명 조회를 위해 추가로 보낼 수 있습니다. birthdate과 businessRegistrationNumber 중 하나만 사용해야 합니다.


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformExternalApiFailedError: 외부 api 오류
                외부 api 오류
            PlatformExternalApiTemporarilyFailedError: 외부 api의 일시적인 오류
                외부 api의 일시적인 오류
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformNotSupportedBankError: 지원하지 않는 은행인 경우
                지원하지 않는 은행인 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if birthdate is not None:
            query.append(("birthdate", birthdate))
        if business_registration_number is not None:
            query.append(("businessRegistrationNumber", business_registration_number))
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/bank-accounts/{quote(bank, safe='')}/{quote(account_number, safe='')}/holder",
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
            if error_type == "PLATFORM_EXTERNAL_API_FAILED":
                raise errors.PlatformExternalApiFailedError(_deserialize_platform_external_api_failed_error(error_response))
            if error_type == "PLATFORM_EXTERNAL_API_TEMPORARILY_FAILED":
                raise errors.PlatformExternalApiTemporarilyFailedError(_deserialize_platform_external_api_temporarily_failed_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_NOT_SUPPORTED_BANK":
                raise errors.PlatformNotSupportedBankError(_deserialize_platform_not_supported_bank_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_platform_account_holder(response.json())
    async def get_platform_account_holder_async(
        self,
        *,
        bank: Bank,
        account_number: str,
        birthdate: Optional[str] = None,
        business_registration_number: Optional[str] = None,
    ) -> PlatformAccountHolder:
        """예금주 조회

        계좌의 예금주를 조회합니다.

        Args:
            bank (Bank):
                은행
            account_number (str):
                '-'를 제외한 계좌 번호
            birthdate (str, optional):
                생년월일

                실명 조회를 위해 추가로 보낼 수 있습니다. birthdate과 businessRegistrationNumber 중 하나만 사용해야 합니다.
            business_registration_number (str, optional):
                사업자등록번호

                실명 조회를 위해 추가로 보낼 수 있습니다. birthdate과 businessRegistrationNumber 중 하나만 사용해야 합니다.


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformExternalApiFailedError: 외부 api 오류
                외부 api 오류
            PlatformExternalApiTemporarilyFailedError: 외부 api의 일시적인 오류
                외부 api의 일시적인 오류
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformNotSupportedBankError: 지원하지 않는 은행인 경우
                지원하지 않는 은행인 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if birthdate is not None:
            query.append(("birthdate", birthdate))
        if business_registration_number is not None:
            query.append(("businessRegistrationNumber", business_registration_number))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/bank-accounts/{quote(bank, safe='')}/{quote(account_number, safe='')}/holder",
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
            if error_type == "PLATFORM_EXTERNAL_API_FAILED":
                raise errors.PlatformExternalApiFailedError(_deserialize_platform_external_api_failed_error(error_response))
            if error_type == "PLATFORM_EXTERNAL_API_TEMPORARILY_FAILED":
                raise errors.PlatformExternalApiTemporarilyFailedError(_deserialize_platform_external_api_temporarily_failed_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_NOT_SUPPORTED_BANK":
                raise errors.PlatformNotSupportedBankError(_deserialize_platform_not_supported_bank_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_platform_account_holder(response.json())
