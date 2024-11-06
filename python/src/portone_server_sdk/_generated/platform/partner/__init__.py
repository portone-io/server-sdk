from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.platform.partner.archive_platform_partner_response import ArchivePlatformPartnerResponse, _deserialize_archive_platform_partner_response, _serialize_archive_platform_partner_response
from portone_server_sdk._generated.platform.partner.create_platform_partner_body import CreatePlatformPartnerBody, _deserialize_create_platform_partner_body, _serialize_create_platform_partner_body
from portone_server_sdk._generated.platform.partner.create_platform_partner_body_account import CreatePlatformPartnerBodyAccount, _deserialize_create_platform_partner_body_account, _serialize_create_platform_partner_body_account
from portone_server_sdk._generated.platform.partner.create_platform_partner_body_contact import CreatePlatformPartnerBodyContact, _deserialize_create_platform_partner_body_contact, _serialize_create_platform_partner_body_contact
from portone_server_sdk._generated.platform.partner.create_platform_partner_body_type import CreatePlatformPartnerBodyType, _deserialize_create_platform_partner_body_type, _serialize_create_platform_partner_body_type
from portone_server_sdk._generated.platform.partner.create_platform_partner_response import CreatePlatformPartnerResponse, _deserialize_create_platform_partner_response, _serialize_create_platform_partner_response
from portone_server_sdk._generated.platform.partner.create_platform_partners_response import CreatePlatformPartnersResponse, _deserialize_create_platform_partners_response, _serialize_create_platform_partners_response
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.platform.partner.get_platform_partners_response import GetPlatformPartnersResponse, _deserialize_get_platform_partners_response, _serialize_get_platform_partners_response
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from portone_server_sdk._generated.platform.platform_account_verification_already_used_error import PlatformAccountVerificationAlreadyUsedError, _deserialize_platform_account_verification_already_used_error, _serialize_platform_account_verification_already_used_error
from portone_server_sdk._generated.platform.platform_account_verification_failed_error import PlatformAccountVerificationFailedError, _deserialize_platform_account_verification_failed_error, _serialize_platform_account_verification_failed_error
from portone_server_sdk._generated.platform.platform_account_verification_not_found_error import PlatformAccountVerificationNotFoundError, _deserialize_platform_account_verification_not_found_error, _serialize_platform_account_verification_not_found_error
from portone_server_sdk._generated.platform.platform_archived_partner_error import PlatformArchivedPartnerError, _deserialize_platform_archived_partner_error, _serialize_platform_archived_partner_error
from portone_server_sdk._generated.platform.partner.platform_cannot_archive_scheduled_partner_error import PlatformCannotArchiveScheduledPartnerError, _deserialize_platform_cannot_archive_scheduled_partner_error, _serialize_platform_cannot_archive_scheduled_partner_error
from portone_server_sdk._generated.platform.platform_contract_not_found_error import PlatformContractNotFoundError, _deserialize_platform_contract_not_found_error, _serialize_platform_contract_not_found_error
from portone_server_sdk._generated.platform.partner.platform_contracts_not_found_error import PlatformContractsNotFoundError, _deserialize_platform_contracts_not_found_error, _serialize_platform_contracts_not_found_error
from portone_server_sdk._generated.platform.platform_currency_not_supported_error import PlatformCurrencyNotSupportedError, _deserialize_platform_currency_not_supported_error, _serialize_platform_currency_not_supported_error
from portone_server_sdk._generated.platform.platform_insufficient_data_to_change_partner_type_error import PlatformInsufficientDataToChangePartnerTypeError, _deserialize_platform_insufficient_data_to_change_partner_type_error, _serialize_platform_insufficient_data_to_change_partner_type_error
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from portone_server_sdk._generated.platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner
from portone_server_sdk._generated.platform.platform_partner_filter_input import PlatformPartnerFilterInput, _deserialize_platform_partner_filter_input, _serialize_platform_partner_filter_input
from portone_server_sdk._generated.platform.partner.platform_partner_id_already_exists_error import PlatformPartnerIdAlreadyExistsError, _deserialize_platform_partner_id_already_exists_error, _serialize_platform_partner_id_already_exists_error
from portone_server_sdk._generated.platform.partner.platform_partner_ids_already_exist_error import PlatformPartnerIdsAlreadyExistError, _deserialize_platform_partner_ids_already_exist_error, _serialize_platform_partner_ids_already_exist_error
from portone_server_sdk._generated.platform.partner.platform_partner_ids_duplicated_error import PlatformPartnerIdsDuplicatedError, _deserialize_platform_partner_ids_duplicated_error, _serialize_platform_partner_ids_duplicated_error
from portone_server_sdk._generated.platform.platform_partner_not_found_error import PlatformPartnerNotFoundError, _deserialize_platform_partner_not_found_error, _serialize_platform_partner_not_found_error
from portone_server_sdk._generated.platform.platform_properties import PlatformProperties, _deserialize_platform_properties, _serialize_platform_properties
from portone_server_sdk._generated.platform.platform_user_defined_property_not_found_error import PlatformUserDefinedPropertyNotFoundError, _deserialize_platform_user_defined_property_not_found_error, _serialize_platform_user_defined_property_not_found_error
from portone_server_sdk._generated.platform.partner.recover_platform_partner_response import RecoverPlatformPartnerResponse, _deserialize_recover_platform_partner_response, _serialize_recover_platform_partner_response
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from portone_server_sdk._generated.platform.update_platform_partner_body_account import UpdatePlatformPartnerBodyAccount, _deserialize_update_platform_partner_body_account, _serialize_update_platform_partner_body_account
from portone_server_sdk._generated.platform.update_platform_partner_body_contact import UpdatePlatformPartnerBodyContact, _deserialize_update_platform_partner_body_contact, _serialize_update_platform_partner_body_contact
from portone_server_sdk._generated.platform.update_platform_partner_body_type import UpdatePlatformPartnerBodyType, _deserialize_update_platform_partner_body_type, _serialize_update_platform_partner_body_type
from portone_server_sdk._generated.platform.partner.update_platform_partner_response import UpdatePlatformPartnerResponse, _deserialize_update_platform_partner_response, _serialize_update_platform_partner_response
from urllib.parse import quote
from portone_server_sdk._generated import errors
class PartnerClient:
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
    def get_platform_partners(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformPartnerFilterInput] = None,
    ) -> GetPlatformPartnersResponse:
        """파트너 다건 조회

        여러 파트너를 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보
            filter (PlatformPartnerFilterInput, optional):
                조회할 파트너 조건 필터


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_partner_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/partners",
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
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_platform_partners_response(response.json())
    async def get_platform_partners_async(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformPartnerFilterInput] = None,
    ) -> GetPlatformPartnersResponse:
        """파트너 다건 조회

        여러 파트너를 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보
            filter (PlatformPartnerFilterInput, optional):
                조회할 파트너 조건 필터


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_partner_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/partners",
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
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_platform_partners_response(response.json())
    def create_platform_partner(
        self,
        *,
        id: Optional[str] = None,
        name: str,
        contact: CreatePlatformPartnerBodyContact,
        account: CreatePlatformPartnerBodyAccount,
        default_contract_id: str,
        memo: Optional[str] = None,
        tags: list[str],
        type: CreatePlatformPartnerBodyType,
        user_defined_properties: Optional[PlatformProperties] = None,
    ) -> CreatePlatformPartnerResponse:
        """파트너 생성

        새로운 파트너를 생성합니다.

        Args:
            id (str, optional):
                파트너에 부여할 고유 아이디

                고객사 서버에 등록된 파트너 지칭 아이디와 동일하게 설정하는 것을 권장합니다. 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
            name (str):
                파트너 법인명 혹은 이름
            contact (CreatePlatformPartnerBodyContact):
                파트너 담당자 연락 정보
            account (CreatePlatformPartnerBodyAccount):
                정산 계좌

                파트너의 사업자등록번호가 존재하는 경우 명시합니다. 별도로 검증하지는 않으며, 번호와 기호 모두 입력 가능합니다.
            default_contract_id (str):
                기본 계약 아이디

                이미 존재하는 계약 아이디를 등록해야 합니다.
            memo (str, optional):
                파트너에 대한 메모

                총 256자까지 입력할 수 있습니다.
            tags (list[str]):
                파트너에 부여할 태그 리스트

                최대 10개까지 입력할 수 있습니다.
            type (CreatePlatformPartnerBodyType):
                파트너 유형별 추가 정보

                사업자/원천징수 대상자 중 추가할 파트너의 유형에 따른 정보를 입력해야 합니다.
            user_defined_properties (PlatformProperties, optional):
                사용자 정의 속성


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAccountVerificationAlreadyUsedError: 파트너 계좌 검증 아이디를 이미 사용한 경우
                파트너 계좌 검증 아이디를 이미 사용한 경우
            PlatformAccountVerificationFailedError: 파트너 계좌 인증이 실패한 경우
                파트너 계좌 인증이 실패한 경우
            PlatformAccountVerificationNotFoundError: 파트너 계좌 검증 아이디를 찾을 수 없는 경우
                파트너 계좌 검증 아이디를 찾을 수 없는 경우
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformCurrencyNotSupportedError: 지원 되지 않는 통화를 선택한 경우
                지원 되지 않는 통화를 선택한 경우
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerIdAlreadyExistsError: PlatformPartnerIdAlreadyExistsError
            PlatformUserDefinedPropertyNotFoundError: 사용자 정의 속성이 존재 하지 않는 경우
                사용자 정의 속성이 존재 하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if id is not None:
            request_body["id"] = id
        request_body["name"] = name
        request_body["contact"] = _serialize_create_platform_partner_body_contact(contact)
        request_body["account"] = _serialize_create_platform_partner_body_account(account)
        request_body["defaultContractId"] = default_contract_id
        if memo is not None:
            request_body["memo"] = memo
        request_body["tags"] = tags
        request_body["type"] = _serialize_create_platform_partner_body_type(type)
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = _serialize_platform_properties(user_defined_properties)
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/partners",
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
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED":
                raise errors.PlatformAccountVerificationAlreadyUsedError(_deserialize_platform_account_verification_already_used_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_FAILED":
                raise errors.PlatformAccountVerificationFailedError(_deserialize_platform_account_verification_failed_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND":
                raise errors.PlatformAccountVerificationNotFoundError(_deserialize_platform_account_verification_not_found_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_CURRENCY_NOT_SUPPORTED":
                raise errors.PlatformCurrencyNotSupportedError(_deserialize_platform_currency_not_supported_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_ID_ALREADY_EXISTS":
                raise errors.PlatformPartnerIdAlreadyExistsError(_deserialize_platform_partner_id_already_exists_error(error_response))
            if error_type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
                raise errors.PlatformUserDefinedPropertyNotFoundError(_deserialize_platform_user_defined_property_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_create_platform_partner_response(response.json())
    async def create_platform_partner_async(
        self,
        *,
        id: Optional[str] = None,
        name: str,
        contact: CreatePlatformPartnerBodyContact,
        account: CreatePlatformPartnerBodyAccount,
        default_contract_id: str,
        memo: Optional[str] = None,
        tags: list[str],
        type: CreatePlatformPartnerBodyType,
        user_defined_properties: Optional[PlatformProperties] = None,
    ) -> CreatePlatformPartnerResponse:
        """파트너 생성

        새로운 파트너를 생성합니다.

        Args:
            id (str, optional):
                파트너에 부여할 고유 아이디

                고객사 서버에 등록된 파트너 지칭 아이디와 동일하게 설정하는 것을 권장합니다. 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
            name (str):
                파트너 법인명 혹은 이름
            contact (CreatePlatformPartnerBodyContact):
                파트너 담당자 연락 정보
            account (CreatePlatformPartnerBodyAccount):
                정산 계좌

                파트너의 사업자등록번호가 존재하는 경우 명시합니다. 별도로 검증하지는 않으며, 번호와 기호 모두 입력 가능합니다.
            default_contract_id (str):
                기본 계약 아이디

                이미 존재하는 계약 아이디를 등록해야 합니다.
            memo (str, optional):
                파트너에 대한 메모

                총 256자까지 입력할 수 있습니다.
            tags (list[str]):
                파트너에 부여할 태그 리스트

                최대 10개까지 입력할 수 있습니다.
            type (CreatePlatformPartnerBodyType):
                파트너 유형별 추가 정보

                사업자/원천징수 대상자 중 추가할 파트너의 유형에 따른 정보를 입력해야 합니다.
            user_defined_properties (PlatformProperties, optional):
                사용자 정의 속성


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAccountVerificationAlreadyUsedError: 파트너 계좌 검증 아이디를 이미 사용한 경우
                파트너 계좌 검증 아이디를 이미 사용한 경우
            PlatformAccountVerificationFailedError: 파트너 계좌 인증이 실패한 경우
                파트너 계좌 인증이 실패한 경우
            PlatformAccountVerificationNotFoundError: 파트너 계좌 검증 아이디를 찾을 수 없는 경우
                파트너 계좌 검증 아이디를 찾을 수 없는 경우
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformCurrencyNotSupportedError: 지원 되지 않는 통화를 선택한 경우
                지원 되지 않는 통화를 선택한 경우
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerIdAlreadyExistsError: PlatformPartnerIdAlreadyExistsError
            PlatformUserDefinedPropertyNotFoundError: 사용자 정의 속성이 존재 하지 않는 경우
                사용자 정의 속성이 존재 하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if id is not None:
            request_body["id"] = id
        request_body["name"] = name
        request_body["contact"] = _serialize_create_platform_partner_body_contact(contact)
        request_body["account"] = _serialize_create_platform_partner_body_account(account)
        request_body["defaultContractId"] = default_contract_id
        if memo is not None:
            request_body["memo"] = memo
        request_body["tags"] = tags
        request_body["type"] = _serialize_create_platform_partner_body_type(type)
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = _serialize_platform_properties(user_defined_properties)
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/partners",
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
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED":
                raise errors.PlatformAccountVerificationAlreadyUsedError(_deserialize_platform_account_verification_already_used_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_FAILED":
                raise errors.PlatformAccountVerificationFailedError(_deserialize_platform_account_verification_failed_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND":
                raise errors.PlatformAccountVerificationNotFoundError(_deserialize_platform_account_verification_not_found_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_CURRENCY_NOT_SUPPORTED":
                raise errors.PlatformCurrencyNotSupportedError(_deserialize_platform_currency_not_supported_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_ID_ALREADY_EXISTS":
                raise errors.PlatformPartnerIdAlreadyExistsError(_deserialize_platform_partner_id_already_exists_error(error_response))
            if error_type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
                raise errors.PlatformUserDefinedPropertyNotFoundError(_deserialize_platform_user_defined_property_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_create_platform_partner_response(response.json())
    def get_platform_partner(
        self,
        *,
        id: str,
    ) -> PlatformPartner:
        """파트너 조회

        파트너 객체를 조회합니다.

        Args:
            id (str):
                조회하고 싶은 파트너 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}",
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
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_platform_partner(response.json())
    async def get_platform_partner_async(
        self,
        *,
        id: str,
    ) -> PlatformPartner:
        """파트너 조회

        파트너 객체를 조회합니다.

        Args:
            id (str):
                조회하고 싶은 파트너 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}",
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
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_platform_partner(response.json())
    def update_platform_partner(
        self,
        *,
        id: str,
        name: Optional[str] = None,
        contact: Optional[UpdatePlatformPartnerBodyContact] = None,
        account: Optional[UpdatePlatformPartnerBodyAccount] = None,
        default_contract_id: Optional[str] = None,
        memo: Optional[str] = None,
        tags: Optional[list[str]] = None,
        type: Optional[UpdatePlatformPartnerBodyType] = None,
        user_defined_properties: Optional[PlatformProperties] = None,
    ) -> UpdatePlatformPartnerResponse:
        """파트너 수정

        주어진 아이디에 대응되는 파트너 정보를 업데이트합니다.

        Args:
            id (str):
                업데이트할 파트너 아이디
            name (str, optional):
                파트너 법인명 혹은 이름
            contact (UpdatePlatformPartnerBodyContact, optional):
                파트너 담당자 연락 정보
            account (UpdatePlatformPartnerBodyAccount, optional):
                정산 계좌
            default_contract_id (str, optional):
                파트너에 설정된 기본 계약 아이디
            memo (str, optional):
                파트너에 대한 메모
            tags (list[str], optional):
                파트너의 태그 리스트
            type (UpdatePlatformPartnerBodyType, optional):
                파트너 유형별 정보
            user_defined_properties (PlatformProperties, optional):
                사용자 정의 속성


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAccountVerificationAlreadyUsedError: 파트너 계좌 검증 아이디를 이미 사용한 경우
                파트너 계좌 검증 아이디를 이미 사용한 경우
            PlatformAccountVerificationFailedError: 파트너 계좌 인증이 실패한 경우
                파트너 계좌 인증이 실패한 경우
            PlatformAccountVerificationNotFoundError: 파트너 계좌 검증 아이디를 찾을 수 없는 경우
                파트너 계좌 검증 아이디를 찾을 수 없는 경우
            PlatformArchivedPartnerError: 보관된 파트너를 업데이트하려고 하는 경우
                보관된 파트너를 업데이트하려고 하는 경우
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformInsufficientDataToChangePartnerTypeError: 파트너 타입 수정에 필요한 데이터가 부족한 경우
                파트너 타입 수정에 필요한 데이터가 부족한 경우
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            PlatformUserDefinedPropertyNotFoundError: 사용자 정의 속성이 존재 하지 않는 경우
                사용자 정의 속성이 존재 하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if name is not None:
            request_body["name"] = name
        if contact is not None:
            request_body["contact"] = _serialize_update_platform_partner_body_contact(contact)
        if account is not None:
            request_body["account"] = _serialize_update_platform_partner_body_account(account)
        if default_contract_id is not None:
            request_body["defaultContractId"] = default_contract_id
        if memo is not None:
            request_body["memo"] = memo
        if tags is not None:
            request_body["tags"] = tags
        if type is not None:
            request_body["type"] = _serialize_update_platform_partner_body_type(type)
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = _serialize_platform_properties(user_defined_properties)
        query = []
        response = httpx.request(
            "PATCH",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}",
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
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED":
                raise errors.PlatformAccountVerificationAlreadyUsedError(_deserialize_platform_account_verification_already_used_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_FAILED":
                raise errors.PlatformAccountVerificationFailedError(_deserialize_platform_account_verification_failed_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND":
                raise errors.PlatformAccountVerificationNotFoundError(_deserialize_platform_account_verification_not_found_error(error_response))
            if error_type == "PLATFORM_ARCHIVED_PARTNER":
                raise errors.PlatformArchivedPartnerError(_deserialize_platform_archived_partner_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_INSUFFICIENT_DATA_TO_CHANGE_PARTNER_TYPE":
                raise errors.PlatformInsufficientDataToChangePartnerTypeError(_deserialize_platform_insufficient_data_to_change_partner_type_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
                raise errors.PlatformUserDefinedPropertyNotFoundError(_deserialize_platform_user_defined_property_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_update_platform_partner_response(response.json())
    async def update_platform_partner_async(
        self,
        *,
        id: str,
        name: Optional[str] = None,
        contact: Optional[UpdatePlatformPartnerBodyContact] = None,
        account: Optional[UpdatePlatformPartnerBodyAccount] = None,
        default_contract_id: Optional[str] = None,
        memo: Optional[str] = None,
        tags: Optional[list[str]] = None,
        type: Optional[UpdatePlatformPartnerBodyType] = None,
        user_defined_properties: Optional[PlatformProperties] = None,
    ) -> UpdatePlatformPartnerResponse:
        """파트너 수정

        주어진 아이디에 대응되는 파트너 정보를 업데이트합니다.

        Args:
            id (str):
                업데이트할 파트너 아이디
            name (str, optional):
                파트너 법인명 혹은 이름
            contact (UpdatePlatformPartnerBodyContact, optional):
                파트너 담당자 연락 정보
            account (UpdatePlatformPartnerBodyAccount, optional):
                정산 계좌
            default_contract_id (str, optional):
                파트너에 설정된 기본 계약 아이디
            memo (str, optional):
                파트너에 대한 메모
            tags (list[str], optional):
                파트너의 태그 리스트
            type (UpdatePlatformPartnerBodyType, optional):
                파트너 유형별 정보
            user_defined_properties (PlatformProperties, optional):
                사용자 정의 속성


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformAccountVerificationAlreadyUsedError: 파트너 계좌 검증 아이디를 이미 사용한 경우
                파트너 계좌 검증 아이디를 이미 사용한 경우
            PlatformAccountVerificationFailedError: 파트너 계좌 인증이 실패한 경우
                파트너 계좌 인증이 실패한 경우
            PlatformAccountVerificationNotFoundError: 파트너 계좌 검증 아이디를 찾을 수 없는 경우
                파트너 계좌 검증 아이디를 찾을 수 없는 경우
            PlatformArchivedPartnerError: 보관된 파트너를 업데이트하려고 하는 경우
                보관된 파트너를 업데이트하려고 하는 경우
            PlatformContractNotFoundError: PlatformContractNotFoundError
            PlatformInsufficientDataToChangePartnerTypeError: 파트너 타입 수정에 필요한 데이터가 부족한 경우
                파트너 타입 수정에 필요한 데이터가 부족한 경우
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            PlatformUserDefinedPropertyNotFoundError: 사용자 정의 속성이 존재 하지 않는 경우
                사용자 정의 속성이 존재 하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if name is not None:
            request_body["name"] = name
        if contact is not None:
            request_body["contact"] = _serialize_update_platform_partner_body_contact(contact)
        if account is not None:
            request_body["account"] = _serialize_update_platform_partner_body_account(account)
        if default_contract_id is not None:
            request_body["defaultContractId"] = default_contract_id
        if memo is not None:
            request_body["memo"] = memo
        if tags is not None:
            request_body["tags"] = tags
        if type is not None:
            request_body["type"] = _serialize_update_platform_partner_body_type(type)
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = _serialize_platform_properties(user_defined_properties)
        query = []
        response = await self._client.request(
            "PATCH",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}",
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
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED":
                raise errors.PlatformAccountVerificationAlreadyUsedError(_deserialize_platform_account_verification_already_used_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_FAILED":
                raise errors.PlatformAccountVerificationFailedError(_deserialize_platform_account_verification_failed_error(error_response))
            if error_type == "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND":
                raise errors.PlatformAccountVerificationNotFoundError(_deserialize_platform_account_verification_not_found_error(error_response))
            if error_type == "PLATFORM_ARCHIVED_PARTNER":
                raise errors.PlatformArchivedPartnerError(_deserialize_platform_archived_partner_error(error_response))
            if error_type == "PLATFORM_CONTRACT_NOT_FOUND":
                raise errors.PlatformContractNotFoundError(_deserialize_platform_contract_not_found_error(error_response))
            if error_type == "PLATFORM_INSUFFICIENT_DATA_TO_CHANGE_PARTNER_TYPE":
                raise errors.PlatformInsufficientDataToChangePartnerTypeError(_deserialize_platform_insufficient_data_to_change_partner_type_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
                raise errors.PlatformUserDefinedPropertyNotFoundError(_deserialize_platform_user_defined_property_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_update_platform_partner_response(response.json())
    def create_platform_partners(
        self,
        *,
        partners: list[CreatePlatformPartnerBody],
    ) -> CreatePlatformPartnersResponse:
        """파트너 다건 생성

        새로운 파트너를 다건 생성합니다.

        Args:
            partners (list[CreatePlatformPartnerBody]):
                생성할 파트너 리스트 정보


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformContractsNotFoundError: PlatformContractsNotFoundError
            PlatformCurrencyNotSupportedError: 지원 되지 않는 통화를 선택한 경우
                지원 되지 않는 통화를 선택한 경우
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerIdsAlreadyExistError: PlatformPartnerIdsAlreadyExistError
            PlatformPartnerIdsDuplicatedError: PlatformPartnerIdsDuplicatedError
            PlatformUserDefinedPropertyNotFoundError: 사용자 정의 속성이 존재 하지 않는 경우
                사용자 정의 속성이 존재 하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["partners"] = partners
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/partners/batch",
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
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_CONTRACTS_NOT_FOUND":
                raise errors.PlatformContractsNotFoundError(_deserialize_platform_contracts_not_found_error(error_response))
            if error_type == "PLATFORM_CURRENCY_NOT_SUPPORTED":
                raise errors.PlatformCurrencyNotSupportedError(_deserialize_platform_currency_not_supported_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_IDS_ALREADY_EXISTS":
                raise errors.PlatformPartnerIdsAlreadyExistError(_deserialize_platform_partner_ids_already_exist_error(error_response))
            if error_type == "PLATFORM_PARTNER_IDS_DUPLICATED":
                raise errors.PlatformPartnerIdsDuplicatedError(_deserialize_platform_partner_ids_duplicated_error(error_response))
            if error_type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
                raise errors.PlatformUserDefinedPropertyNotFoundError(_deserialize_platform_user_defined_property_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_create_platform_partners_response(response.json())
    async def create_platform_partners_async(
        self,
        *,
        partners: list[CreatePlatformPartnerBody],
    ) -> CreatePlatformPartnersResponse:
        """파트너 다건 생성

        새로운 파트너를 다건 생성합니다.

        Args:
            partners (list[CreatePlatformPartnerBody]):
                생성할 파트너 리스트 정보


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformContractsNotFoundError: PlatformContractsNotFoundError
            PlatformCurrencyNotSupportedError: 지원 되지 않는 통화를 선택한 경우
                지원 되지 않는 통화를 선택한 경우
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerIdsAlreadyExistError: PlatformPartnerIdsAlreadyExistError
            PlatformPartnerIdsDuplicatedError: PlatformPartnerIdsDuplicatedError
            PlatformUserDefinedPropertyNotFoundError: 사용자 정의 속성이 존재 하지 않는 경우
                사용자 정의 속성이 존재 하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["partners"] = partners
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/partners/batch",
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
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PLATFORM_CONTRACTS_NOT_FOUND":
                raise errors.PlatformContractsNotFoundError(_deserialize_platform_contracts_not_found_error(error_response))
            if error_type == "PLATFORM_CURRENCY_NOT_SUPPORTED":
                raise errors.PlatformCurrencyNotSupportedError(_deserialize_platform_currency_not_supported_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_IDS_ALREADY_EXISTS":
                raise errors.PlatformPartnerIdsAlreadyExistError(_deserialize_platform_partner_ids_already_exist_error(error_response))
            if error_type == "PLATFORM_PARTNER_IDS_DUPLICATED":
                raise errors.PlatformPartnerIdsDuplicatedError(_deserialize_platform_partner_ids_duplicated_error(error_response))
            if error_type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
                raise errors.PlatformUserDefinedPropertyNotFoundError(_deserialize_platform_user_defined_property_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_create_platform_partners_response(response.json())
    def archive_platform_partner(
        self,
        *,
        id: str,
    ) -> ArchivePlatformPartnerResponse:
        """파트너 복원

        주어진 아이디에 대응되는 파트너를 보관합니다.

        Args:
            id (str):
                파트너 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformCannotArchiveScheduledPartnerError: 예약된 업데이트가 있는 파트너를 보관하려고 하는 경우
                예약된 업데이트가 있는 파트너를 보관하려고 하는 경우
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/archive",
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
            if error_type == "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER":
                raise errors.PlatformCannotArchiveScheduledPartnerError(_deserialize_platform_cannot_archive_scheduled_partner_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_archive_platform_partner_response(response.json())
    async def archive_platform_partner_async(
        self,
        *,
        id: str,
    ) -> ArchivePlatformPartnerResponse:
        """파트너 복원

        주어진 아이디에 대응되는 파트너를 보관합니다.

        Args:
            id (str):
                파트너 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformCannotArchiveScheduledPartnerError: 예약된 업데이트가 있는 파트너를 보관하려고 하는 경우
                예약된 업데이트가 있는 파트너를 보관하려고 하는 경우
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/archive",
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
            if error_type == "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER":
                raise errors.PlatformCannotArchiveScheduledPartnerError(_deserialize_platform_cannot_archive_scheduled_partner_error(error_response))
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_archive_platform_partner_response(response.json())
    def recover_platform_partner(
        self,
        *,
        id: str,
    ) -> RecoverPlatformPartnerResponse:
        """파트너 복원

        주어진 아이디에 대응되는 파트너를 복원합니다.

        Args:
            id (str):
                파트너 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/recover",
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
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_recover_platform_partner_response(response.json())
    async def recover_platform_partner_async(
        self,
        *,
        id: str,
    ) -> RecoverPlatformPartnerResponse:
        """파트너 복원

        주어진 아이디에 대응되는 파트너를 복원합니다.

        Args:
            id (str):
                파트너 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PlatformNotEnabledError: 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
                플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
            PlatformPartnerNotFoundError: PlatformPartnerNotFoundError
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/recover",
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
            if error_type == "PLATFORM_NOT_ENABLED":
                raise errors.PlatformNotEnabledError(_deserialize_platform_not_enabled_error(error_response))
            if error_type == "PLATFORM_PARTNER_NOT_FOUND":
                raise errors.PlatformPartnerNotFoundError(_deserialize_platform_partner_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_recover_platform_partner_response(response.json())
