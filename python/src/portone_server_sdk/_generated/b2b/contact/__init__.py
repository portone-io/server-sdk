from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.common.b2b_company_contact import B2bCompanyContact, _deserialize_b2b_company_contact, _serialize_b2b_company_contact
from portone_server_sdk._generated.b2b.contact.b2b_contact_not_found_error import B2bContactNotFoundError, _deserialize_b2b_contact_not_found_error, _serialize_b2b_contact_not_found_error
from portone_server_sdk._generated.common.b2b_external_service_error import B2bExternalServiceError, _deserialize_b2b_external_service_error, _serialize_b2b_external_service_error
from portone_server_sdk._generated.common.b2b_member_company_not_found_error import B2bMemberCompanyNotFoundError, _deserialize_b2b_member_company_not_found_error, _serialize_b2b_member_company_not_found_error
from portone_server_sdk._generated.common.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.b2b.contact.get_b2b_contact_id_existence_response import GetB2bContactIdExistenceResponse, _deserialize_get_b2b_contact_id_existence_response, _serialize_get_b2b_contact_id_existence_response
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from portone_server_sdk._generated.b2b.contact.update_b2b_contact_response import UpdateB2bContactResponse, _deserialize_update_b2b_contact_response, _serialize_update_b2b_contact_response
from portone_server_sdk._generated import errors
class ContactClient:
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
    def get_b2b_contact(
        self,
        *,
        contact_id: str,
        test: Optional[bool] = None,
    ) -> B2bCompanyContact:
        """담당자 조회

        연동 사업자에 등록된 담당자를 조회합니다.

        Args:
            contact_id (str):
                담당자 ID
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bContactNotFoundError: 담당자가 존재하지 않는 경우
                담당자가 존재하지 않는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bMemberCompanyNotFoundError: 연동 사업자가 존재하지 않는 경우
                연동 사업자가 존재하지 않는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b/contacts/{contact_id}",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_CONTACT_NOT_FOUND":
                raise errors.B2bContactNotFoundError(_deserialize_b2b_contact_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_deserialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_company_contact(response.json())
    async def get_b2b_contact_async(
        self,
        *,
        contact_id: str,
        test: Optional[bool] = None,
    ) -> B2bCompanyContact:
        """담당자 조회

        연동 사업자에 등록된 담당자를 조회합니다.

        Args:
            contact_id (str):
                담당자 ID
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bContactNotFoundError: 담당자가 존재하지 않는 경우
                담당자가 존재하지 않는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bMemberCompanyNotFoundError: 연동 사업자가 존재하지 않는 경우
                연동 사업자가 존재하지 않는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b/contacts/{contact_id}",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_CONTACT_NOT_FOUND":
                raise errors.B2bContactNotFoundError(_deserialize_b2b_contact_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_deserialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_company_contact(response.json())
    def update_b2b_contact(
        self,
        *,
        contact_id: str,
        test: Optional[bool] = None,
        password: Optional[str] = None,
        name: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
    ) -> UpdateB2bContactResponse:
        """담당자 정보 수정

        담당자 정보를 수정합니다.

        Args:
            contact_id (str):
                담당자 ID
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            password (str, optional):
                비밀번호
            name (str, optional):
                담당자 성명
            phone_number (str, optional):
                담당자 핸드폰 번호
            email (str, optional):
                담당자 이메일


        Raises:
            B2bContactNotFoundError: 담당자가 존재하지 않는 경우
                담당자가 존재하지 않는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bMemberCompanyNotFoundError: 연동 사업자가 존재하지 않는 경우
                연동 사업자가 존재하지 않는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
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
        if password is not None:
            request_body["password"] = password,
        if name is not None:
            request_body["name"] = name,
        if phone_number is not None:
            request_body["phoneNumber"] = phone_number,
        if email is not None:
            request_body["email"] = email,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "PATCH",
            f"{self._base_url}/b2b/contacts/{contact_id}",
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
            if error_type == "B2B_CONTACT_NOT_FOUND":
                raise errors.B2bContactNotFoundError(_deserialize_b2b_contact_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_deserialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_update_b2b_contact_response(response.json())
    async def update_b2b_contact_async(
        self,
        *,
        contact_id: str,
        test: Optional[bool] = None,
        password: Optional[str] = None,
        name: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
    ) -> UpdateB2bContactResponse:
        """담당자 정보 수정

        담당자 정보를 수정합니다.

        Args:
            contact_id (str):
                담당자 ID
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            password (str, optional):
                비밀번호
            name (str, optional):
                담당자 성명
            phone_number (str, optional):
                담당자 핸드폰 번호
            email (str, optional):
                담당자 이메일


        Raises:
            B2bContactNotFoundError: 담당자가 존재하지 않는 경우
                담당자가 존재하지 않는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bMemberCompanyNotFoundError: 연동 사업자가 존재하지 않는 경우
                연동 사업자가 존재하지 않는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
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
        if password is not None:
            request_body["password"] = password,
        if name is not None:
            request_body["name"] = name,
        if phone_number is not None:
            request_body["phoneNumber"] = phone_number,
        if email is not None:
            request_body["email"] = email,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "PATCH",
            f"{self._base_url}/b2b/contacts/{contact_id}",
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
            if error_type == "B2B_CONTACT_NOT_FOUND":
                raise errors.B2bContactNotFoundError(_deserialize_b2b_contact_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_deserialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_update_b2b_contact_response(response.json())
    def get_b2b_contact_id_existence(
        self,
        *,
        contact_id: str,
        test: Optional[bool] = None,
    ) -> GetB2bContactIdExistenceResponse:
        """담당자 ID 존재 여부 확인

        담당자 ID가 이미 사용중인지 확인합니다.

        Args:
            contact_id (str):
                담당자 ID
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b/contacts/{contact_id}/exists",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_contact_id_existence_response(response.json())
    async def get_b2b_contact_id_existence_async(
        self,
        *,
        contact_id: str,
        test: Optional[bool] = None,
    ) -> GetB2bContactIdExistenceResponse:
        """담당자 ID 존재 여부 확인

        담당자 ID가 이미 사용중인지 확인합니다.

        Args:
            contact_id (str):
                담당자 ID
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b/contacts/{contact_id}/exists",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_contact_id_existence_response(response.json())
