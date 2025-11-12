from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
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
    def get_platform_account_holder(
        self,
        *,
        bank: Bank,
        account_number: str,
        test: Optional[bool] = None,
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
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        if birthdate is not None:
            query.append(("birthdate", birthdate))
        if business_registration_number is not None:
            query.append(("businessRegistrationNumber", business_registration_number))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
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
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        if birthdate is not None:
            query.append(("birthdate", birthdate))
        if business_registration_number is not None:
            query.append(("businessRegistrationNumber", business_registration_number))
        response = await self._async_client.request(
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
