from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import ForbiddenError, InvalidRequestError, PlatformCompanyNotFoundError, PlatformExternalApiFailedError, PlatformNotEnabledError, UnauthorizedError, UnknownError
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...platform.company.platform_company_not_found_error import _deserialize_platform_company_not_found_error
from ...platform.platform_external_api_failed_error import _deserialize_platform_external_api_failed_error
from ...platform.platform_not_enabled_error import _deserialize_platform_not_enabled_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...platform.company.get_platform_company_state_payload import GetPlatformCompanyStatePayload, _deserialize_get_platform_company_state_payload, _serialize_get_platform_company_state_payload
from urllib.parse import quote
class CompanyClient:
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
    def get_platform_company_state(
        self,
        *,
        business_registration_number: str,
    ) -> GetPlatformCompanyStatePayload:
        """사업자 조회

        사업자 정보를 조회합니다. 포트원 서비스에 연동 및 등록되지 않은 사업자도 조회 가능합니다.

        Args:
            business_registration_number (str):
                사업자등록번호


        Raises:
            GetPlatformCompanyStateError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/companies/{quote(business_registration_number, safe='')}/state",
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
                error = _deserialize_platform_company_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCompanyNotFoundError(error)
            try:
                error = _deserialize_platform_external_api_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformExternalApiFailedError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_get_platform_company_state_payload(response.json())
    async def get_platform_company_state_async(
        self,
        *,
        business_registration_number: str,
    ) -> GetPlatformCompanyStatePayload:
        """사업자 조회

        사업자 정보를 조회합니다. 포트원 서비스에 연동 및 등록되지 않은 사업자도 조회 가능합니다.

        Args:
            business_registration_number (str):
                사업자등록번호


        Raises:
            GetPlatformCompanyStateError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/companies/{quote(business_registration_number, safe='')}/state",
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
                error = _deserialize_platform_company_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCompanyNotFoundError(error)
            try:
                error = _deserialize_platform_external_api_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformExternalApiFailedError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_get_platform_company_state_payload(response.json())
