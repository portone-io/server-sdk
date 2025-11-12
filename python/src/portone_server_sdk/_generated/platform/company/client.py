from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import B2bExternalServiceError, B2bNotEnabledError, ForbiddenError, InvalidRequestError, PlatformCompanyNotFoundError, PlatformExternalApiFailedError, PlatformNotEnabledError, UnauthorizedError, UnknownError
from ...common.b2b_external_service_error import _deserialize_b2b_external_service_error
from ...common.b2b_not_enabled_error import _deserialize_b2b_not_enabled_error
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...platform.company.platform_company_not_found_error import _deserialize_platform_company_not_found_error
from ...platform.platform_external_api_failed_error import _deserialize_platform_external_api_failed_error
from ...platform.platform_not_enabled_error import _deserialize_platform_not_enabled_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...platform.company.get_b2b_business_infos_response import GetB2bBusinessInfosResponse, _deserialize_get_b2b_business_infos_response, _serialize_get_b2b_business_infos_response
from ...platform.company.get_platform_company_state_payload import GetPlatformCompanyStatePayload, _deserialize_get_platform_company_state_payload, _serialize_get_platform_company_state_payload
from urllib.parse import quote
class CompanyClient:
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
    def get_b2b_business_infos(
        self,
        *,
        brn_list: list[str],
    ) -> GetB2bBusinessInfosResponse:
        """사업자등록 정보조회

        요청된 사업자등록번호 리스트에 해당하는 사업자등록 정보를 조회합니다.
        해당 API 사용을 위해서는 별도 문의가 필요합니다.

        Args:
            brn_list (list[str]):
                조회할 사업자등록번호 리스트


        Raises:
            GetB2bBusinessInfosError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["brnList"] = brn_list
        query = []
        response = self._sync_client.request(
            "POST",
            f"{self._base_url}/b2b/companies/business-info",
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
                error = _deserialize_b2b_external_service_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bExternalServiceError(error)
            try:
                error = _deserialize_b2b_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bNotEnabledError(error)
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
        return _deserialize_get_b2b_business_infos_response(response.json())
    async def get_b2b_business_infos_async(
        self,
        *,
        brn_list: list[str],
    ) -> GetB2bBusinessInfosResponse:
        """사업자등록 정보조회

        요청된 사업자등록번호 리스트에 해당하는 사업자등록 정보를 조회합니다.
        해당 API 사용을 위해서는 별도 문의가 필요합니다.

        Args:
            brn_list (list[str]):
                조회할 사업자등록번호 리스트


        Raises:
            GetB2bBusinessInfosError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["brnList"] = brn_list
        query = []
        response = await self._async_client.request(
            "POST",
            f"{self._base_url}/b2b/companies/business-info",
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
                error = _deserialize_b2b_external_service_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bExternalServiceError(error)
            try:
                error = _deserialize_b2b_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bNotEnabledError(error)
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
        return _deserialize_get_b2b_business_infos_response(response.json())
    def get_platform_company_state(
        self,
        *,
        business_registration_number: str,
        test: Optional[bool] = None,
    ) -> GetPlatformCompanyStatePayload:
        """사업자 조회

        사업자 정보를 조회합니다. 포트원 서비스에 연동 및 등록되지 않은 사업자도 조회 가능합니다.

        Args:
            business_registration_number (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformCompanyStateError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
    ) -> GetPlatformCompanyStatePayload:
        """사업자 조회

        사업자 정보를 조회합니다. 포트원 서비스에 연동 및 등록되지 않은 사업자도 조회 가능합니다.

        Args:
            business_registration_number (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformCompanyStateError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
