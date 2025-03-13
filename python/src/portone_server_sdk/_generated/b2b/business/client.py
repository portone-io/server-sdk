from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import B2bExternalServiceError, B2bNotEnabledError, ForbiddenError, InvalidRequestError, UnauthorizedError, UnknownError
from ...b2b.business.b2b_external_service_error import _deserialize_b2b_external_service_error
from ...b2b.business.b2b_not_enabled_error import _deserialize_b2b_not_enabled_error
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...b2b.business.get_b2b_business_infos_response import GetB2bBusinessInfosResponse, _deserialize_get_b2b_business_infos_response, _serialize_get_b2b_business_infos_response
from urllib.parse import quote
class BusinessClient:
    _secret: str
    _base_url: str
    _store_id: Optional[str]
    _client: AsyncClient

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
        self._client = AsyncClient()
    def get_b2b_business_infos(
        self,
        *,
        brn_list: list[str],
    ) -> GetB2bBusinessInfosResponse:
        """사업자 정보 조회

        요청된 사업자번호에 해당하는 사업자의 정보를 조회합니다.

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
        response = httpx.request(
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
        """사업자 정보 조회

        요청된 사업자번호에 해당하는 사업자의 정보를 조회합니다.

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
        response = await self._client.request(
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
