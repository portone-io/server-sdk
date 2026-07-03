from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import B2bCertificateUnregisteredError, B2bCounterpartyBrnInvalidError, B2bCounterpartyBrnModificationNotAllowedError, B2bCounterpartyIdAlreadyExistsByPartnerError, B2bCounterpartyIdAlreadyExistsError, B2bCounterpartyMissingRequiredFieldsError, B2bCounterpartyNotFoundError, B2bCounterpartyNtsConnectionFailedError, B2bCounterpartyNtsNotConnectedError, B2bCounterpartyOngoingTaxInvoiceExistsError, B2bCounterpartyPartnerNotConnectableError, B2bCounterpartyPartnerNotDeletableError, B2bCounterpartyPartnerNotUpdatableError, B2bCounterpartySelfOriginBrnMismatchError, B2bCounterpartyTooManyAdditionalContactsError, B2bCounterpartyVerificationBrnMismatchError, B2bCounterpartyVerificationInvalidError, B2bCounterpartyVerificationNotFoundError, B2bCounterpartyVerificationTypeMismatchError, B2bExternalServiceError, B2bNotEnabledError, ForbiddenError, InvalidRequestError, UnauthorizedError, UnknownError
from ...b2b.counterparty.b2b_certificate_unregistered_error import _deserialize_b2b_certificate_unregistered_error
from ...b2b.counterparty.b2b_counterparty_brn_invalid_error import _deserialize_b2b_counterparty_brn_invalid_error
from ...b2b.counterparty.b2b_counterparty_brn_modification_not_allowed_error import _deserialize_b2b_counterparty_brn_modification_not_allowed_error
from ...b2b.counterparty.b2b_counterparty_id_already_exists_by_partner_error import _deserialize_b2b_counterparty_id_already_exists_by_partner_error
from ...b2b.counterparty.b2b_counterparty_id_already_exists_error import _deserialize_b2b_counterparty_id_already_exists_error
from ...b2b.counterparty.b2b_counterparty_missing_required_fields_error import _deserialize_b2b_counterparty_missing_required_fields_error
from ...common.b2b_counterparty_not_found_error import _deserialize_b2b_counterparty_not_found_error
from ...b2b.counterparty.b2b_counterparty_nts_connection_failed_error import _deserialize_b2b_counterparty_nts_connection_failed_error
from ...common.b2b_counterparty_nts_not_connected_error import _deserialize_b2b_counterparty_nts_not_connected_error
from ...b2b.counterparty.b2b_counterparty_ongoing_tax_invoice_exists_error import _deserialize_b2b_counterparty_ongoing_tax_invoice_exists_error
from ...b2b.counterparty.b2b_counterparty_partner_not_connectable_error import _deserialize_b2b_counterparty_partner_not_connectable_error
from ...b2b.counterparty.b2b_counterparty_partner_not_deletable_error import _deserialize_b2b_counterparty_partner_not_deletable_error
from ...b2b.counterparty.b2b_counterparty_partner_not_updatable_error import _deserialize_b2b_counterparty_partner_not_updatable_error
from ...b2b.counterparty.b2b_counterparty_self_origin_brn_mismatch_error import _deserialize_b2b_counterparty_self_origin_brn_mismatch_error
from ...b2b.counterparty.b2b_counterparty_too_many_additional_contacts_error import _deserialize_b2b_counterparty_too_many_additional_contacts_error
from ...b2b.counterparty.b2b_counterparty_verification_brn_mismatch_error import _deserialize_b2b_counterparty_verification_brn_mismatch_error
from ...b2b.counterparty.b2b_counterparty_verification_invalid_error import _deserialize_b2b_counterparty_verification_invalid_error
from ...b2b.counterparty.b2b_counterparty_verification_not_found_error import _deserialize_b2b_counterparty_verification_not_found_error
from ...b2b.counterparty.b2b_counterparty_verification_type_mismatch_error import _deserialize_b2b_counterparty_verification_type_mismatch_error
from ...common.b2b_external_service_error import _deserialize_b2b_external_service_error
from ...common.b2b_not_enabled_error import _deserialize_b2b_not_enabled_error
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...b2b.counterparty.b2b_certificate import B2bCertificate, _deserialize_b2b_certificate, _serialize_b2b_certificate
from ...b2b.counterparty.b2b_counterparty import B2bCounterparty, _deserialize_b2b_counterparty, _serialize_b2b_counterparty
from ...b2b.counterparty.b2b_counterparty_create_options import B2bCounterpartyCreateOptions, _deserialize_b2b_counterparty_create_options, _serialize_b2b_counterparty_create_options
from ...b2b.counterparty.b2b_counterparty_filter import B2bCounterpartyFilter, _deserialize_b2b_counterparty_filter, _serialize_b2b_counterparty_filter
from ...b2b.counterparty.b2b_counterparty_input import B2bCounterpartyInput, _deserialize_b2b_counterparty_input, _serialize_b2b_counterparty_input
from ...b2b.counterparty.create_b2b_counterparty_response import CreateB2bCounterpartyResponse, _deserialize_create_b2b_counterparty_response, _serialize_create_b2b_counterparty_response
from ...b2b.counterparty.delete_b2b_counterparty_response import DeleteB2bCounterpartyResponse, _deserialize_delete_b2b_counterparty_response, _serialize_delete_b2b_counterparty_response
from ...b2b.counterparty.get_b2b_counterparties_response import GetB2bCounterpartiesResponse, _deserialize_get_b2b_counterparties_response, _serialize_get_b2b_counterparties_response
from ...b2b.counterparty.get_b2b_counterparty_certificate_registration_url_response import GetB2bCounterpartyCertificateRegistrationUrlResponse, _deserialize_get_b2b_counterparty_certificate_registration_url_response, _serialize_get_b2b_counterparty_certificate_registration_url_response
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...b2b.counterparty.update_b2b_counterparty_response import UpdateB2bCounterpartyResponse, _deserialize_update_b2b_counterparty_response, _serialize_update_b2b_counterparty_response
from ...b2b.counterparty.validate_b2b_counterparty_certificate_response import ValidateB2bCounterpartyCertificateResponse, _deserialize_validate_b2b_counterparty_certificate_response, _serialize_validate_b2b_counterparty_certificate_response
from urllib.parse import quote
class CounterpartyClient:
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
    def get_b2b_counterparty_certificate_registration_url(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> GetB2bCounterpartyCertificateRegistrationUrlResponse:
        """사업자 인증서 등록 URL 조회

        연동 사업자의 인증서를 등록하기 위한 URL을 조회합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            GetB2bCounterpartyCertificateRegistrationUrlError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/b2b/counterparties/{quote(brn, safe='')}/certificate/registration-url",
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
                error = _deserialize_b2b_counterparty_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_nts_not_connected_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNtsNotConnectedError(error)
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
        return _deserialize_get_b2b_counterparty_certificate_registration_url_response(response.json())
    async def get_b2b_counterparty_certificate_registration_url_async(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> GetB2bCounterpartyCertificateRegistrationUrlResponse:
        """사업자 인증서 등록 URL 조회

        연동 사업자의 인증서를 등록하기 위한 URL을 조회합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            GetB2bCounterpartyCertificateRegistrationUrlError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/b2b/counterparties/{quote(brn, safe='')}/certificate/registration-url",
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
                error = _deserialize_b2b_counterparty_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_nts_not_connected_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNtsNotConnectedError(error)
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
        return _deserialize_get_b2b_counterparty_certificate_registration_url_response(response.json())
    def validate_b2b_counterparty_certificate(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> ValidateB2bCounterpartyCertificateResponse:
        """사업자 인증서 유효성 검증

        연동 사업자가 등록한 인증서의 유효성을 검증합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            ValidateB2bCounterpartyCertificateError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
            "POST",
            f"{self._base_url}/b2b/counterparties/{quote(brn, safe='')}/certificate/validate",
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
                error = _deserialize_b2b_certificate_unregistered_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCertificateUnregisteredError(error)
            try:
                error = _deserialize_b2b_counterparty_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_nts_not_connected_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNtsNotConnectedError(error)
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
        return _deserialize_validate_b2b_counterparty_certificate_response(response.json())
    async def validate_b2b_counterparty_certificate_async(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
    ) -> ValidateB2bCounterpartyCertificateResponse:
        """사업자 인증서 유효성 검증

        연동 사업자가 등록한 인증서의 유효성을 검증합니다.

        Args:
            brn (str):
                사업자등록번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            ValidateB2bCounterpartyCertificateError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
            "POST",
            f"{self._base_url}/b2b/counterparties/{quote(brn, safe='')}/certificate/validate",
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
                error = _deserialize_b2b_certificate_unregistered_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCertificateUnregisteredError(error)
            try:
                error = _deserialize_b2b_counterparty_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_nts_not_connected_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNtsNotConnectedError(error)
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
        return _deserialize_validate_b2b_counterparty_certificate_response(response.json())
    def get_b2b_counterparty_certificate(
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
            GetB2bCounterpartyCertificateError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/b2b/counterparties/{quote(brn, safe='')}/certificate",
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
                error = _deserialize_b2b_certificate_unregistered_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCertificateUnregisteredError(error)
            try:
                error = _deserialize_b2b_counterparty_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_nts_not_connected_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNtsNotConnectedError(error)
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
        return _deserialize_b2b_certificate(response.json())
    async def get_b2b_counterparty_certificate_async(
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
            GetB2bCounterpartyCertificateError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/b2b/counterparties/{quote(brn, safe='')}/certificate",
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
                error = _deserialize_b2b_certificate_unregistered_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCertificateUnregisteredError(error)
            try:
                error = _deserialize_b2b_counterparty_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_nts_not_connected_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNtsNotConnectedError(error)
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
        return _deserialize_b2b_certificate(response.json())
    def get_b2b_counterparty(
        self,
        *,
        counterparty_id: str,
        test: Optional[bool] = None,
    ) -> B2bCounterparty:
        """거래처 조회

        거래처를 조회합니다.

        Args:
            counterparty_id (str):
                거래처 ID
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            GetB2bCounterpartyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/b2b/counterparties/{quote(counterparty_id, safe='')}",
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
                error = _deserialize_b2b_counterparty_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNotFoundError(error)
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
        return _deserialize_b2b_counterparty(response.json())
    async def get_b2b_counterparty_async(
        self,
        *,
        counterparty_id: str,
        test: Optional[bool] = None,
    ) -> B2bCounterparty:
        """거래처 조회

        거래처를 조회합니다.

        Args:
            counterparty_id (str):
                거래처 ID
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            GetB2bCounterpartyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/b2b/counterparties/{quote(counterparty_id, safe='')}",
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
                error = _deserialize_b2b_counterparty_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNotFoundError(error)
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
        return _deserialize_b2b_counterparty(response.json())
    def delete_b2b_counterparty(
        self,
        *,
        counterparty_id: str,
        test: Optional[bool] = None,
    ) -> DeleteB2bCounterpartyResponse:
        """거래처 삭제

        거래처를 삭제합니다.

        Args:
            counterparty_id (str):
                거래처 ID
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            DeleteB2bCounterpartyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
            "DELETE",
            f"{self._base_url}/b2b/counterparties/{quote(counterparty_id, safe='')}",
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
                error = _deserialize_b2b_counterparty_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_ongoing_tax_invoice_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyOngoingTaxInvoiceExistsError(error)
            try:
                error = _deserialize_b2b_counterparty_partner_not_deletable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyPartnerNotDeletableError(error)
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
        return _deserialize_delete_b2b_counterparty_response(response.json())
    async def delete_b2b_counterparty_async(
        self,
        *,
        counterparty_id: str,
        test: Optional[bool] = None,
    ) -> DeleteB2bCounterpartyResponse:
        """거래처 삭제

        거래처를 삭제합니다.

        Args:
            counterparty_id (str):
                거래처 ID
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            DeleteB2bCounterpartyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
            "DELETE",
            f"{self._base_url}/b2b/counterparties/{quote(counterparty_id, safe='')}",
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
                error = _deserialize_b2b_counterparty_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_ongoing_tax_invoice_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyOngoingTaxInvoiceExistsError(error)
            try:
                error = _deserialize_b2b_counterparty_partner_not_deletable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyPartnerNotDeletableError(error)
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
        return _deserialize_delete_b2b_counterparty_response(response.json())
    def update_b2b_counterparty(
        self,
        *,
        counterparty_id: str,
        test: Optional[bool] = None,
        counterparty: B2bCounterpartyInput,
        options: Optional[B2bCounterpartyCreateOptions] = None,
    ) -> UpdateB2bCounterpartyResponse:
        """거래처 정보 수정

        거래처 정보를 수정합니다.

        Args:
            counterparty_id (str):
                거래처 ID
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            counterparty (B2bCounterpartyInput):
                거래처 정보
            options (B2bCounterpartyCreateOptions, optional):
                확인 옵션

                사업자 정보 및 휴폐업 상태 조회 옵션입니다.


        Raises:
            UpdateB2bCounterpartyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["counterparty"] = _serialize_b2b_counterparty_input(counterparty)
        if options is not None:
            request_body["options"] = _serialize_b2b_counterparty_create_options(options)
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
            "PATCH",
            f"{self._base_url}/b2b/counterparties/{quote(counterparty_id, safe='')}",
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
                error = _deserialize_b2b_counterparty_brn_modification_not_allowed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyBrnModificationNotAllowedError(error)
            try:
                error = _deserialize_b2b_counterparty_missing_required_fields_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyMissingRequiredFieldsError(error)
            try:
                error = _deserialize_b2b_counterparty_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_partner_not_updatable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyPartnerNotUpdatableError(error)
            try:
                error = _deserialize_b2b_counterparty_too_many_additional_contacts_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyTooManyAdditionalContactsError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_brn_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationBrnMismatchError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_invalid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationInvalidError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_type_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationTypeMismatchError(error)
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
        return _deserialize_update_b2b_counterparty_response(response.json())
    async def update_b2b_counterparty_async(
        self,
        *,
        counterparty_id: str,
        test: Optional[bool] = None,
        counterparty: B2bCounterpartyInput,
        options: Optional[B2bCounterpartyCreateOptions] = None,
    ) -> UpdateB2bCounterpartyResponse:
        """거래처 정보 수정

        거래처 정보를 수정합니다.

        Args:
            counterparty_id (str):
                거래처 ID
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            counterparty (B2bCounterpartyInput):
                거래처 정보
            options (B2bCounterpartyCreateOptions, optional):
                확인 옵션

                사업자 정보 및 휴폐업 상태 조회 옵션입니다.


        Raises:
            UpdateB2bCounterpartyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["counterparty"] = _serialize_b2b_counterparty_input(counterparty)
        if options is not None:
            request_body["options"] = _serialize_b2b_counterparty_create_options(options)
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
            "PATCH",
            f"{self._base_url}/b2b/counterparties/{quote(counterparty_id, safe='')}",
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
                error = _deserialize_b2b_counterparty_brn_modification_not_allowed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyBrnModificationNotAllowedError(error)
            try:
                error = _deserialize_b2b_counterparty_missing_required_fields_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyMissingRequiredFieldsError(error)
            try:
                error = _deserialize_b2b_counterparty_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_partner_not_updatable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyPartnerNotUpdatableError(error)
            try:
                error = _deserialize_b2b_counterparty_too_many_additional_contacts_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyTooManyAdditionalContactsError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_brn_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationBrnMismatchError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_invalid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationInvalidError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_type_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationTypeMismatchError(error)
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
        return _deserialize_update_b2b_counterparty_response(response.json())
    def get_b2b_counterparties(
        self,
        *,
        test: Optional[bool] = None,
        page: Optional[PageInput] = None,
        filter: Optional[B2bCounterpartyFilter] = None,
    ) -> GetB2bCounterpartiesResponse:
        """거래처 검색

        거래처를 검색합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            page (PageInput, optional):
                페이지 정보
            filter (B2bCounterpartyFilter, optional):
                검색 필터


        Raises:
            GetB2bCounterpartiesError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_b2b_counterparty_filter(filter)
        query = []
        if test is not None:
            query.append(("test", test))
        query.append(("requestBody", json.dumps(request_body)))
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/b2b/counterparties",
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
        return _deserialize_get_b2b_counterparties_response(response.json())
    async def get_b2b_counterparties_async(
        self,
        *,
        test: Optional[bool] = None,
        page: Optional[PageInput] = None,
        filter: Optional[B2bCounterpartyFilter] = None,
    ) -> GetB2bCounterpartiesResponse:
        """거래처 검색

        거래처를 검색합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            page (PageInput, optional):
                페이지 정보
            filter (B2bCounterpartyFilter, optional):
                검색 필터


        Raises:
            GetB2bCounterpartiesError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_b2b_counterparty_filter(filter)
        query = []
        if test is not None:
            query.append(("test", test))
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/b2b/counterparties",
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
        return _deserialize_get_b2b_counterparties_response(response.json())
    def create_b2b_counterparty(
        self,
        *,
        test: Optional[bool] = None,
        counterparty_id: Optional[str] = None,
        counterparty: B2bCounterpartyInput,
        options: Optional[B2bCounterpartyCreateOptions] = None,
    ) -> CreateB2bCounterpartyResponse:
        """거래처 생성

        거래처를 생성합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            counterparty_id (str, optional):
                거래처 아이디

                입력하지 않으면 임의의 ID가 채번됩니다.
            counterparty (B2bCounterpartyInput):
                거래처 정보
            options (B2bCounterpartyCreateOptions, optional):
                거래처 생성 옵션


        Raises:
            CreateB2bCounterpartyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if counterparty_id is not None:
            request_body["counterpartyId"] = counterparty_id
        request_body["counterparty"] = _serialize_b2b_counterparty_input(counterparty)
        if options is not None:
            request_body["options"] = _serialize_b2b_counterparty_create_options(options)
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
            "POST",
            f"{self._base_url}/b2b/counterparties",
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
                error = _deserialize_b2b_counterparty_brn_invalid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyBrnInvalidError(error)
            try:
                error = _deserialize_b2b_counterparty_id_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyIdAlreadyExistsError(error)
            try:
                error = _deserialize_b2b_counterparty_id_already_exists_by_partner_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyIdAlreadyExistsByPartnerError(error)
            try:
                error = _deserialize_b2b_counterparty_missing_required_fields_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyMissingRequiredFieldsError(error)
            try:
                error = _deserialize_b2b_counterparty_nts_connection_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNtsConnectionFailedError(error)
            try:
                error = _deserialize_b2b_counterparty_partner_not_connectable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyPartnerNotConnectableError(error)
            try:
                error = _deserialize_b2b_counterparty_self_origin_brn_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartySelfOriginBrnMismatchError(error)
            try:
                error = _deserialize_b2b_counterparty_too_many_additional_contacts_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyTooManyAdditionalContactsError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_brn_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationBrnMismatchError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_invalid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationInvalidError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_type_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationTypeMismatchError(error)
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
        return _deserialize_create_b2b_counterparty_response(response.json())
    async def create_b2b_counterparty_async(
        self,
        *,
        test: Optional[bool] = None,
        counterparty_id: Optional[str] = None,
        counterparty: B2bCounterpartyInput,
        options: Optional[B2bCounterpartyCreateOptions] = None,
    ) -> CreateB2bCounterpartyResponse:
        """거래처 생성

        거래처를 생성합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            counterparty_id (str, optional):
                거래처 아이디

                입력하지 않으면 임의의 ID가 채번됩니다.
            counterparty (B2bCounterpartyInput):
                거래처 정보
            options (B2bCounterpartyCreateOptions, optional):
                거래처 생성 옵션


        Raises:
            CreateB2bCounterpartyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if counterparty_id is not None:
            request_body["counterpartyId"] = counterparty_id
        request_body["counterparty"] = _serialize_b2b_counterparty_input(counterparty)
        if options is not None:
            request_body["options"] = _serialize_b2b_counterparty_create_options(options)
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
            "POST",
            f"{self._base_url}/b2b/counterparties",
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
                error = _deserialize_b2b_counterparty_brn_invalid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyBrnInvalidError(error)
            try:
                error = _deserialize_b2b_counterparty_id_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyIdAlreadyExistsError(error)
            try:
                error = _deserialize_b2b_counterparty_id_already_exists_by_partner_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyIdAlreadyExistsByPartnerError(error)
            try:
                error = _deserialize_b2b_counterparty_missing_required_fields_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyMissingRequiredFieldsError(error)
            try:
                error = _deserialize_b2b_counterparty_nts_connection_failed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyNtsConnectionFailedError(error)
            try:
                error = _deserialize_b2b_counterparty_partner_not_connectable_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyPartnerNotConnectableError(error)
            try:
                error = _deserialize_b2b_counterparty_self_origin_brn_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartySelfOriginBrnMismatchError(error)
            try:
                error = _deserialize_b2b_counterparty_too_many_additional_contacts_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyTooManyAdditionalContactsError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_brn_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationBrnMismatchError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_invalid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationInvalidError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationNotFoundError(error)
            try:
                error = _deserialize_b2b_counterparty_verification_type_mismatch_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise B2bCounterpartyVerificationTypeMismatchError(error)
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
        return _deserialize_create_b2b_counterparty_response(response.json())
