from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import ForbiddenError, InvalidRequestError, PlatformExternalApiFailedError, PlatformExternalApiTemporarilyFailedError, PlatformNotEnabledError, PlatformNotSupportedBankError, UnauthorizedError, UnknownError
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...platform.platform_external_api_failed_error import _deserialize_platform_external_api_failed_error
from ...platform.account.platform_external_api_temporarily_failed_error import _deserialize_platform_external_api_temporarily_failed_error
from ...platform.platform_not_enabled_error import _deserialize_platform_not_enabled_error
from ...platform.account.platform_not_supported_bank_error import _deserialize_platform_not_supported_bank_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...common.bank import Bank, _deserialize_bank, _serialize_bank
from ...platform.account.platform_account_holder import PlatformAccountHolder, _deserialize_platform_account_holder, _serialize_platform_account_holder
from urllib.parse import quote
class AccountClient:
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
            GetPlatformAccountHolderError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_platform_external_api_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformExternalApiFailedError(error)
            try:
                error = _deserialize_platform_external_api_temporarily_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformExternalApiTemporarilyFailedError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_not_supported_bank_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotSupportedBankError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            GetPlatformAccountHolderError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_platform_external_api_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformExternalApiFailedError(error)
            try:
                error = _deserialize_platform_external_api_temporarily_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformExternalApiTemporarilyFailedError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_not_supported_bank_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotSupportedBankError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_account_holder(response.json())
