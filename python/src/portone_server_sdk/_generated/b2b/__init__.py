from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.b2b.b2b_bank_account_not_found_error import B2bBankAccountNotFoundError, _deserialize_b2b_bank_account_not_found_error, _serialize_b2b_bank_account_not_found_error
from portone_server_sdk._generated.b2b.b2b_certificate import B2bCertificate, _deserialize_b2b_certificate, _serialize_b2b_certificate
from portone_server_sdk._generated.b2b.b2b_certificate_unregistered_error import B2bCertificateUnregisteredError, _deserialize_b2b_certificate_unregistered_error, _serialize_b2b_certificate_unregistered_error
from portone_server_sdk._generated.b2b.b2b_company_already_registered_error import B2bCompanyAlreadyRegisteredError, _deserialize_b2b_company_already_registered_error, _serialize_b2b_company_already_registered_error
from portone_server_sdk._generated.b2b.b2b_company_contact import B2bCompanyContact, _deserialize_b2b_company_contact, _serialize_b2b_company_contact
from portone_server_sdk._generated.b2b.b2b_company_contact_input import B2bCompanyContactInput, _deserialize_b2b_company_contact_input, _serialize_b2b_company_contact_input
from portone_server_sdk._generated.b2b.b2b_company_not_found_error import B2bCompanyNotFoundError, _deserialize_b2b_company_not_found_error, _serialize_b2b_company_not_found_error
from portone_server_sdk._generated.b2b.b2b_company_state import B2bCompanyState, _deserialize_b2b_company_state, _serialize_b2b_company_state
from portone_server_sdk._generated.b2b.b2b_contact_not_found_error import B2bContactNotFoundError, _deserialize_b2b_contact_not_found_error, _serialize_b2b_contact_not_found_error
from portone_server_sdk._generated.b2b.b2b_external_service_error import B2bExternalServiceError, _deserialize_b2b_external_service_error, _serialize_b2b_external_service_error
from portone_server_sdk._generated.b2b.b2b_file_not_found_error import B2bFileNotFoundError, _deserialize_b2b_file_not_found_error, _serialize_b2b_file_not_found_error
from portone_server_sdk._generated.b2b.b2b_financial_system_communication_error import B2bFinancialSystemCommunicationError, _deserialize_b2b_financial_system_communication_error, _serialize_b2b_financial_system_communication_error
from portone_server_sdk._generated.b2b.b2b_financial_system_failure_error import B2bFinancialSystemFailureError, _deserialize_b2b_financial_system_failure_error, _serialize_b2b_financial_system_failure_error
from portone_server_sdk._generated.b2b.b2b_financial_system_under_maintenance_error import B2bFinancialSystemUnderMaintenanceError, _deserialize_b2b_financial_system_under_maintenance_error, _serialize_b2b_financial_system_under_maintenance_error
from portone_server_sdk._generated.b2b.b2b_foreign_exchange_account_error import B2bForeignExchangeAccountError, _deserialize_b2b_foreign_exchange_account_error, _serialize_b2b_foreign_exchange_account_error
from portone_server_sdk._generated.b2b.b2b_hometax_under_maintenance_error import B2bHometaxUnderMaintenanceError, _deserialize_b2b_hometax_under_maintenance_error, _serialize_b2b_hometax_under_maintenance_error
from portone_server_sdk._generated.b2b.b2b_id_already_exists_error import B2bIdAlreadyExistsError, _deserialize_b2b_id_already_exists_error, _serialize_b2b_id_already_exists_error
from portone_server_sdk._generated.b2b.b2b_member_company import B2bMemberCompany, _deserialize_b2b_member_company, _serialize_b2b_member_company
from portone_server_sdk._generated.b2b.b2b_member_company_not_found_error import B2bMemberCompanyNotFoundError, _deserialize_b2b_member_company_not_found_error, _serialize_b2b_member_company_not_found_error
from portone_server_sdk._generated.b2b.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from portone_server_sdk._generated.b2b.b2b_recipient_not_found_error import B2bRecipientNotFoundError, _deserialize_b2b_recipient_not_found_error, _serialize_b2b_recipient_not_found_error
from portone_server_sdk._generated.b2b.b2b_regular_maintenance_time_error import B2bRegularMaintenanceTimeError, _deserialize_b2b_regular_maintenance_time_error, _serialize_b2b_regular_maintenance_time_error
from portone_server_sdk._generated.b2b.b2b_search_date_type import B2bSearchDateType, _deserialize_b2b_search_date_type, _serialize_b2b_search_date_type
from portone_server_sdk._generated.b2b.b2b_supplier_not_found_error import B2bSupplierNotFoundError, _deserialize_b2b_supplier_not_found_error, _serialize_b2b_supplier_not_found_error
from portone_server_sdk._generated.b2b.b2b_suspended_account_error import B2bSuspendedAccountError, _deserialize_b2b_suspended_account_error, _serialize_b2b_suspended_account_error
from portone_server_sdk._generated.b2b.b2b_tax_invoice import B2bTaxInvoice, _deserialize_b2b_tax_invoice, _serialize_b2b_tax_invoice
from portone_server_sdk._generated.b2b.b2b_tax_invoice_attachment_not_found_error import B2bTaxInvoiceAttachmentNotFoundError, _deserialize_b2b_tax_invoice_attachment_not_found_error, _serialize_b2b_tax_invoice_attachment_not_found_error
from portone_server_sdk._generated.b2b.b2b_tax_invoice_document_key_type import B2bTaxInvoiceDocumentKeyType, _deserialize_b2b_tax_invoice_document_key_type, _serialize_b2b_tax_invoice_document_key_type
from portone_server_sdk._generated.b2b.b2b_tax_invoice_input import B2bTaxInvoiceInput, _deserialize_b2b_tax_invoice_input, _serialize_b2b_tax_invoice_input
from portone_server_sdk._generated.b2b.b2b_tax_invoice_no_recipient_document_key_error import B2bTaxInvoiceNoRecipientDocumentKeyError, _deserialize_b2b_tax_invoice_no_recipient_document_key_error, _serialize_b2b_tax_invoice_no_recipient_document_key_error
from portone_server_sdk._generated.b2b.b2b_tax_invoice_no_supplier_document_key_error import B2bTaxInvoiceNoSupplierDocumentKeyError, _deserialize_b2b_tax_invoice_no_supplier_document_key_error, _serialize_b2b_tax_invoice_no_supplier_document_key_error
from portone_server_sdk._generated.b2b.b2b_tax_invoice_non_deletable_status_error import B2bTaxInvoiceNonDeletableStatusError, _deserialize_b2b_tax_invoice_non_deletable_status_error, _serialize_b2b_tax_invoice_non_deletable_status_error
from portone_server_sdk._generated.b2b.b2b_tax_invoice_not_found_error import B2bTaxInvoiceNotFoundError, _deserialize_b2b_tax_invoice_not_found_error, _serialize_b2b_tax_invoice_not_found_error
from portone_server_sdk._generated.b2b.b2b_tax_invoice_not_issued_status_error import B2bTaxInvoiceNotIssuedStatusError, _deserialize_b2b_tax_invoice_not_issued_status_error, _serialize_b2b_tax_invoice_not_issued_status_error
from portone_server_sdk._generated.b2b.b2b_tax_invoice_not_registered_status_error import B2bTaxInvoiceNotRegisteredStatusError, _deserialize_b2b_tax_invoice_not_registered_status_error, _serialize_b2b_tax_invoice_not_registered_status_error
from portone_server_sdk._generated.b2b.b2b_tax_invoice_not_requested_status_error import B2bTaxInvoiceNotRequestedStatusError, _deserialize_b2b_tax_invoice_not_requested_status_error, _serialize_b2b_tax_invoice_not_requested_status_error
from portone_server_sdk._generated.common.bank import Bank, _deserialize_bank, _serialize_bank
from portone_server_sdk._generated.b2b.create_b2b_tax_invoice_file_upload_link_response import CreateB2bTaxInvoiceFileUploadLinkResponse, _deserialize_create_b2b_tax_invoice_file_upload_link_response, _serialize_create_b2b_tax_invoice_file_upload_link_response
from portone_server_sdk._generated.b2b.get_b2b_bank_account_holder_response import GetB2bBankAccountHolderResponse, _deserialize_get_b2b_bank_account_holder_response, _serialize_get_b2b_bank_account_holder_response
from portone_server_sdk._generated.b2b.get_b2b_certificate_registration_url_response import GetB2bCertificateRegistrationUrlResponse, _deserialize_get_b2b_certificate_registration_url_response, _serialize_get_b2b_certificate_registration_url_response
from portone_server_sdk._generated.b2b.get_b2b_contact_id_existence_response import GetB2bContactIdExistenceResponse, _deserialize_get_b2b_contact_id_existence_response, _serialize_get_b2b_contact_id_existence_response
from portone_server_sdk._generated.b2b.get_b2b_tax_invoice_attachments_response import GetB2bTaxInvoiceAttachmentsResponse, _deserialize_get_b2b_tax_invoice_attachments_response, _serialize_get_b2b_tax_invoice_attachments_response
from portone_server_sdk._generated.b2b.get_b2b_tax_invoice_pdf_download_url_response import GetB2bTaxInvoicePdfDownloadUrlResponse, _deserialize_get_b2b_tax_invoice_pdf_download_url_response, _serialize_get_b2b_tax_invoice_pdf_download_url_response
from portone_server_sdk._generated.b2b.get_b2b_tax_invoice_popup_url_response import GetB2bTaxInvoicePopupUrlResponse, _deserialize_get_b2b_tax_invoice_popup_url_response, _serialize_get_b2b_tax_invoice_popup_url_response
from portone_server_sdk._generated.b2b.get_b2b_tax_invoice_print_url_response import GetB2bTaxInvoicePrintUrlResponse, _deserialize_get_b2b_tax_invoice_print_url_response, _serialize_get_b2b_tax_invoice_print_url_response
from portone_server_sdk._generated.b2b.get_b2b_tax_invoices_response import GetB2bTaxInvoicesResponse, _deserialize_get_b2b_tax_invoices_response, _serialize_get_b2b_tax_invoices_response
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.b2b.register_b2b_member_company_response import RegisterB2bMemberCompanyResponse, _deserialize_register_b2b_member_company_response, _serialize_register_b2b_member_company_response
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from portone_server_sdk._generated.b2b.update_b2b_member_company_contact_response import UpdateB2bMemberCompanyContactResponse, _deserialize_update_b2b_member_company_contact_response, _serialize_update_b2b_member_company_contact_response
from portone_server_sdk._generated.b2b.update_b2b_member_company_response import UpdateB2bMemberCompanyResponse, _deserialize_update_b2b_member_company_response, _serialize_update_b2b_member_company_response
from portone_server_sdk._generated import errors
class B2BClient:
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
            f"{self._base_url}/b2b-preview/member-companies/{brn}",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_serialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
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
            f"{self._base_url}/b2b-preview/member-companies/{brn}",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_serialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_member_company(response.json())
    def update_b2b_member_company(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
        name: Optional[str] = None,
        ceo_name: Optional[str] = None,
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
            name (str, optional):
                회사명
            ceo_name (str, optional):
                대표자 성명
            address (str, optional):
                회사 주소
            business_type (str, optional):
                업태
            business_class (str, optional):
                업종


        Raises:
            B2bMemberCompanyNotFoundError: 연동 사업자가 존재하지 않는 경우
                연동 사업자가 존재하지 않는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if name is not None:
            request_body["name"] = name,
        if ceo_name is not None:
            request_body["ceoName"] = ceo_name,
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
            f"{self._base_url}/b2b-preview/member-companies/{brn}",
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
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_serialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_update_b2b_member_company_response(response.json())
    async def update_b2b_member_company_async(
        self,
        *,
        brn: str,
        test: Optional[bool] = None,
        name: Optional[str] = None,
        ceo_name: Optional[str] = None,
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
            name (str, optional):
                회사명
            ceo_name (str, optional):
                대표자 성명
            address (str, optional):
                회사 주소
            business_type (str, optional):
                업태
            business_class (str, optional):
                업종


        Raises:
            B2bMemberCompanyNotFoundError: 연동 사업자가 존재하지 않는 경우
                연동 사업자가 존재하지 않는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if name is not None:
            request_body["name"] = name,
        if ceo_name is not None:
            request_body["ceoName"] = ceo_name,
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
            f"{self._base_url}/b2b-preview/member-companies/{brn}",
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
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_serialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_update_b2b_member_company_response(response.json())
    def register_b2b_member_company(
        self,
        *,
        test: Optional[bool] = None,
        company: B2bMemberCompany,
        contact: B2bCompanyContactInput,
    ) -> RegisterB2bMemberCompanyResponse:
        """사업자 연동

        포트원 B2B 서비스에 사업자를 연동합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            company (B2bMemberCompany):
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
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["company"] = _serialize_b2b_member_company(company),
        request_body["contact"] = _serialize_b2b_company_contact_input(contact),
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b-preview/member-companies",
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
                raise errors.B2bCompanyAlreadyRegisteredError(_serialize_b2b_company_already_registered_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_ID_ALREADY_EXISTS":
                raise errors.B2bIdAlreadyExistsError(_serialize_b2b_id_already_exists_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_register_b2b_member_company_response(response.json())
    async def register_b2b_member_company_async(
        self,
        *,
        test: Optional[bool] = None,
        company: B2bMemberCompany,
        contact: B2bCompanyContactInput,
    ) -> RegisterB2bMemberCompanyResponse:
        """사업자 연동

        포트원 B2B 서비스에 사업자를 연동합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            company (B2bMemberCompany):
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
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["company"] = _serialize_b2b_member_company(company),
        request_body["contact"] = _serialize_b2b_company_contact_input(contact),
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b-preview/member-companies",
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
                raise errors.B2bCompanyAlreadyRegisteredError(_serialize_b2b_company_already_registered_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_ID_ALREADY_EXISTS":
                raise errors.B2bIdAlreadyExistsError(_serialize_b2b_id_already_exists_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_register_b2b_member_company_response(response.json())
    def get_b2b_member_company_contact(
        self,
        *,
        brn: str,
        contact_id: str,
        test: Optional[bool] = None,
    ) -> B2bCompanyContact:
        """담당자 조회

        연동 사업자에 등록된 담당자를 조회합니다.

        Args:
            brn (str):
                사업자등록번호
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
            f"{self._base_url}/b2b-preview/member-companies/{brn}/contacts/{contact_id}",
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
                raise errors.B2bContactNotFoundError(_serialize_b2b_contact_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_serialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_company_contact(response.json())
    async def get_b2b_member_company_contact_async(
        self,
        *,
        brn: str,
        contact_id: str,
        test: Optional[bool] = None,
    ) -> B2bCompanyContact:
        """담당자 조회

        연동 사업자에 등록된 담당자를 조회합니다.

        Args:
            brn (str):
                사업자등록번호
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
            f"{self._base_url}/b2b-preview/member-companies/{brn}/contacts/{contact_id}",
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
                raise errors.B2bContactNotFoundError(_serialize_b2b_contact_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_serialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_company_contact(response.json())
    def update_b2b_member_company_contact(
        self,
        *,
        brn: str,
        contact_id: str,
        test: Optional[bool] = None,
        password: Optional[str] = None,
        name: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
    ) -> UpdateB2bMemberCompanyContactResponse:
        """담당자 정보 수정

        담당자 정보를 수정합니다.

        Args:
            brn (str):
                사업자등록번호
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
            f"{self._base_url}/b2b-preview/member-companies/{brn}/contacts/{contact_id}",
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
                raise errors.B2bContactNotFoundError(_serialize_b2b_contact_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_serialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_update_b2b_member_company_contact_response(response.json())
    async def update_b2b_member_company_contact_async(
        self,
        *,
        brn: str,
        contact_id: str,
        test: Optional[bool] = None,
        password: Optional[str] = None,
        name: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
    ) -> UpdateB2bMemberCompanyContactResponse:
        """담당자 정보 수정

        담당자 정보를 수정합니다.

        Args:
            brn (str):
                사업자등록번호
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
            f"{self._base_url}/b2b-preview/member-companies/{brn}/contacts/{contact_id}",
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
                raise errors.B2bContactNotFoundError(_serialize_b2b_contact_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_serialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_update_b2b_member_company_contact_response(response.json())
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
            f"{self._base_url}/b2b-preview/member-companies/{brn}/certificate/registration-url",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_serialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
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
            f"{self._base_url}/b2b-preview/member-companies/{brn}/certificate/registration-url",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_serialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_certificate_registration_url_response(response.json())
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
            f"{self._base_url}/b2b-preview/member-companies/{brn}/certificate",
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
                raise errors.B2bCertificateUnregisteredError(_serialize_b2b_certificate_unregistered_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_serialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
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
            f"{self._base_url}/b2b-preview/member-companies/{brn}/certificate",
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
                raise errors.B2bCertificateUnregisteredError(_serialize_b2b_certificate_unregistered_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MEMBER_COMPANY_NOT_FOUND":
                raise errors.B2bMemberCompanyNotFoundError(_serialize_b2b_member_company_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_certificate(response.json())
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
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if contact_id is not None:
            query.append(("contactId", contact_id))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b-preview/member-companies/contacts/id-existence",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
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
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if contact_id is not None:
            query.append(("contactId", contact_id))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b-preview/member-companies/contacts/id-existence",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_contact_id_existence_response(response.json())
    def get_b2b_bank_account_holder(
        self,
        *,
        bank: Bank,
        account_number: str,
        test: Optional[bool] = None,
    ) -> GetB2bBankAccountHolderResponse:
        """예금주 조회

        원하는 계좌의 예금주를 조회합니다.

        Args:
            bank (Bank):
                은행
            account_number (str):
                '-'를 제외한 계좌 번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


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
            f"{self._base_url}/b2b-preview/bank-accounts/{bank}/{account_number}/holder",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_BANK_ACCOUNT_NOT_FOUND":
                raise errors.B2bBankAccountNotFoundError(_serialize_b2b_bank_account_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_FINANCIAL_SYSTEM_COMMUNICATION":
                raise errors.B2bFinancialSystemCommunicationError(_serialize_b2b_financial_system_communication_error(error_response))
            if error_type == "B2B_FINANCIAL_SYSTEM_FAILURE":
                raise errors.B2bFinancialSystemFailureError(_serialize_b2b_financial_system_failure_error(error_response))
            if error_type == "B2B_FINANCIAL_SYSTEM_UNDER_MAINTENANCE":
                raise errors.B2bFinancialSystemUnderMaintenanceError(_serialize_b2b_financial_system_under_maintenance_error(error_response))
            if error_type == "B2B_FOREIGN_EXCHANGE_ACCOUNT":
                raise errors.B2bForeignExchangeAccountError(_serialize_b2b_foreign_exchange_account_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_REGULAR_MAINTENANCE_TIME":
                raise errors.B2bRegularMaintenanceTimeError(_serialize_b2b_regular_maintenance_time_error(error_response))
            if error_type == "B2B_SUSPENDED_ACCOUNT":
                raise errors.B2bSuspendedAccountError(_serialize_b2b_suspended_account_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_bank_account_holder_response(response.json())
    async def get_b2b_bank_account_holder_async(
        self,
        *,
        bank: Bank,
        account_number: str,
        test: Optional[bool] = None,
    ) -> GetB2bBankAccountHolderResponse:
        """예금주 조회

        원하는 계좌의 예금주를 조회합니다.

        Args:
            bank (Bank):
                은행
            account_number (str):
                '-'를 제외한 계좌 번호
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


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
            f"{self._base_url}/b2b-preview/bank-accounts/{bank}/{account_number}/holder",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_BANK_ACCOUNT_NOT_FOUND":
                raise errors.B2bBankAccountNotFoundError(_serialize_b2b_bank_account_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_FINANCIAL_SYSTEM_COMMUNICATION":
                raise errors.B2bFinancialSystemCommunicationError(_serialize_b2b_financial_system_communication_error(error_response))
            if error_type == "B2B_FINANCIAL_SYSTEM_FAILURE":
                raise errors.B2bFinancialSystemFailureError(_serialize_b2b_financial_system_failure_error(error_response))
            if error_type == "B2B_FINANCIAL_SYSTEM_UNDER_MAINTENANCE":
                raise errors.B2bFinancialSystemUnderMaintenanceError(_serialize_b2b_financial_system_under_maintenance_error(error_response))
            if error_type == "B2B_FOREIGN_EXCHANGE_ACCOUNT":
                raise errors.B2bForeignExchangeAccountError(_serialize_b2b_foreign_exchange_account_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_REGULAR_MAINTENANCE_TIME":
                raise errors.B2bRegularMaintenanceTimeError(_serialize_b2b_regular_maintenance_time_error(error_response))
            if error_type == "B2B_SUSPENDED_ACCOUNT":
                raise errors.B2bSuspendedAccountError(_serialize_b2b_suspended_account_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
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
            f"{self._base_url}/b2b-preview/company/{brn}/state",
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
                raise errors.B2bCompanyNotFoundError(_serialize_b2b_company_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_HOMETAX_UNDER_MAINTENANCE":
                raise errors.B2bHometaxUnderMaintenanceError(_serialize_b2b_hometax_under_maintenance_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
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
            f"{self._base_url}/b2b-preview/company/{brn}/state",
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
                raise errors.B2bCompanyNotFoundError(_serialize_b2b_company_not_found_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_HOMETAX_UNDER_MAINTENANCE":
                raise errors.B2bHometaxUnderMaintenanceError(_serialize_b2b_hometax_under_maintenance_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_company_state(response.json())
    def request_b2b_tax_invoice_reverse_issuance(
        self,
        *,
        test: Optional[bool] = None,
        tax_invoice: B2bTaxInvoiceInput,
        memo: Optional[str] = None,
    ) -> B2bTaxInvoice:
        """세금계산서 역발행 요청

        공급자에게 세금계산서 역발행을 요청합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            tax_invoice (B2bTaxInvoiceInput):
                세금계산서 생성 요청 정보
            memo (str, optional):
                메모


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bRecipientNotFoundError: 공급받는자가 존재하지 않은 경우
                공급받는자가 존재하지 않은 경우
            B2bSupplierNotFoundError: 공급자가 존재하지 않은 경우
                공급자가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["taxInvoice"] = _serialize_b2b_tax_invoice_input(tax_invoice),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/request-reverse-issuance",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_RECIPIENT_NOT_FOUND":
                raise errors.B2bRecipientNotFoundError(_serialize_b2b_recipient_not_found_error(error_response))
            if error_type == "B2B_SUPPLIER_NOT_FOUND":
                raise errors.B2bSupplierNotFoundError(_serialize_b2b_supplier_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    async def request_b2b_tax_invoice_reverse_issuance_async(
        self,
        *,
        test: Optional[bool] = None,
        tax_invoice: B2bTaxInvoiceInput,
        memo: Optional[str] = None,
    ) -> B2bTaxInvoice:
        """세금계산서 역발행 요청

        공급자에게 세금계산서 역발행을 요청합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            tax_invoice (B2bTaxInvoiceInput):
                세금계산서 생성 요청 정보
            memo (str, optional):
                메모


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bRecipientNotFoundError: 공급받는자가 존재하지 않은 경우
                공급받는자가 존재하지 않은 경우
            B2bSupplierNotFoundError: 공급자가 존재하지 않은 경우
                공급자가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["taxInvoice"] = _serialize_b2b_tax_invoice_input(tax_invoice),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/request-reverse-issuance",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_RECIPIENT_NOT_FOUND":
                raise errors.B2bRecipientNotFoundError(_serialize_b2b_recipient_not_found_error(error_response))
            if error_type == "B2B_SUPPLIER_NOT_FOUND":
                raise errors.B2bSupplierNotFoundError(_serialize_b2b_supplier_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    def get_b2b_tax_invoice(
        self,
        *,
        document_key: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> B2bTaxInvoice:
        """세금 계산서 조회

        등록된 세금 계산서를 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    async def get_b2b_tax_invoice_async(
        self,
        *,
        document_key: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> B2bTaxInvoice:
        """세금 계산서 조회

        등록된 세금 계산서를 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    def delete_b2b_tax_invoice(
        self,
        *,
        document_key: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> None:
        """세금계산서 삭제

        세금계산서를 삭제합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNonDeletableStatusError: 세금계산서가 삭제 가능한 상태가 아닌 경우
                세금계산서가 삭제 가능한 상태가 아닌 경우

                삭제 가능한 상태는 `REGISTERED`, `ISSUE_REFUSED`, `REQUEST_CANCELLED_BY_RECIPIENT`, `ISSUE_CANCELLED_BY_SUPPLIER`, `SENDING_FAILED` 입니다.
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NON_DELETABLE_STATUS":
                raise errors.B2bTaxInvoiceNonDeletableStatusError(_serialize_b2b_tax_invoice_non_deletable_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
    async def delete_b2b_tax_invoice_async(
        self,
        *,
        document_key: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> None:
        """세금계산서 삭제

        세금계산서를 삭제합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNonDeletableStatusError: 세금계산서가 삭제 가능한 상태가 아닌 경우
                세금계산서가 삭제 가능한 상태가 아닌 경우

                삭제 가능한 상태는 `REGISTERED`, `ISSUE_REFUSED`, `REQUEST_CANCELLED_BY_RECIPIENT`, `ISSUE_CANCELLED_BY_SUPPLIER`, `SENDING_FAILED` 입니다.
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NON_DELETABLE_STATUS":
                raise errors.B2bTaxInvoiceNonDeletableStatusError(_serialize_b2b_tax_invoice_non_deletable_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
    def issue_b2b_tax_invoice(
        self,
        *,
        test: Optional[bool] = None,
        brn: str,
        document_key: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        memo: Optional[str] = None,
        email_subject: Optional[str] = None,
    ) -> B2bTaxInvoice:
        """세금계산서 발행

        역발행의 경우 역발행요청(REQUESTED) 상태, 정발행의 경우 임시저장(REGISTERED) 상태의 세금계산서를 발행합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str):
                사업자등록번호
            document_key (str):
                세금계산서 문서 번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            memo (str, optional):
                메모
            email_subject (str, optional):
                이메일 제목


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotRequestedStatusError: 세금계산서가 역발행 대기 상태가 아닌 경우
                세금계산서가 역발행 대기 상태가 아닌 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["brn"] = brn,
        request_body["documentKey"] = document_key,
        if document_key_type is not None:
            request_body["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(document_key_type),
        if memo is not None:
            request_body["memo"] = memo,
        if email_subject is not None:
            request_body["emailSubject"] = email_subject,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/issue",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
                raise errors.B2bTaxInvoiceNotRequestedStatusError(_serialize_b2b_tax_invoice_not_requested_status_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    async def issue_b2b_tax_invoice_async(
        self,
        *,
        test: Optional[bool] = None,
        brn: str,
        document_key: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        memo: Optional[str] = None,
        email_subject: Optional[str] = None,
    ) -> B2bTaxInvoice:
        """세금계산서 발행

        역발행의 경우 역발행요청(REQUESTED) 상태, 정발행의 경우 임시저장(REGISTERED) 상태의 세금계산서를 발행합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str):
                사업자등록번호
            document_key (str):
                세금계산서 문서 번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            memo (str, optional):
                메모
            email_subject (str, optional):
                이메일 제목


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotRequestedStatusError: 세금계산서가 역발행 대기 상태가 아닌 경우
                세금계산서가 역발행 대기 상태가 아닌 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["brn"] = brn,
        request_body["documentKey"] = document_key,
        if document_key_type is not None:
            request_body["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(document_key_type),
        if memo is not None:
            request_body["memo"] = memo,
        if email_subject is not None:
            request_body["emailSubject"] = email_subject,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/issue",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
                raise errors.B2bTaxInvoiceNotRequestedStatusError(_serialize_b2b_tax_invoice_not_requested_status_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    def cancel_b2b_tax_invoice_request(
        self,
        *,
        test: Optional[bool] = None,
        brn: str,
        document_key: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        memo: Optional[str] = None,
    ) -> B2bTaxInvoice:
        """세금계산서 역발행 요청 취소

        공급받는자가 공급자에게 세금계산서 역발행 요청한 것을 취소합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str):
                사업자등록번호
            document_key (str):
                세금계산서 문서 번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            memo (str, optional):
                메모


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotRequestedStatusError: 세금계산서가 역발행 대기 상태가 아닌 경우
                세금계산서가 역발행 대기 상태가 아닌 경우
            B2bTaxInvoiceNoRecipientDocumentKeyError: 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
                세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["brn"] = brn,
        request_body["documentKey"] = document_key,
        if document_key_type is not None:
            request_body["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(document_key_type),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/cancel-request",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
                raise errors.B2bTaxInvoiceNotRequestedStatusError(_serialize_b2b_tax_invoice_not_requested_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoRecipientDocumentKeyError(_serialize_b2b_tax_invoice_no_recipient_document_key_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    async def cancel_b2b_tax_invoice_request_async(
        self,
        *,
        test: Optional[bool] = None,
        brn: str,
        document_key: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        memo: Optional[str] = None,
    ) -> B2bTaxInvoice:
        """세금계산서 역발행 요청 취소

        공급받는자가 공급자에게 세금계산서 역발행 요청한 것을 취소합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str):
                사업자등록번호
            document_key (str):
                세금계산서 문서 번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            memo (str, optional):
                메모


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotRequestedStatusError: 세금계산서가 역발행 대기 상태가 아닌 경우
                세금계산서가 역발행 대기 상태가 아닌 경우
            B2bTaxInvoiceNoRecipientDocumentKeyError: 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
                세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["brn"] = brn,
        request_body["documentKey"] = document_key,
        if document_key_type is not None:
            request_body["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(document_key_type),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/cancel-request",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
                raise errors.B2bTaxInvoiceNotRequestedStatusError(_serialize_b2b_tax_invoice_not_requested_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoRecipientDocumentKeyError(_serialize_b2b_tax_invoice_no_recipient_document_key_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    def cancel_b2b_tax_invoice_issuance(
        self,
        *,
        test: Optional[bool] = None,
        brn: str,
        document_key: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        memo: Optional[str] = None,
    ) -> B2bTaxInvoice:
        """세금계산서 역발행 취소

        공급자가 발행 완료한 세금계산서를 국세청 전송 전 취소합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str):
                사업자등록번호
            document_key (str):
                세금계산서 문서 번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            memo (str, optional):
                메모


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotIssuedStatusError: 세금계산서가 발행된(ISSUED) 상태가 아닌 경우
                세금계산서가 발행된(ISSUED) 상태가 아닌 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["brn"] = brn,
        request_body["documentKey"] = document_key,
        if document_key_type is not None:
            request_body["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(document_key_type),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/cancel-issuance",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_ISSUED_STATUS":
                raise errors.B2bTaxInvoiceNotIssuedStatusError(_serialize_b2b_tax_invoice_not_issued_status_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    async def cancel_b2b_tax_invoice_issuance_async(
        self,
        *,
        test: Optional[bool] = None,
        brn: str,
        document_key: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        memo: Optional[str] = None,
    ) -> B2bTaxInvoice:
        """세금계산서 역발행 취소

        공급자가 발행 완료한 세금계산서를 국세청 전송 전 취소합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str):
                사업자등록번호
            document_key (str):
                세금계산서 문서 번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            memo (str, optional):
                메모


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotIssuedStatusError: 세금계산서가 발행된(ISSUED) 상태가 아닌 경우
                세금계산서가 발행된(ISSUED) 상태가 아닌 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["brn"] = brn,
        request_body["documentKey"] = document_key,
        if document_key_type is not None:
            request_body["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(document_key_type),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/cancel-issuance",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_ISSUED_STATUS":
                raise errors.B2bTaxInvoiceNotIssuedStatusError(_serialize_b2b_tax_invoice_not_issued_status_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    def refuse_b2b_tax_invoice_request(
        self,
        *,
        test: Optional[bool] = None,
        brn: str,
        document_key: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        memo: Optional[str] = None,
    ) -> B2bTaxInvoice:
        """세금계산서 역발행 요청 거부

        공급자가 공급받는자로부터 요청받은 세금계산서 역발행 건을 거부합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str):
                사업자등록번호
            document_key (str):
                세금계산서 문서 번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            memo (str, optional):
                메모


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotRequestedStatusError: 세금계산서가 역발행 대기 상태가 아닌 경우
                세금계산서가 역발행 대기 상태가 아닌 경우
            B2bTaxInvoiceNoSupplierDocumentKeyError: 세금계산서에 공급자 문서 번호가 기입되지 않은 경우
                세금계산서에 공급자 문서 번호가 기입되지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["brn"] = brn,
        request_body["documentKey"] = document_key,
        if document_key_type is not None:
            request_body["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(document_key_type),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/refuse-request",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
                raise errors.B2bTaxInvoiceNotRequestedStatusError(_serialize_b2b_tax_invoice_not_requested_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_SUPPLIER_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoSupplierDocumentKeyError(_serialize_b2b_tax_invoice_no_supplier_document_key_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    async def refuse_b2b_tax_invoice_request_async(
        self,
        *,
        test: Optional[bool] = None,
        brn: str,
        document_key: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        memo: Optional[str] = None,
    ) -> B2bTaxInvoice:
        """세금계산서 역발행 요청 거부

        공급자가 공급받는자로부터 요청받은 세금계산서 역발행 건을 거부합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str):
                사업자등록번호
            document_key (str):
                세금계산서 문서 번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            memo (str, optional):
                메모


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotRequestedStatusError: 세금계산서가 역발행 대기 상태가 아닌 경우
                세금계산서가 역발행 대기 상태가 아닌 경우
            B2bTaxInvoiceNoSupplierDocumentKeyError: 세금계산서에 공급자 문서 번호가 기입되지 않은 경우
                세금계산서에 공급자 문서 번호가 기입되지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["brn"] = brn,
        request_body["documentKey"] = document_key,
        if document_key_type is not None:
            request_body["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(document_key_type),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/refuse-request",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
                raise errors.B2bTaxInvoiceNotRequestedStatusError(_serialize_b2b_tax_invoice_not_requested_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_SUPPLIER_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoSupplierDocumentKeyError(_serialize_b2b_tax_invoice_no_supplier_document_key_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    def get_b2b_tax_invoices(
        self,
        *,
        brn: str,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
        from_: str,
        until: str,
        date_type: B2bSearchDateType,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicesResponse:
        """세금 계산서 다건조회

        조회 기간 내 등록된 세금 계산서를 다건 조회합니다.

        Args:
            brn (str):
                사업자등록번호
            page_number (int, optional):
                페이지 번호

                0부터 시작하는 페이지 번호. 기본 값은 0.
            page_size (int, optional):
                페이지 크기

                각 페이지 당 포함할 객체 수. 기본 값은 500이며 최대 1000까지 요청가능합니다.
            from_ (str):
                조회 시작일
            until (str):
                조회 종료일
            date_type (B2bSearchDateType):
                조회 기간 기준
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if page_number is not None:
            query.append(("pageNumber", page_number))
        if page_size is not None:
            query.append(("pageSize", page_size))
        if from_ is not None:
            query.append(("from", from_))
        if until is not None:
            query.append(("until", until))
        if date_type is not None:
            query.append(("dateType", date_type))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b-preview/tax-invoices",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoices_response(response.json())
    async def get_b2b_tax_invoices_async(
        self,
        *,
        brn: str,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
        from_: str,
        until: str,
        date_type: B2bSearchDateType,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicesResponse:
        """세금 계산서 다건조회

        조회 기간 내 등록된 세금 계산서를 다건 조회합니다.

        Args:
            brn (str):
                사업자등록번호
            page_number (int, optional):
                페이지 번호

                0부터 시작하는 페이지 번호. 기본 값은 0.
            page_size (int, optional):
                페이지 크기

                각 페이지 당 포함할 객체 수. 기본 값은 500이며 최대 1000까지 요청가능합니다.
            from_ (str):
                조회 시작일
            until (str):
                조회 종료일
            date_type (B2bSearchDateType):
                조회 기간 기준
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if page_number is not None:
            query.append(("pageNumber", page_number))
        if page_size is not None:
            query.append(("pageSize", page_size))
        if from_ is not None:
            query.append(("from", from_))
        if until is not None:
            query.append(("until", until))
        if date_type is not None:
            query.append(("dateType", date_type))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b-preview/tax-invoices",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoices_response(response.json())
    def get_b2b_tax_invoice_popup_url(
        self,
        *,
        document_key: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        include_menu: Optional[bool] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicePopupUrlResponse:
        """세금 계산서 팝업 URL 조회

        등록된 세금 계산서 팝업 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            include_menu (bool, optional):
                메뉴 포함 여부

                팝업 URL에 메뉴 레이아웃을 포함 여부를 결정합니다. 기본 값은 true입니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if include_menu is not None:
            query.append(("includeMenu", include_menu))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}/popup-url",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_popup_url_response(response.json())
    async def get_b2b_tax_invoice_popup_url_async(
        self,
        *,
        document_key: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        include_menu: Optional[bool] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicePopupUrlResponse:
        """세금 계산서 팝업 URL 조회

        등록된 세금 계산서 팝업 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            include_menu (bool, optional):
                메뉴 포함 여부

                팝업 URL에 메뉴 레이아웃을 포함 여부를 결정합니다. 기본 값은 true입니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if include_menu is not None:
            query.append(("includeMenu", include_menu))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}/popup-url",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_popup_url_response(response.json())
    def get_b2b_tax_invoice_print_url(
        self,
        *,
        document_key: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicePrintUrlResponse:
        """세금 계산서 프린트 URL 조회

        등록된 세금 계산서 프린트 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}/print-url",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_print_url_response(response.json())
    async def get_b2b_tax_invoice_print_url_async(
        self,
        *,
        document_key: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicePrintUrlResponse:
        """세금 계산서 프린트 URL 조회

        등록된 세금 계산서 프린트 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}/print-url",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_print_url_response(response.json())
    def get_b2b_tax_invoice_pdf_download_url(
        self,
        *,
        document_key: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicePdfDownloadUrlResponse:
        """세금 계산서 PDF 다운로드 URL 조회

        등록된 세금 계산서 PDF 다운로드 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}/pdf-download-url",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_pdf_download_url_response(response.json())
    async def get_b2b_tax_invoice_pdf_download_url_async(
        self,
        *,
        document_key: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicePdfDownloadUrlResponse:
        """세금 계산서 PDF 다운로드 URL 조회

        등록된 세금 계산서 PDF 다운로드 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}/pdf-download-url",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_pdf_download_url_response(response.json())
    def request_b2b_tax_invoice_register(
        self,
        *,
        test: Optional[bool] = None,
        tax_invoice: B2bTaxInvoiceInput,
    ) -> B2bTaxInvoice:
        """세금계산서 임시 저장

        세금계산서 임시 저장을 요청합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            tax_invoice (B2bTaxInvoiceInput):
                세금계산서 생성 요청 정보


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bRecipientNotFoundError: 공급받는자가 존재하지 않은 경우
                공급받는자가 존재하지 않은 경우
            B2bSupplierNotFoundError: 공급자가 존재하지 않은 경우
                공급자가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["taxInvoice"] = _serialize_b2b_tax_invoice_input(tax_invoice),
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/register",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_RECIPIENT_NOT_FOUND":
                raise errors.B2bRecipientNotFoundError(_serialize_b2b_recipient_not_found_error(error_response))
            if error_type == "B2B_SUPPLIER_NOT_FOUND":
                raise errors.B2bSupplierNotFoundError(_serialize_b2b_supplier_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    async def request_b2b_tax_invoice_register_async(
        self,
        *,
        test: Optional[bool] = None,
        tax_invoice: B2bTaxInvoiceInput,
    ) -> B2bTaxInvoice:
        """세금계산서 임시 저장

        세금계산서 임시 저장을 요청합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            tax_invoice (B2bTaxInvoiceInput):
                세금계산서 생성 요청 정보


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bRecipientNotFoundError: 공급받는자가 존재하지 않은 경우
                공급받는자가 존재하지 않은 경우
            B2bSupplierNotFoundError: 공급자가 존재하지 않은 경우
                공급자가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["taxInvoice"] = _serialize_b2b_tax_invoice_input(tax_invoice),
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/register",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_RECIPIENT_NOT_FOUND":
                raise errors.B2bRecipientNotFoundError(_serialize_b2b_recipient_not_found_error(error_response))
            if error_type == "B2B_SUPPLIER_NOT_FOUND":
                raise errors.B2bSupplierNotFoundError(_serialize_b2b_supplier_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    def request_b2b_tax_invoice(
        self,
        *,
        test: Optional[bool] = None,
        brn: str,
        document_key: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        memo: Optional[str] = None,
    ) -> B2bTaxInvoice:
        """세금계산서 역발행 요청

        임시저장(REGISTERED) 상태의 역발행 세금계산서를 공급자에게 발행 요청합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str):
                사업자등록번호
            document_key (str):
                세금계산서 문서 번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            memo (str, optional):
                메모


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotRegisteredStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            B2bTaxInvoiceNoRecipientDocumentKeyError: 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
                세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["brn"] = brn,
        request_body["documentKey"] = document_key,
        if document_key_type is not None:
            request_body["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(document_key_type),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/request",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REGISTERED_STATUS":
                raise errors.B2bTaxInvoiceNotRegisteredStatusError(_serialize_b2b_tax_invoice_not_registered_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoRecipientDocumentKeyError(_serialize_b2b_tax_invoice_no_recipient_document_key_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    async def request_b2b_tax_invoice_async(
        self,
        *,
        test: Optional[bool] = None,
        brn: str,
        document_key: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        memo: Optional[str] = None,
    ) -> B2bTaxInvoice:
        """세금계산서 역발행 요청

        임시저장(REGISTERED) 상태의 역발행 세금계산서를 공급자에게 발행 요청합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str):
                사업자등록번호
            document_key (str):
                세금계산서 문서 번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            memo (str, optional):
                메모


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotRegisteredStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            B2bTaxInvoiceNoRecipientDocumentKeyError: 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
                세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["brn"] = brn,
        request_body["documentKey"] = document_key,
        if document_key_type is not None:
            request_body["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(document_key_type),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/request",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REGISTERED_STATUS":
                raise errors.B2bTaxInvoiceNotRegisteredStatusError(_serialize_b2b_tax_invoice_not_registered_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoRecipientDocumentKeyError(_serialize_b2b_tax_invoice_no_recipient_document_key_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    def create_b2b_tax_invoice_file_upload_link(
        self,
        *,
        test: Optional[bool] = None,
        file_name: str,
    ) -> CreateB2bTaxInvoiceFileUploadLinkResponse:
        """세금계산서 파일 업로드 링크 생성

        세금계산서의 첨부파일를 업로드할 링크를 생성합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            file_name (str):
                파일 이름


        Raises:
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["fileName"] = file_name,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/file-upload-link",
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
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_create_b2b_tax_invoice_file_upload_link_response(response.json())
    async def create_b2b_tax_invoice_file_upload_link_async(
        self,
        *,
        test: Optional[bool] = None,
        file_name: str,
    ) -> CreateB2bTaxInvoiceFileUploadLinkResponse:
        """세금계산서 파일 업로드 링크 생성

        세금계산서의 첨부파일를 업로드할 링크를 생성합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            file_name (str):
                파일 이름


        Raises:
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["fileName"] = file_name,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/file-upload-link",
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
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_create_b2b_tax_invoice_file_upload_link_response(response.json())
    def attach_b2b_tax_invoice_file(
        self,
        *,
        test: Optional[bool] = None,
        brn: str,
        document_key: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        file_id: str,
    ) -> None:
        """세금계산서 파일 첨부

        세금계산서에 파일을 첨부합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str):
                사업자등록번호

                `-` 없이 숫자 10자리로 구성됩니다.
            document_key (str):
                세금계산서 문서 번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            file_id (str):
                파일 아이디


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bFileNotFoundError: 업로드한 파일을 찾을 수 없는 경우
                업로드한 파일을 찾을 수 없는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotRegisteredStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["brn"] = brn,
        request_body["documentKey"] = document_key,
        if document_key_type is not None:
            request_body["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(document_key_type),
        request_body["fileId"] = file_id,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/attach-file",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_FILE_NOT_FOUND":
                raise errors.B2bFileNotFoundError(_serialize_b2b_file_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REGISTERED_STATUS":
                raise errors.B2bTaxInvoiceNotRegisteredStatusError(_serialize_b2b_tax_invoice_not_registered_status_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
    async def attach_b2b_tax_invoice_file_async(
        self,
        *,
        test: Optional[bool] = None,
        brn: str,
        document_key: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        file_id: str,
    ) -> None:
        """세금계산서 파일 첨부

        세금계산서에 파일을 첨부합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str):
                사업자등록번호

                `-` 없이 숫자 10자리로 구성됩니다.
            document_key (str):
                세금계산서 문서 번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            file_id (str):
                파일 아이디


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bFileNotFoundError: 업로드한 파일을 찾을 수 없는 경우
                업로드한 파일을 찾을 수 없는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotRegisteredStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["brn"] = brn,
        request_body["documentKey"] = document_key,
        if document_key_type is not None:
            request_body["documentKeyType"] = _serialize_b2b_tax_invoice_document_key_type(document_key_type),
        request_body["fileId"] = file_id,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b-preview/tax-invoices/attach-file",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_FILE_NOT_FOUND":
                raise errors.B2bFileNotFoundError(_serialize_b2b_file_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REGISTERED_STATUS":
                raise errors.B2bTaxInvoiceNotRegisteredStatusError(_serialize_b2b_tax_invoice_not_registered_status_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
    def get_b2b_tax_invoice_attachments(
        self,
        *,
        document_key: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoiceAttachmentsResponse:
        """세금계산서 첨부파일 목록 조회

        세금계산서에 첨부된 파일 목록을 조회합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}/attachments",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_attachments_response(response.json())
    async def get_b2b_tax_invoice_attachments_async(
        self,
        *,
        document_key: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoiceAttachmentsResponse:
        """세금계산서 첨부파일 목록 조회

        세금계산서에 첨부된 파일 목록을 조회합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}/attachments",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_attachments_response(response.json())
    def delete_b2b_tax_invoice_attachment(
        self,
        *,
        document_key: str,
        attachment_id: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> None:
        """세금계산서 첨부파일 삭제

        세금계산서 첨부파일을 삭제합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            attachment_id (str):
                첨부파일 아이디
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceAttachmentNotFoundError: 세금계산서의 첨부파일을 찾을 수 없는 경우
                세금계산서의 첨부파일을 찾을 수 없는 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotRegisteredStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}/attachments/{attachment_id}",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND":
                raise errors.B2bTaxInvoiceAttachmentNotFoundError(_serialize_b2b_tax_invoice_attachment_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REGISTERED_STATUS":
                raise errors.B2bTaxInvoiceNotRegisteredStatusError(_serialize_b2b_tax_invoice_not_registered_status_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
    async def delete_b2b_tax_invoice_attachment_async(
        self,
        *,
        document_key: str,
        attachment_id: str,
        brn: str,
        document_key_type: Optional[B2bTaxInvoiceDocumentKeyType] = None,
        test: Optional[bool] = None,
    ) -> None:
        """세금계산서 첨부파일 삭제

        세금계산서 첨부파일을 삭제합니다.

        Args:
            document_key (str):
                세금계산서 문서 번호
            attachment_id (str):
                첨부파일 아이디
            brn (str):
                사업자등록번호
            document_key_type (B2bTaxInvoiceDocumentKeyType, optional):
                문서 번호 유형

                path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceAttachmentNotFoundError: 세금계산서의 첨부파일을 찾을 수 없는 경우
                세금계산서의 첨부파일을 찾을 수 없는 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotRegisteredStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if document_key_type is not None:
            query.append(("documentKeyType", document_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/b2b-preview/tax-invoices/{document_key}/attachments/{attachment_id}",
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
                raise errors.B2bExternalServiceError(_serialize_b2b_external_service_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_serialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND":
                raise errors.B2bTaxInvoiceAttachmentNotFoundError(_serialize_b2b_tax_invoice_attachment_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_serialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REGISTERED_STATUS":
                raise errors.B2bTaxInvoiceNotRegisteredStatusError(_serialize_b2b_tax_invoice_not_registered_status_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_serialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_serialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
