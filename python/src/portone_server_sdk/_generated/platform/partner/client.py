from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import ForbiddenError, InvalidRequestError, PlatformAccountVerificationAlreadyUsedError, PlatformAccountVerificationFailedError, PlatformAccountVerificationNotFoundError, PlatformArchivedPartnerError, PlatformCannotArchiveScheduledPartnerError, PlatformCompanyVerificationAlreadyUsedError, PlatformContractNotFoundError, PlatformContractsNotFoundError, PlatformCurrencyNotSupportedError, PlatformInsufficientDataToChangePartnerTypeError, PlatformMemberCompanyConnectedPartnerBrnUnchangeableError, PlatformMemberCompanyConnectedPartnerTypeUnchangeableError, PlatformNotEnabledError, PlatformPartnerIdAlreadyExistsError, PlatformPartnerIdsAlreadyExistError, PlatformPartnerIdsDuplicatedError, PlatformPartnerNotFoundError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError, UnknownError
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...platform.platform_account_verification_already_used_error import _deserialize_platform_account_verification_already_used_error
from ...platform.platform_account_verification_failed_error import _deserialize_platform_account_verification_failed_error
from ...platform.platform_account_verification_not_found_error import _deserialize_platform_account_verification_not_found_error
from ...platform.platform_archived_partner_error import _deserialize_platform_archived_partner_error
from ...platform.partner.platform_cannot_archive_scheduled_partner_error import _deserialize_platform_cannot_archive_scheduled_partner_error
from ...platform.platform_company_verification_already_used_error import _deserialize_platform_company_verification_already_used_error
from ...platform.platform_contract_not_found_error import _deserialize_platform_contract_not_found_error
from ...platform.partner.platform_contracts_not_found_error import _deserialize_platform_contracts_not_found_error
from ...platform.platform_currency_not_supported_error import _deserialize_platform_currency_not_supported_error
from ...platform.platform_insufficient_data_to_change_partner_type_error import _deserialize_platform_insufficient_data_to_change_partner_type_error
from ...platform.platform_member_company_connected_partner_brn_unchangeable_error import _deserialize_platform_member_company_connected_partner_brn_unchangeable_error
from ...platform.platform_member_company_connected_partner_type_unchangeable_error import _deserialize_platform_member_company_connected_partner_type_unchangeable_error
from ...platform.platform_not_enabled_error import _deserialize_platform_not_enabled_error
from ...platform.partner.platform_partner_id_already_exists_error import _deserialize_platform_partner_id_already_exists_error
from ...platform.partner.platform_partner_ids_already_exist_error import _deserialize_platform_partner_ids_already_exist_error
from ...platform.partner.platform_partner_ids_duplicated_error import _deserialize_platform_partner_ids_duplicated_error
from ...platform.platform_partner_not_found_error import _deserialize_platform_partner_not_found_error
from ...platform.platform_user_defined_property_not_found_error import _deserialize_platform_user_defined_property_not_found_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...platform.partner.archive_platform_partner_response import ArchivePlatformPartnerResponse, _deserialize_archive_platform_partner_response, _serialize_archive_platform_partner_response
from ...platform.partner.create_platform_partner_body import CreatePlatformPartnerBody, _deserialize_create_platform_partner_body, _serialize_create_platform_partner_body
from ...platform.partner.create_platform_partner_body_account import CreatePlatformPartnerBodyAccount, _deserialize_create_platform_partner_body_account, _serialize_create_platform_partner_body_account
from ...platform.partner.create_platform_partner_body_contact import CreatePlatformPartnerBodyContact, _deserialize_create_platform_partner_body_contact, _serialize_create_platform_partner_body_contact
from ...platform.partner.create_platform_partner_body_type import CreatePlatformPartnerBodyType, _deserialize_create_platform_partner_body_type, _serialize_create_platform_partner_body_type
from ...platform.partner.create_platform_partner_response import CreatePlatformPartnerResponse, _deserialize_create_platform_partner_response, _serialize_create_platform_partner_response
from ...platform.partner.create_platform_partners_response import CreatePlatformPartnersResponse, _deserialize_create_platform_partners_response, _serialize_create_platform_partners_response
from ...platform.partner.get_platform_partners_response import GetPlatformPartnersResponse, _deserialize_get_platform_partners_response, _serialize_get_platform_partners_response
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner
from ...platform.platform_partner_filter_input import PlatformPartnerFilterInput, _deserialize_platform_partner_filter_input, _serialize_platform_partner_filter_input
from ...platform.platform_properties import PlatformProperties, _deserialize_platform_properties, _serialize_platform_properties
from ...platform.partner.recover_platform_partner_response import RecoverPlatformPartnerResponse, _deserialize_recover_platform_partner_response, _serialize_recover_platform_partner_response
from ...platform.update_platform_partner_body_account import UpdatePlatformPartnerBodyAccount, _deserialize_update_platform_partner_body_account, _serialize_update_platform_partner_body_account
from ...platform.update_platform_partner_body_contact import UpdatePlatformPartnerBodyContact, _deserialize_update_platform_partner_body_contact, _serialize_update_platform_partner_body_contact
from ...platform.update_platform_partner_body_type import UpdatePlatformPartnerBodyType, _deserialize_update_platform_partner_body_type, _serialize_update_platform_partner_body_type
from ...platform.partner.update_platform_partner_response import UpdatePlatformPartnerResponse, _deserialize_update_platform_partner_response, _serialize_update_platform_partner_response
from urllib.parse import quote
class PartnerClient:
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
            GetPlatformPartnersError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
            GetPlatformPartnersError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
            CreatePlatformPartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_account_verification_already_used_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationAlreadyUsedError(error)
            try:
                error = _deserialize_platform_account_verification_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationFailedError(error)
            try:
                error = _deserialize_platform_account_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationNotFoundError(error)
            try:
                error = _deserialize_platform_company_verification_already_used_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCompanyVerificationAlreadyUsedError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_currency_not_supported_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCurrencyNotSupportedError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_id_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerIdAlreadyExistsError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            CreatePlatformPartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_account_verification_already_used_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationAlreadyUsedError(error)
            try:
                error = _deserialize_platform_account_verification_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationFailedError(error)
            try:
                error = _deserialize_platform_account_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationNotFoundError(error)
            try:
                error = _deserialize_platform_company_verification_already_used_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCompanyVerificationAlreadyUsedError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_currency_not_supported_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCurrencyNotSupportedError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_id_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerIdAlreadyExistsError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            GetPlatformPartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}",
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
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            GetPlatformPartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}",
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
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            UpdatePlatformPartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_account_verification_already_used_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationAlreadyUsedError(error)
            try:
                error = _deserialize_platform_account_verification_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationFailedError(error)
            try:
                error = _deserialize_platform_account_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationNotFoundError(error)
            try:
                error = _deserialize_platform_archived_partner_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformArchivedPartnerError(error)
            try:
                error = _deserialize_platform_company_verification_already_used_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCompanyVerificationAlreadyUsedError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_insufficient_data_to_change_partner_type_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformInsufficientDataToChangePartnerTypeError(error)
            try:
                error = _deserialize_platform_member_company_connected_partner_brn_unchangeable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnerBrnUnchangeableError(error)
            try:
                error = _deserialize_platform_member_company_connected_partner_type_unchangeable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnerTypeUnchangeableError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            UpdatePlatformPartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_account_verification_already_used_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationAlreadyUsedError(error)
            try:
                error = _deserialize_platform_account_verification_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationFailedError(error)
            try:
                error = _deserialize_platform_account_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAccountVerificationNotFoundError(error)
            try:
                error = _deserialize_platform_archived_partner_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformArchivedPartnerError(error)
            try:
                error = _deserialize_platform_company_verification_already_used_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCompanyVerificationAlreadyUsedError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_insufficient_data_to_change_partner_type_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformInsufficientDataToChangePartnerTypeError(error)
            try:
                error = _deserialize_platform_member_company_connected_partner_brn_unchangeable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnerBrnUnchangeableError(error)
            try:
                error = _deserialize_platform_member_company_connected_partner_type_unchangeable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformMemberCompanyConnectedPartnerTypeUnchangeableError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            CreatePlatformPartnersError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_contracts_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractsNotFoundError(error)
            try:
                error = _deserialize_platform_currency_not_supported_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCurrencyNotSupportedError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_ids_already_exist_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerIdsAlreadyExistError(error)
            try:
                error = _deserialize_platform_partner_ids_duplicated_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerIdsDuplicatedError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            CreatePlatformPartnersError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_platform_contracts_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractsNotFoundError(error)
            try:
                error = _deserialize_platform_currency_not_supported_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCurrencyNotSupportedError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_ids_already_exist_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerIdsAlreadyExistError(error)
            try:
                error = _deserialize_platform_partner_ids_duplicated_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerIdsDuplicatedError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            ArchivePlatformPartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/archive",
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
                error = _deserialize_platform_cannot_archive_scheduled_partner_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCannotArchiveScheduledPartnerError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            ArchivePlatformPartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/archive",
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
                error = _deserialize_platform_cannot_archive_scheduled_partner_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCannotArchiveScheduledPartnerError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            RecoverPlatformPartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/recover",
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
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            RecoverPlatformPartnerError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/partners/{quote(id, safe='')}/recover",
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
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_recover_platform_partner_response(response.json())
