from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.b2b.member_company.b2b_bank_account_not_found_error import B2bBankAccountNotFoundError, _deserialize_b2b_bank_account_not_found_error, _serialize_b2b_bank_account_not_found_error
from portone_server_sdk._generated.b2b.member_company.b2b_certificate import B2bCertificate, _deserialize_b2b_certificate, _serialize_b2b_certificate
from portone_server_sdk._generated.b2b.member_company.b2b_certificate_unregistered_error import B2bCertificateUnregisteredError, _deserialize_b2b_certificate_unregistered_error, _serialize_b2b_certificate_unregistered_error
from portone_server_sdk._generated.b2b.member_company.b2b_company_already_registered_error import B2bCompanyAlreadyRegisteredError, _deserialize_b2b_company_already_registered_error, _serialize_b2b_company_already_registered_error
from portone_server_sdk._generated.b2b.member_company.b2b_company_contact_input import B2bCompanyContactInput, _deserialize_b2b_company_contact_input, _serialize_b2b_company_contact_input
from portone_server_sdk._generated.b2b.member_company.b2b_company_not_found_error import B2bCompanyNotFoundError, _deserialize_b2b_company_not_found_error, _serialize_b2b_company_not_found_error
from portone_server_sdk._generated.b2b.member_company.b2b_company_state import B2bCompanyState, _deserialize_b2b_company_state, _serialize_b2b_company_state
from portone_server_sdk._generated.common.b2b_external_service_error import B2bExternalServiceError, _deserialize_b2b_external_service_error, _serialize_b2b_external_service_error
from portone_server_sdk._generated.b2b.member_company.b2b_financial_system_communication_error import B2bFinancialSystemCommunicationError, _deserialize_b2b_financial_system_communication_error, _serialize_b2b_financial_system_communication_error
from portone_server_sdk._generated.b2b.member_company.b2b_financial_system_failure_error import B2bFinancialSystemFailureError, _deserialize_b2b_financial_system_failure_error, _serialize_b2b_financial_system_failure_error
from portone_server_sdk._generated.b2b.member_company.b2b_financial_system_under_maintenance_error import B2bFinancialSystemUnderMaintenanceError, _deserialize_b2b_financial_system_under_maintenance_error, _serialize_b2b_financial_system_under_maintenance_error
from portone_server_sdk._generated.b2b.member_company.b2b_foreign_exchange_account_error import B2bForeignExchangeAccountError, _deserialize_b2b_foreign_exchange_account_error, _serialize_b2b_foreign_exchange_account_error
from portone_server_sdk._generated.b2b.member_company.b2b_hometax_under_maintenance_error import B2bHometaxUnderMaintenanceError, _deserialize_b2b_hometax_under_maintenance_error, _serialize_b2b_hometax_under_maintenance_error
from portone_server_sdk._generated.common.b2b_id_already_exists_error import B2bIdAlreadyExistsError, _deserialize_b2b_id_already_exists_error, _serialize_b2b_id_already_exists_error
from portone_server_sdk._generated.b2b.member_company.b2b_member_company import B2bMemberCompany, _deserialize_b2b_member_company, _serialize_b2b_member_company
from portone_server_sdk._generated.b2b.member_company.b2b_member_company_input import B2bMemberCompanyInput, _deserialize_b2b_member_company_input, _serialize_b2b_member_company_input
from portone_server_sdk._generated.common.b2b_member_company_not_found_error import B2bMemberCompanyNotFoundError, _deserialize_b2b_member_company_not_found_error, _serialize_b2b_member_company_not_found_error
from portone_server_sdk._generated.common.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from portone_server_sdk._generated.b2b.member_company.b2b_regular_maintenance_time_error import B2bRegularMaintenanceTimeError, _deserialize_b2b_regular_maintenance_time_error, _serialize_b2b_regular_maintenance_time_error
from portone_server_sdk._generated.b2b.member_company.b2b_suspended_account_error import B2bSuspendedAccountError, _deserialize_b2b_suspended_account_error, _serialize_b2b_suspended_account_error
from portone_server_sdk._generated.common.bank import Bank, _deserialize_bank, _serialize_bank
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.b2b.member_company.get_b2b_bank_account_holder_response import GetB2bBankAccountHolderResponse, _deserialize_get_b2b_bank_account_holder_response, _serialize_get_b2b_bank_account_holder_response
from portone_server_sdk._generated.b2b.member_company.get_b2b_certificate_registration_url_response import GetB2bCertificateRegistrationUrlResponse, _deserialize_get_b2b_certificate_registration_url_response, _serialize_get_b2b_certificate_registration_url_response
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.b2b.member_company.register_b2b_member_company_response import RegisterB2bMemberCompanyResponse, _deserialize_register_b2b_member_company_response, _serialize_register_b2b_member_company_response
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from portone_server_sdk._generated.b2b.member_company.update_b2b_member_company_response import UpdateB2bMemberCompanyResponse, _deserialize_update_b2b_member_company_response, _serialize_update_b2b_member_company_response
from portone_server_sdk._generated.b2b.member_company.validate_b2b_certificate_response import ValidateB2bCertificateResponse, _deserialize_validate_b2b_certificate_response, _serialize_validate_b2b_certificate_response
from portone_server_sdk._generated import errors
class MemberCompanyClient:
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
    def get_b2b_member_company(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> B2bMemberCompany:
        """연동 사업자 조회

        포트원 B2B 서비스에 연동된 사업자를 조회합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
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
            f"{self._base_url}/b2b/member-companies/{brn}",
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
        return _deserialize_b2b_member_company(response.json())
    async def get_b2b_member_company_async(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> B2bMemberCompany:
        """연동 사업자 조회

        포트원 B2B 서비스에 연동된 사업자를 조회합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
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
            f"{self._base_url}/b2b/member-companies/{brn}",
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
        return _deserialize_b2b_member_company(response.json())
    def update_b2b_member_company(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
        company_name: Optional[str] = None,
        representative_name: Optional[str] = None,
        address: Optional[str] = None,
        business_type: Optional[str] = None,
        business_class: Optional[str] = None,
    ) -> UpdateB2bMemberCompanyResponse:
        """연동 사업자 정보 수정

        연동 사업자 정보를 수정합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            company_name (str, optional):
                회사명
            representative_name (str, optional):
                대표자 성명
            address (str, optional):
                회사 주소
            business_type (str, optional):
                업태
            business_class (str, optional):
                업종


        Raises:
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
        if company_name is not None:
            request_body["companyName"] = company_name,
        if representative_name is not None:
            request_body["representativeName"] = representative_name,
        if address is not None:
            request_body["address"] = address,
        if business_type is not None:
            request_body["businessType"] = business_type,
        if business_class is not None:
            request_body["businessClass"] = business_class,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "PATCH",
            f"{self._base_url}/b2b/member-companies/{brn}",
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
        return _deserialize_update_b2b_member_company_response(response.json())
    async def update_b2b_member_company_async(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
        company_name: Optional[str] = None,
        representative_name: Optional[str] = None,
        address: Optional[str] = None,
        business_type: Optional[str] = None,
        business_class: Optional[str] = None,
    ) -> UpdateB2bMemberCompanyResponse:
        """연동 사업자 정보 수정

        연동 사업자 정보를 수정합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            company_name (str, optional):
                회사명
            representative_name (str, optional):
                대표자 성명
            address (str, optional):
                회사 주소
            business_type (str, optional):
                업태
            business_class (str, optional):
                업종


        Raises:
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
        if company_name is not None:
            request_body["companyName"] = company_name,
        if representative_name is not None:
            request_body["representativeName"] = representative_name,
        if address is not None:
            request_body["address"] = address,
        if business_type is not None:
            request_body["businessType"] = business_type,
        if business_class is not None:
            request_body["businessClass"] = business_class,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "PATCH",
            f"{self._base_url}/b2b/member-companies/{brn}",
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
        return _deserialize_update_b2b_member_company_response(response.json())
    def register_b2b_member_company(
        self,
        *,
        test: Optional[bool] = None,
        company: B2bMemberCompanyInput,
        contact: B2bCompanyContactInput,
    ) -> RegisterB2bMemberCompanyResponse:
        """사업자 연동

        포트원 B2B 서비스에 사업자를 연동합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            company (B2bMemberCompanyInput):
                사업자 정보
            contact (B2bCompanyContactInput):
                담당자 정보


        Raises:
            B2bCompanyAlreadyRegisteredError: 사업자가 이미 연동되어 있는 경우
                사업자가 이미 연동되어 있는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bIdAlreadyExistsError: ID가 이미 사용중인 경우
                ID가 이미 사용중인 경우
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
        request_body["company"] = _serialize_b2b_member_company_input(company),
        request_body["contact"] = _serialize_b2b_company_contact_input(contact),
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b/member-companies",
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
            if error_type == "B2B_COMPANY_ALREADY_REGISTERED":
                raise errors.B2bCompanyAlreadyRegisteredError(_deserialize_b2b_company_already_registered_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_ID_ALREADY_EXISTS":
                raise errors.B2bIdAlreadyExistsError(_deserialize_b2b_id_already_exists_error(error_response))
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
        return _deserialize_register_b2b_member_company_response(response.json())
    async def register_b2b_member_company_async(
        self,
        *,
        test: Optional[bool] = None,
        company: B2bMemberCompanyInput,
        contact: B2bCompanyContactInput,
    ) -> RegisterB2bMemberCompanyResponse:
        """사업자 연동

        포트원 B2B 서비스에 사업자를 연동합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            company (B2bMemberCompanyInput):
                사업자 정보
            contact (B2bCompanyContactInput):
                담당자 정보


        Raises:
            B2bCompanyAlreadyRegisteredError: 사업자가 이미 연동되어 있는 경우
                사업자가 이미 연동되어 있는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bIdAlreadyExistsError: ID가 이미 사용중인 경우
                ID가 이미 사용중인 경우
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
        request_body["company"] = _serialize_b2b_member_company_input(company),
        request_body["contact"] = _serialize_b2b_company_contact_input(contact),
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b/member-companies",
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
            if error_type == "B2B_COMPANY_ALREADY_REGISTERED":
                raise errors.B2bCompanyAlreadyRegisteredError(_deserialize_b2b_company_already_registered_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_ID_ALREADY_EXISTS":
                raise errors.B2bIdAlreadyExistsError(_deserialize_b2b_id_already_exists_error(error_response))
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
        return _deserialize_register_b2b_member_company_response(response.json())
    def get_b2b_certificate_registration_url(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> GetB2bCertificateRegistrationUrlResponse:
        """사업자 인증서 등록 URL 조회

        연동 사업자의 인증서를 등록하기 위한 URL을 조회합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
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
            f"{self._base_url}/b2b/member-companies/{brn}/certificate/registration-url",
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
        return _deserialize_get_b2b_certificate_registration_url_response(response.json())
    async def get_b2b_certificate_registration_url_async(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> GetB2bCertificateRegistrationUrlResponse:
        """사업자 인증서 등록 URL 조회

        연동 사업자의 인증서를 등록하기 위한 URL을 조회합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
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
            f"{self._base_url}/b2b/member-companies/{brn}/certificate/registration-url",
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
        return _deserialize_get_b2b_certificate_registration_url_response(response.json())
    def validate_b2b_certificate(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> ValidateB2bCertificateResponse:
        """사업자 인증서 유효성 검증

        연동 사업자가 등록한 인증서의 유효성을 검증합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bCertificateUnregisteredError: 인증서가 등록되어 있지 않은 경우
                인증서가 등록되어 있지 않은 경우
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
            "POST",
            f"{self._base_url}/b2b/member-companies/{brn}/certificate/validate",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_CERTIFICATE_UNREGISTERED":
                raise errors.B2bCertificateUnregisteredError(_deserialize_b2b_certificate_unregistered_error(error_response))
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
        return _deserialize_validate_b2b_certificate_response(response.json())
    async def validate_b2b_certificate_async(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> ValidateB2bCertificateResponse:
        """사업자 인증서 유효성 검증

        연동 사업자가 등록한 인증서의 유효성을 검증합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bCertificateUnregisteredError: 인증서가 등록되어 있지 않은 경우
                인증서가 등록되어 있지 않은 경우
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
            "POST",
            f"{self._base_url}/b2b/member-companies/{brn}/certificate/validate",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_CERTIFICATE_UNREGISTERED":
                raise errors.B2bCertificateUnregisteredError(_deserialize_b2b_certificate_unregistered_error(error_response))
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
        return _deserialize_validate_b2b_certificate_response(response.json())
    def get_b2b_certificate(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> B2bCertificate:
        """인증서 조회

        연동 사업자의 인증서를 조회합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bCertificateUnregisteredError: 인증서가 등록되어 있지 않은 경우
                인증서가 등록되어 있지 않은 경우
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
            f"{self._base_url}/b2b/member-companies/{brn}/certificate",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_CERTIFICATE_UNREGISTERED":
                raise errors.B2bCertificateUnregisteredError(_deserialize_b2b_certificate_unregistered_error(error_response))
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
        return _deserialize_b2b_certificate(response.json())
    async def get_b2b_certificate_async(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> B2bCertificate:
        """인증서 조회

        연동 사업자의 인증서를 조회합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bCertificateUnregisteredError: 인증서가 등록되어 있지 않은 경우
                인증서가 등록되어 있지 않은 경우
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
            f"{self._base_url}/b2b/member-companies/{brn}/certificate",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_CERTIFICATE_UNREGISTERED":
                raise errors.B2bCertificateUnregisteredError(_deserialize_b2b_certificate_unregistered_error(error_response))
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
        return _deserialize_b2b_certificate(response.json())
    def get_b2b_bank_account_holder(
        self,
        *,
        test: Optional[bool] = None,
        bank: Bank,
        account_number: str,
    ) -> GetB2bBankAccountHolderResponse:
        """예금주 조회

        원하는 계좌의 예금주를 조회합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            bank (Bank):
                은행
            account_number (str):
                계좌번호


        Raises:
            B2bBankAccountNotFoundError: 계좌가 존재하지 않는 경우
                계좌가 존재하지 않는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bFinancialSystemCommunicationError: 금융기관과의 통신에 실패한 경우
                금융기관과의 통신에 실패한 경우
            B2bFinancialSystemFailureError: 금융기관 장애
                금융기관 장애
            B2bFinancialSystemUnderMaintenanceError: 금융기관 시스템이 점검 중인 경우
                금융기관 시스템이 점검 중인 경우
            B2bForeignExchangeAccountError: 계좌 정보 조회가 불가능한 외화 계좌인 경우
                계좌 정보 조회가 불가능한 외화 계좌인 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bRegularMaintenanceTimeError: 금융기관 시스템이 정기 점검 중인 경우
                금융기관 시스템이 정기 점검 중인 경우
            B2bSuspendedAccountError: 정지 계좌인 경우
                정지 계좌인 경우
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
        request_body["bank"] = _serialize_bank(bank),
        request_body["accountNumber"] = account_number,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b/bank-accounts/holder",
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
            if error_type == "B2B_BANK_ACCOUNT_NOT_FOUND":
                raise errors.B2bBankAccountNotFoundError(_deserialize_b2b_bank_account_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_FINANCIAL_SYSTEM_COMMUNICATION":
                raise errors.B2bFinancialSystemCommunicationError(_deserialize_b2b_financial_system_communication_error(error_response))
            if error_type == "B2B_FINANCIAL_SYSTEM_FAILURE":
                raise errors.B2bFinancialSystemFailureError(_deserialize_b2b_financial_system_failure_error(error_response))
            if error_type == "B2B_FINANCIAL_SYSTEM_UNDER_MAINTENANCE":
                raise errors.B2bFinancialSystemUnderMaintenanceError(_deserialize_b2b_financial_system_under_maintenance_error(error_response))
            if error_type == "B2B_FOREIGN_EXCHANGE_ACCOUNT":
                raise errors.B2bForeignExchangeAccountError(_deserialize_b2b_foreign_exchange_account_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_REGULAR_MAINTENANCE_TIME":
                raise errors.B2bRegularMaintenanceTimeError(_deserialize_b2b_regular_maintenance_time_error(error_response))
            if error_type == "B2B_SUSPENDED_ACCOUNT":
                raise errors.B2bSuspendedAccountError(_deserialize_b2b_suspended_account_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_bank_account_holder_response(response.json())
    async def get_b2b_bank_account_holder_async(
        self,
        *,
        test: Optional[bool] = None,
        bank: Bank,
        account_number: str,
    ) -> GetB2bBankAccountHolderResponse:
        """예금주 조회

        원하는 계좌의 예금주를 조회합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            bank (Bank):
                은행
            account_number (str):
                계좌번호


        Raises:
            B2bBankAccountNotFoundError: 계좌가 존재하지 않는 경우
                계좌가 존재하지 않는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bFinancialSystemCommunicationError: 금융기관과의 통신에 실패한 경우
                금융기관과의 통신에 실패한 경우
            B2bFinancialSystemFailureError: 금융기관 장애
                금융기관 장애
            B2bFinancialSystemUnderMaintenanceError: 금융기관 시스템이 점검 중인 경우
                금융기관 시스템이 점검 중인 경우
            B2bForeignExchangeAccountError: 계좌 정보 조회가 불가능한 외화 계좌인 경우
                계좌 정보 조회가 불가능한 외화 계좌인 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bRegularMaintenanceTimeError: 금융기관 시스템이 정기 점검 중인 경우
                금융기관 시스템이 정기 점검 중인 경우
            B2bSuspendedAccountError: 정지 계좌인 경우
                정지 계좌인 경우
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
        request_body["bank"] = _serialize_bank(bank),
        request_body["accountNumber"] = account_number,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b/bank-accounts/holder",
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
            if error_type == "B2B_BANK_ACCOUNT_NOT_FOUND":
                raise errors.B2bBankAccountNotFoundError(_deserialize_b2b_bank_account_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_FINANCIAL_SYSTEM_COMMUNICATION":
                raise errors.B2bFinancialSystemCommunicationError(_deserialize_b2b_financial_system_communication_error(error_response))
            if error_type == "B2B_FINANCIAL_SYSTEM_FAILURE":
                raise errors.B2bFinancialSystemFailureError(_deserialize_b2b_financial_system_failure_error(error_response))
            if error_type == "B2B_FINANCIAL_SYSTEM_UNDER_MAINTENANCE":
                raise errors.B2bFinancialSystemUnderMaintenanceError(_deserialize_b2b_financial_system_under_maintenance_error(error_response))
            if error_type == "B2B_FOREIGN_EXCHANGE_ACCOUNT":
                raise errors.B2bForeignExchangeAccountError(_deserialize_b2b_foreign_exchange_account_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_REGULAR_MAINTENANCE_TIME":
                raise errors.B2bRegularMaintenanceTimeError(_deserialize_b2b_regular_maintenance_time_error(error_response))
            if error_type == "B2B_SUSPENDED_ACCOUNT":
                raise errors.B2bSuspendedAccountError(_deserialize_b2b_suspended_account_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_bank_account_holder_response(response.json())
    def get_b2b_company_state(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> B2bCompanyState:
        """사업자 상태 조회

        원하는 사업자의 상태를 조회합니다. 포트원 B2B 서비스에 연동 및 등록되지 않은 사업자도 조회 가능합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bCompanyNotFoundError: 사업자가 존재하지 않는 경우
                사업자가 존재하지 않는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bHometaxUnderMaintenanceError: 홈택스가 점검중이거나 순단이 발생한 경우
                홈택스가 점검중이거나 순단이 발생한 경우
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
            f"{self._base_url}/b2b/companies/{brn}/state",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_COMPANY_NOT_FOUND":
                raise errors.B2bCompanyNotFoundError(_deserialize_b2b_company_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_HOMETAX_UNDER_MAINTENANCE":
                raise errors.B2bHometaxUnderMaintenanceError(_deserialize_b2b_hometax_under_maintenance_error(error_response))
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
        return _deserialize_b2b_company_state(response.json())
    async def get_b2b_company_state_async(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> B2bCompanyState:
        """사업자 상태 조회

        원하는 사업자의 상태를 조회합니다. 포트원 B2B 서비스에 연동 및 등록되지 않은 사업자도 조회 가능합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bCompanyNotFoundError: 사업자가 존재하지 않는 경우
                사업자가 존재하지 않는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bHometaxUnderMaintenanceError: 홈택스가 점검중이거나 순단이 발생한 경우
                홈택스가 점검중이거나 순단이 발생한 경우
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
            f"{self._base_url}/b2b/companies/{brn}/state",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_COMPANY_NOT_FOUND":
                raise errors.B2bCompanyNotFoundError(_deserialize_b2b_company_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_HOMETAX_UNDER_MAINTENANCE":
                raise errors.B2bHometaxUnderMaintenanceError(_deserialize_b2b_hometax_under_maintenance_error(error_response))
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
        return _deserialize_b2b_company_state(response.json())
