from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.b2b.tax_invoice.b2b_cannot_change_tax_type_error import B2BCannotChangeTaxTypeError, _deserialize_b2b_cannot_change_tax_type_error, _serialize_b2b_cannot_change_tax_type_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_status_not_sending_completed_error import B2BTaxInvoiceStatusNotSendingCompletedError, _deserialize_b2b_tax_invoice_status_not_sending_completed_error, _serialize_b2b_tax_invoice_status_not_sending_completed_error
from portone_server_sdk._generated.common.b2b_external_service_error import B2bExternalServiceError, _deserialize_b2b_external_service_error, _serialize_b2b_external_service_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_file_not_found_error import B2bFileNotFoundError, _deserialize_b2b_file_not_found_error, _serialize_b2b_file_not_found_error
from portone_server_sdk._generated.common.b2b_id_already_exists_error import B2bIdAlreadyExistsError, _deserialize_b2b_id_already_exists_error, _serialize_b2b_id_already_exists_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_modification_not_provided_error import B2bModificationNotProvidedError, _deserialize_b2b_modification_not_provided_error, _serialize_b2b_modification_not_provided_error
from portone_server_sdk._generated.common.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_original_tax_invoice_not_found_error import B2bOriginalTaxInvoiceNotFoundError, _deserialize_b2b_original_tax_invoice_not_found_error, _serialize_b2b_original_tax_invoice_not_found_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_recipient_not_found_error import B2bRecipientNotFoundError, _deserialize_b2b_recipient_not_found_error, _serialize_b2b_recipient_not_found_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_supplier_not_found_error import B2bSupplierNotFoundError, _deserialize_b2b_supplier_not_found_error, _serialize_b2b_supplier_not_found_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice import B2bTaxInvoice, _deserialize_b2b_tax_invoice, _serialize_b2b_tax_invoice
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_attachment_not_found_error import B2bTaxInvoiceAttachmentNotFoundError, _deserialize_b2b_tax_invoice_attachment_not_found_error, _serialize_b2b_tax_invoice_attachment_not_found_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_input import B2bTaxInvoiceInput, _deserialize_b2b_tax_invoice_input, _serialize_b2b_tax_invoice_input
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_key_type import B2bTaxInvoiceKeyType, _deserialize_b2b_tax_invoice_key_type, _serialize_b2b_tax_invoice_key_type
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_modification_create_body import B2bTaxInvoiceModificationCreateBody, _deserialize_b2b_tax_invoice_modification_create_body, _serialize_b2b_tax_invoice_modification_create_body
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_modification_update_body import B2bTaxInvoiceModificationUpdateBody, _deserialize_b2b_tax_invoice_modification_update_body, _serialize_b2b_tax_invoice_modification_update_body
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_no_recipient_document_key_error import B2bTaxInvoiceNoRecipientDocumentKeyError, _deserialize_b2b_tax_invoice_no_recipient_document_key_error, _serialize_b2b_tax_invoice_no_recipient_document_key_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_no_supplier_document_key_error import B2bTaxInvoiceNoSupplierDocumentKeyError, _deserialize_b2b_tax_invoice_no_supplier_document_key_error, _serialize_b2b_tax_invoice_no_supplier_document_key_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_non_deletable_status_error import B2bTaxInvoiceNonDeletableStatusError, _deserialize_b2b_tax_invoice_non_deletable_status_error, _serialize_b2b_tax_invoice_non_deletable_status_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_not_drafted_status_error import B2bTaxInvoiceNotDraftedStatusError, _deserialize_b2b_tax_invoice_not_drafted_status_error, _serialize_b2b_tax_invoice_not_drafted_status_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_not_found_error import B2bTaxInvoiceNotFoundError, _deserialize_b2b_tax_invoice_not_found_error, _serialize_b2b_tax_invoice_not_found_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_not_issued_status_error import B2bTaxInvoiceNotIssuedStatusError, _deserialize_b2b_tax_invoice_not_issued_status_error, _serialize_b2b_tax_invoice_not_issued_status_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_not_requested_status_error import B2bTaxInvoiceNotRequestedStatusError, _deserialize_b2b_tax_invoice_not_requested_status_error, _serialize_b2b_tax_invoice_not_requested_status_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_recipient_document_key_already_used_error import B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError, _deserialize_b2b_tax_invoice_recipient_document_key_already_used_error, _serialize_b2b_tax_invoice_recipient_document_key_already_used_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_supplier_document_key_already_used_error import B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError, _deserialize_b2b_tax_invoice_supplier_document_key_already_used_error, _serialize_b2b_tax_invoice_supplier_document_key_already_used_error
from portone_server_sdk._generated.b2b.tax_invoice.cancel_b2b_tax_invoice_issuance_response import CancelB2bTaxInvoiceIssuanceResponse, _deserialize_cancel_b2b_tax_invoice_issuance_response, _serialize_cancel_b2b_tax_invoice_issuance_response
from portone_server_sdk._generated.b2b.tax_invoice.cancel_b2b_tax_invoice_request_response import CancelB2bTaxInvoiceRequestResponse, _deserialize_cancel_b2b_tax_invoice_request_response, _serialize_cancel_b2b_tax_invoice_request_response
from portone_server_sdk._generated.b2b.tax_invoice.create_b2b_file_upload_url_payload import CreateB2bFileUploadUrlPayload, _deserialize_create_b2b_file_upload_url_payload, _serialize_create_b2b_file_upload_url_payload
from portone_server_sdk._generated.b2b.tax_invoice.delete_b2b_tax_invoice_response import DeleteB2bTaxInvoiceResponse, _deserialize_delete_b2b_tax_invoice_response, _serialize_delete_b2b_tax_invoice_response
from portone_server_sdk._generated.b2b.tax_invoice.draft_b2b_tax_invoice_response import DraftB2bTaxInvoiceResponse, _deserialize_draft_b2b_tax_invoice_response, _serialize_draft_b2b_tax_invoice_response
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.b2b.tax_invoice.get_b2b_tax_invoice_attachments_response import GetB2bTaxInvoiceAttachmentsResponse, _deserialize_get_b2b_tax_invoice_attachments_response, _serialize_get_b2b_tax_invoice_attachments_response
from portone_server_sdk._generated.b2b.tax_invoice.get_b2b_tax_invoice_pdf_download_url_response import GetB2bTaxInvoicePdfDownloadUrlResponse, _deserialize_get_b2b_tax_invoice_pdf_download_url_response, _serialize_get_b2b_tax_invoice_pdf_download_url_response
from portone_server_sdk._generated.b2b.tax_invoice.get_b2b_tax_invoice_popup_url_response import GetB2bTaxInvoicePopupUrlResponse, _deserialize_get_b2b_tax_invoice_popup_url_response, _serialize_get_b2b_tax_invoice_popup_url_response
from portone_server_sdk._generated.b2b.tax_invoice.get_b2b_tax_invoice_print_url_response import GetB2bTaxInvoicePrintUrlResponse, _deserialize_get_b2b_tax_invoice_print_url_response, _serialize_get_b2b_tax_invoice_print_url_response
from portone_server_sdk._generated.b2b.tax_invoice.get_b2b_tax_invoices_body_filter import GetB2bTaxInvoicesBodyFilter, _deserialize_get_b2b_tax_invoices_body_filter, _serialize_get_b2b_tax_invoices_body_filter
from portone_server_sdk._generated.b2b.tax_invoice.get_b2b_tax_invoices_response import GetB2bTaxInvoicesResponse, _deserialize_get_b2b_tax_invoices_response, _serialize_get_b2b_tax_invoices_response
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.b2b.tax_invoice.issue_b2b_tax_invoice_response import IssueB2bTaxInvoiceResponse, _deserialize_issue_b2b_tax_invoice_response, _serialize_issue_b2b_tax_invoice_response
from portone_server_sdk._generated.b2b.tax_invoice.refuse_b2b_tax_invoice_request_response import RefuseB2bTaxInvoiceRequestResponse, _deserialize_refuse_b2b_tax_invoice_request_response, _serialize_refuse_b2b_tax_invoice_request_response
from portone_server_sdk._generated.b2b.tax_invoice.request_b2b_tax_invoice_response import RequestB2bTaxInvoiceResponse, _deserialize_request_b2b_tax_invoice_response, _serialize_request_b2b_tax_invoice_response
from portone_server_sdk._generated.b2b.tax_invoice.request_b2b_tax_invoice_reverse_issuance_response import RequestB2bTaxInvoiceReverseIssuanceResponse, _deserialize_request_b2b_tax_invoice_reverse_issuance_response, _serialize_request_b2b_tax_invoice_reverse_issuance_response
from portone_server_sdk._generated.b2b.tax_invoice.send_to_nts_b2b_tax_invoice_response import SendToNtsB2bTaxInvoiceResponse, _deserialize_send_to_nts_b2b_tax_invoice_response, _serialize_send_to_nts_b2b_tax_invoice_response
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from portone_server_sdk._generated.b2b.tax_invoice.update_b2b_tax_invoice_draft_response import UpdateB2bTaxInvoiceDraftResponse, _deserialize_update_b2b_tax_invoice_draft_response, _serialize_update_b2b_tax_invoice_draft_response
from portone_server_sdk._generated import errors
class TaxInvoiceClient:
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
    def request_b2b_tax_invoice_reverse_issuance(
        self,
        *,
        test: Optional[bool] = None,
        tax_invoice: B2bTaxInvoiceInput,
        memo: Optional[str] = None,
        modification: Optional[B2bTaxInvoiceModificationCreateBody] = None,
    ) -> RequestB2bTaxInvoiceReverseIssuanceResponse:
        """세금계산서 역발행 즉시 요청

        공급자에게 세금계산서 역발행을 즉시 요청합니다. 임시저장 API와 역발행 요청 API 기능을 한 번의 프로세스로 처리합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            tax_invoice (B2bTaxInvoiceInput):
                세금계산서 생성 요청 정보
            memo (str, optional):
                메모
            modification (B2bTaxInvoiceModificationCreateBody, optional):
                수정 세금계산서 입력 정보


        Raises:
            B2BCannotChangeTaxTypeError: 세금계산서 과세 유형을 수정할 수 없는 경우
                세금계산서 과세 유형을 수정할 수 없는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bIdAlreadyExistsError: ID가 이미 사용중인 경우
                ID가 이미 사용중인 경우
            B2bModificationNotProvidedError: 세금계산서 수정 입력 정보를 찾을 수 없는 경우
                세금계산서 수정 입력 정보를 찾을 수 없는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bOriginalTaxInvoiceNotFoundError: 원본 세금계산서가 존재하지 않은 경우
                원본 세금계산서가 존재하지 않은 경우
            B2bRecipientNotFoundError: 공급받는자가 존재하지 않은 경우
                공급받는자가 존재하지 않은 경우
            B2bSupplierNotFoundError: 공급자가 존재하지 않은 경우
                공급자가 존재하지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError: 세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
                세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
            B2BTaxInvoiceStatusNotSendingCompletedError: 원본 세금계산서가 전송완료 상태가 아닌 경우
                원본 세금계산서가 전송완료 상태가 아닌 경우
            B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError: 세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
                세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
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
        request_body["taxInvoice"] = _serialize_b2b_tax_invoice_input(tax_invoice),
        if memo is not None:
            request_body["memo"] = memo,
        if modification is not None:
            request_body["modification"] = _serialize_b2b_tax_invoice_modification_create_body(modification),
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/request-reverse-issuance",
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
            if error_type == "B2B_CANNOT_CHANGE_TAX_TYPE":
                raise errors.B2BCannotChangeTaxTypeError(_deserialize_b2b_cannot_change_tax_type_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_ID_ALREADY_EXISTS":
                raise errors.B2bIdAlreadyExistsError(_deserialize_b2b_id_already_exists_error(error_response))
            if error_type == "B2B_MODIFICATION_NOT_PROVIDED":
                raise errors.B2bModificationNotProvidedError(_deserialize_b2b_modification_not_provided_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bOriginalTaxInvoiceNotFoundError(_deserialize_b2b_original_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_RECIPIENT_NOT_FOUND":
                raise errors.B2bRecipientNotFoundError(_deserialize_b2b_recipient_not_found_error(error_response))
            if error_type == "B2B_SUPPLIER_NOT_FOUND":
                raise errors.B2bSupplierNotFoundError(_deserialize_b2b_supplier_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_RECIPIENT_DOCUMENT_KEY_ALREADY_USED":
                raise errors.B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError(_deserialize_b2b_tax_invoice_recipient_document_key_already_used_error(error_response))
            if error_type == "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED":
                raise errors.B2BTaxInvoiceStatusNotSendingCompletedError(_deserialize_b2b_tax_invoice_status_not_sending_completed_error(error_response))
            if error_type == "B2B_TAX_INVOICE_SUPPLIER_DOCUMENT_KEY_ALREADY_USED":
                raise errors.B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError(_deserialize_b2b_tax_invoice_supplier_document_key_already_used_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_request_b2b_tax_invoice_reverse_issuance_response(response.json())
    async def request_b2b_tax_invoice_reverse_issuance_async(
        self,
        *,
        test: Optional[bool] = None,
        tax_invoice: B2bTaxInvoiceInput,
        memo: Optional[str] = None,
        modification: Optional[B2bTaxInvoiceModificationCreateBody] = None,
    ) -> RequestB2bTaxInvoiceReverseIssuanceResponse:
        """세금계산서 역발행 즉시 요청

        공급자에게 세금계산서 역발행을 즉시 요청합니다. 임시저장 API와 역발행 요청 API 기능을 한 번의 프로세스로 처리합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            tax_invoice (B2bTaxInvoiceInput):
                세금계산서 생성 요청 정보
            memo (str, optional):
                메모
            modification (B2bTaxInvoiceModificationCreateBody, optional):
                수정 세금계산서 입력 정보


        Raises:
            B2BCannotChangeTaxTypeError: 세금계산서 과세 유형을 수정할 수 없는 경우
                세금계산서 과세 유형을 수정할 수 없는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bIdAlreadyExistsError: ID가 이미 사용중인 경우
                ID가 이미 사용중인 경우
            B2bModificationNotProvidedError: 세금계산서 수정 입력 정보를 찾을 수 없는 경우
                세금계산서 수정 입력 정보를 찾을 수 없는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bOriginalTaxInvoiceNotFoundError: 원본 세금계산서가 존재하지 않은 경우
                원본 세금계산서가 존재하지 않은 경우
            B2bRecipientNotFoundError: 공급받는자가 존재하지 않은 경우
                공급받는자가 존재하지 않은 경우
            B2bSupplierNotFoundError: 공급자가 존재하지 않은 경우
                공급자가 존재하지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError: 세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
                세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
            B2BTaxInvoiceStatusNotSendingCompletedError: 원본 세금계산서가 전송완료 상태가 아닌 경우
                원본 세금계산서가 전송완료 상태가 아닌 경우
            B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError: 세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
                세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
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
        request_body["taxInvoice"] = _serialize_b2b_tax_invoice_input(tax_invoice),
        if memo is not None:
            request_body["memo"] = memo,
        if modification is not None:
            request_body["modification"] = _serialize_b2b_tax_invoice_modification_create_body(modification),
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/request-reverse-issuance",
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
            if error_type == "B2B_CANNOT_CHANGE_TAX_TYPE":
                raise errors.B2BCannotChangeTaxTypeError(_deserialize_b2b_cannot_change_tax_type_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_ID_ALREADY_EXISTS":
                raise errors.B2bIdAlreadyExistsError(_deserialize_b2b_id_already_exists_error(error_response))
            if error_type == "B2B_MODIFICATION_NOT_PROVIDED":
                raise errors.B2bModificationNotProvidedError(_deserialize_b2b_modification_not_provided_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bOriginalTaxInvoiceNotFoundError(_deserialize_b2b_original_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_RECIPIENT_NOT_FOUND":
                raise errors.B2bRecipientNotFoundError(_deserialize_b2b_recipient_not_found_error(error_response))
            if error_type == "B2B_SUPPLIER_NOT_FOUND":
                raise errors.B2bSupplierNotFoundError(_deserialize_b2b_supplier_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_RECIPIENT_DOCUMENT_KEY_ALREADY_USED":
                raise errors.B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError(_deserialize_b2b_tax_invoice_recipient_document_key_already_used_error(error_response))
            if error_type == "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED":
                raise errors.B2BTaxInvoiceStatusNotSendingCompletedError(_deserialize_b2b_tax_invoice_status_not_sending_completed_error(error_response))
            if error_type == "B2B_TAX_INVOICE_SUPPLIER_DOCUMENT_KEY_ALREADY_USED":
                raise errors.B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError(_deserialize_b2b_tax_invoice_supplier_document_key_already_used_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_request_b2b_tax_invoice_reverse_issuance_response(response.json())
    def get_b2b_tax_invoice(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> B2bTaxInvoice:
        """세금 계산서 조회

        등록된 세금 계산서를 세금계산서 아이디로 조회합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    async def get_b2b_tax_invoice_async(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> B2bTaxInvoice:
        """세금 계산서 조회

        등록된 세금 계산서를 세금계산서 아이디로 조회합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_b2b_tax_invoice(response.json())
    def delete_b2b_tax_invoice(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> DeleteB2bTaxInvoiceResponse:
        """세금계산서 삭제

        세금계산서를 삭제합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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

                삭제 가능한 상태는 `DRAFTED`, `ISSUE_REFUSED`, `REQUEST_CANCELLED_BY_RECIPIENT`, `ISSUE_CANCELLED_BY_SUPPLIER`, `SENDING_FAILED` 입니다.
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}",
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
            if error_type == "B2B_TAX_INVOICE_NON_DELETABLE_STATUS":
                raise errors.B2bTaxInvoiceNonDeletableStatusError(_deserialize_b2b_tax_invoice_non_deletable_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_delete_b2b_tax_invoice_response(response.json())
    async def delete_b2b_tax_invoice_async(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> DeleteB2bTaxInvoiceResponse:
        """세금계산서 삭제

        세금계산서를 삭제합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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

                삭제 가능한 상태는 `DRAFTED`, `ISSUE_REFUSED`, `REQUEST_CANCELLED_BY_RECIPIENT`, `ISSUE_CANCELLED_BY_SUPPLIER`, `SENDING_FAILED` 입니다.
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}",
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
            if error_type == "B2B_TAX_INVOICE_NON_DELETABLE_STATUS":
                raise errors.B2bTaxInvoiceNonDeletableStatusError(_deserialize_b2b_tax_invoice_non_deletable_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_delete_b2b_tax_invoice_response(response.json())
    def issue_b2b_tax_invoice(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
        memo: Optional[str] = None,
        email_subject: Optional[str] = None,
    ) -> IssueB2bTaxInvoiceResponse:
        """세금계산서 발행 승인

        역발행의 경우 역발행요청(REQUESTED) 상태, 정발행의 경우 임시저장(DRAFTED) 상태의 세금계산서에 대해 발행을 승인합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
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
            B2bTaxInvoiceNoSupplierDocumentKeyError: 세금계산서에 공급자 문서 번호가 기입되지 않은 경우
                세금계산서에 공급자 문서 번호가 기입되지 않은 경우
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
        if memo is not None:
            request_body["memo"] = memo,
        if email_subject is not None:
            request_body["emailSubject"] = email_subject,
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/issue",
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
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
                raise errors.B2bTaxInvoiceNotRequestedStatusError(_deserialize_b2b_tax_invoice_not_requested_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_SUPPLIER_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoSupplierDocumentKeyError(_deserialize_b2b_tax_invoice_no_supplier_document_key_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_issue_b2b_tax_invoice_response(response.json())
    async def issue_b2b_tax_invoice_async(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
        memo: Optional[str] = None,
        email_subject: Optional[str] = None,
    ) -> IssueB2bTaxInvoiceResponse:
        """세금계산서 발행 승인

        역발행의 경우 역발행요청(REQUESTED) 상태, 정발행의 경우 임시저장(DRAFTED) 상태의 세금계산서에 대해 발행을 승인합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
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
            B2bTaxInvoiceNoSupplierDocumentKeyError: 세금계산서에 공급자 문서 번호가 기입되지 않은 경우
                세금계산서에 공급자 문서 번호가 기입되지 않은 경우
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
        if memo is not None:
            request_body["memo"] = memo,
        if email_subject is not None:
            request_body["emailSubject"] = email_subject,
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/issue",
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
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
                raise errors.B2bTaxInvoiceNotRequestedStatusError(_deserialize_b2b_tax_invoice_not_requested_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_SUPPLIER_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoSupplierDocumentKeyError(_deserialize_b2b_tax_invoice_no_supplier_document_key_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_issue_b2b_tax_invoice_response(response.json())
    def send_to_nts_b2b_tax_invoice(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> SendToNtsB2bTaxInvoiceResponse:
        """세금계산서 국세청 즉시 전송

        발행이 완료된 세금계산서를 국세청에 즉시 전송합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
            B2bTaxInvoiceNotIssuedStatusError: 세금계산서가 발행된(ISSUED) 상태가 아닌 경우
                세금계산서가 발행된(ISSUED) 상태가 아닌 경우
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/send-to-nts",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_ISSUED_STATUS":
                raise errors.B2bTaxInvoiceNotIssuedStatusError(_deserialize_b2b_tax_invoice_not_issued_status_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_send_to_nts_b2b_tax_invoice_response(response.json())
    async def send_to_nts_b2b_tax_invoice_async(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> SendToNtsB2bTaxInvoiceResponse:
        """세금계산서 국세청 즉시 전송

        발행이 완료된 세금계산서를 국세청에 즉시 전송합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
            B2bTaxInvoiceNotIssuedStatusError: 세금계산서가 발행된(ISSUED) 상태가 아닌 경우
                세금계산서가 발행된(ISSUED) 상태가 아닌 경우
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/send-to-nts",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_ISSUED_STATUS":
                raise errors.B2bTaxInvoiceNotIssuedStatusError(_deserialize_b2b_tax_invoice_not_issued_status_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_send_to_nts_b2b_tax_invoice_response(response.json())
    def cancel_b2b_tax_invoice_request(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
        memo: Optional[str] = None,
    ) -> CancelB2bTaxInvoiceRequestResponse:
        """세금계산서 역발행 요청 취소 (공급받는자에 의한 취소)

        공급자가 세금계산서 발행을 승인하기 전에 공급받는자가 해당 역발행 요청을 취소합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
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
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/cancel-request",
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
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
                raise errors.B2bTaxInvoiceNotRequestedStatusError(_deserialize_b2b_tax_invoice_not_requested_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoRecipientDocumentKeyError(_deserialize_b2b_tax_invoice_no_recipient_document_key_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_cancel_b2b_tax_invoice_request_response(response.json())
    async def cancel_b2b_tax_invoice_request_async(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
        memo: Optional[str] = None,
    ) -> CancelB2bTaxInvoiceRequestResponse:
        """세금계산서 역발행 요청 취소 (공급받는자에 의한 취소)

        공급자가 세금계산서 발행을 승인하기 전에 공급받는자가 해당 역발행 요청을 취소합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
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
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/cancel-request",
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
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
                raise errors.B2bTaxInvoiceNotRequestedStatusError(_deserialize_b2b_tax_invoice_not_requested_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoRecipientDocumentKeyError(_deserialize_b2b_tax_invoice_no_recipient_document_key_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_cancel_b2b_tax_invoice_request_response(response.json())
    def cancel_b2b_tax_invoice_issuance(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
        memo: Optional[str] = None,
    ) -> CancelB2bTaxInvoiceIssuanceResponse:
        """세금계산서 역발행 취소 (공급자에 의한 취소)

        발행 완료된 세금계산서를 공급자가 국세청 전송 전에 취소합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            memo (str, optional):
                메모


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotIssuedStatusError: 세금계산서가 발행된(ISSUED) 상태가 아닌 경우
                세금계산서가 발행된(ISSUED) 상태가 아닌 경우
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
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/cancel-issuance",
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
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_ISSUED_STATUS":
                raise errors.B2bTaxInvoiceNotIssuedStatusError(_deserialize_b2b_tax_invoice_not_issued_status_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_cancel_b2b_tax_invoice_issuance_response(response.json())
    async def cancel_b2b_tax_invoice_issuance_async(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
        memo: Optional[str] = None,
    ) -> CancelB2bTaxInvoiceIssuanceResponse:
        """세금계산서 역발행 취소 (공급자에 의한 취소)

        발행 완료된 세금계산서를 공급자가 국세청 전송 전에 취소합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            memo (str, optional):
                메모


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotIssuedStatusError: 세금계산서가 발행된(ISSUED) 상태가 아닌 경우
                세금계산서가 발행된(ISSUED) 상태가 아닌 경우
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
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/cancel-issuance",
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
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_ISSUED_STATUS":
                raise errors.B2bTaxInvoiceNotIssuedStatusError(_deserialize_b2b_tax_invoice_not_issued_status_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_cancel_b2b_tax_invoice_issuance_response(response.json())
    def refuse_b2b_tax_invoice_request(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
        memo: Optional[str] = None,
    ) -> RefuseB2bTaxInvoiceRequestResponse:
        """세금계산서 역발행 요청 거부

        공급자가 공급받는자로부터 요청받은 세금계산서 역발행 건을 거부합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
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
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/refuse-request",
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
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
                raise errors.B2bTaxInvoiceNotRequestedStatusError(_deserialize_b2b_tax_invoice_not_requested_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_SUPPLIER_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoSupplierDocumentKeyError(_deserialize_b2b_tax_invoice_no_supplier_document_key_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_refuse_b2b_tax_invoice_request_response(response.json())
    async def refuse_b2b_tax_invoice_request_async(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
        memo: Optional[str] = None,
    ) -> RefuseB2bTaxInvoiceRequestResponse:
        """세금계산서 역발행 요청 거부

        공급자가 공급받는자로부터 요청받은 세금계산서 역발행 건을 거부합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
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
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/refuse-request",
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
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
                raise errors.B2bTaxInvoiceNotRequestedStatusError(_deserialize_b2b_tax_invoice_not_requested_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_SUPPLIER_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoSupplierDocumentKeyError(_deserialize_b2b_tax_invoice_no_supplier_document_key_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_refuse_b2b_tax_invoice_request_response(response.json())
    def get_b2b_tax_invoices(
        self,
        *,
        test: Optional[bool] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
        filter: Optional[GetB2bTaxInvoicesBodyFilter] = None,
    ) -> GetB2bTaxInvoicesResponse:
        """세금 계산서 다건조회

        조회 기간 내 등록된 세금 계산서를 다건 조회합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            page_number (int, optional):
                페이지 번호

                0부터 시작하는 페이지 번호. 기본 값은 0.
            page_size (int, optional):
                페이지 크기

                각 페이지 당 포함할 객체 수. 기본 값은 500이며 최대 1000까지 요청가능합니다.
            filter (GetB2bTaxInvoicesBodyFilter, optional):
                필터


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
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
        if test is not None:
            request_body["test"] = test,
        if page_number is not None:
            request_body["pageNumber"] = page_number,
        if page_size is not None:
            request_body["pageSize"] = page_size,
        if filter is not None:
            request_body["filter"] = _serialize_get_b2b_tax_invoices_body_filter(filter),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b/tax-invoices",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoices_response(response.json())
    async def get_b2b_tax_invoices_async(
        self,
        *,
        test: Optional[bool] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
        filter: Optional[GetB2bTaxInvoicesBodyFilter] = None,
    ) -> GetB2bTaxInvoicesResponse:
        """세금 계산서 다건조회

        조회 기간 내 등록된 세금 계산서를 다건 조회합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            page_number (int, optional):
                페이지 번호

                0부터 시작하는 페이지 번호. 기본 값은 0.
            page_size (int, optional):
                페이지 크기

                각 페이지 당 포함할 객체 수. 기본 값은 500이며 최대 1000까지 요청가능합니다.
            filter (GetB2bTaxInvoicesBodyFilter, optional):
                필터


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
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
        if test is not None:
            request_body["test"] = test,
        if page_number is not None:
            request_body["pageNumber"] = page_number,
        if page_size is not None:
            request_body["pageSize"] = page_size,
        if filter is not None:
            request_body["filter"] = _serialize_get_b2b_tax_invoices_body_filter(filter),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b/tax-invoices",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoices_response(response.json())
    def get_b2b_tax_invoice_popup_url(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        include_menu: Optional[bool] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicePopupUrlResponse:
        """세금 계산서 팝업 URL 조회

        등록된 세금 계산서 팝업 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if include_menu is not None:
            query.append(("includeMenu", include_menu))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/popup-url",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_popup_url_response(response.json())
    async def get_b2b_tax_invoice_popup_url_async(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        include_menu: Optional[bool] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicePopupUrlResponse:
        """세금 계산서 팝업 URL 조회

        등록된 세금 계산서 팝업 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if include_menu is not None:
            query.append(("includeMenu", include_menu))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/popup-url",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_popup_url_response(response.json())
    def get_b2b_tax_invoice_print_url(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicePrintUrlResponse:
        """세금 계산서 프린트 URL 조회

        등록된 세금 계산서 프린트 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/print-url",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_print_url_response(response.json())
    async def get_b2b_tax_invoice_print_url_async(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicePrintUrlResponse:
        """세금 계산서 프린트 URL 조회

        등록된 세금 계산서 프린트 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/print-url",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_print_url_response(response.json())
    def get_b2b_tax_invoice_pdf_download_url(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicePdfDownloadUrlResponse:
        """세금 계산서 PDF 다운로드 URL 조회

        등록된 세금 계산서 PDF 다운로드 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/pdf-download-url",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_pdf_download_url_response(response.json())
    async def get_b2b_tax_invoice_pdf_download_url_async(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoicePdfDownloadUrlResponse:
        """세금 계산서 PDF 다운로드 URL 조회

        등록된 세금 계산서 PDF 다운로드 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/pdf-download-url",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_pdf_download_url_response(response.json())
    def update_b2b_tax_invoice_draft(
        self,
        *,
        test: Optional[bool] = None,
        brn: Optional[str] = None,
        tax_invoice_key: str,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        tax_invoice: B2bTaxInvoiceInput,
        modification: Optional[B2bTaxInvoiceModificationUpdateBody] = None,
        memo: Optional[str] = None,
    ) -> UpdateB2bTaxInvoiceDraftResponse:
        """세금계산서 임시저장 수정

        임시 저장된 세금계산서를 수정합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str, optional):
                사업자등록번호

                taxInvoiceKeyType이 TAX_INVOICE_ID가 아닌 경우 필수 값입니다.
            tax_invoice_key (str):
                세금계산서 문서 번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            tax_invoice (B2bTaxInvoiceInput):
                세금계산서 임시저장 수정 정보
            modification (B2bTaxInvoiceModificationUpdateBody, optional):
                수정 세금계산서 입력 정보
            memo (str, optional):
                메모


        Raises:
            B2BCannotChangeTaxTypeError: 세금계산서 과세 유형을 수정할 수 없는 경우
                세금계산서 과세 유형을 수정할 수 없는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bIdAlreadyExistsError: ID가 이미 사용중인 경우
                ID가 이미 사용중인 경우
            B2bModificationNotProvidedError: 세금계산서 수정 입력 정보를 찾을 수 없는 경우
                세금계산서 수정 입력 정보를 찾을 수 없는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bOriginalTaxInvoiceNotFoundError: 원본 세금계산서가 존재하지 않은 경우
                원본 세금계산서가 존재하지 않은 경우
            B2bRecipientNotFoundError: 공급받는자가 존재하지 않은 경우
                공급받는자가 존재하지 않은 경우
            B2bSupplierNotFoundError: 공급자가 존재하지 않은 경우
                공급자가 존재하지 않은 경우
            B2bTaxInvoiceNotDraftedStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError: 세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
                세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
            B2BTaxInvoiceStatusNotSendingCompletedError: 원본 세금계산서가 전송완료 상태가 아닌 경우
                원본 세금계산서가 전송완료 상태가 아닌 경우
            B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError: 세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
                세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
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
        if brn is not None:
            request_body["brn"] = brn,
        request_body["taxInvoiceKey"] = tax_invoice_key,
        if tax_invoice_key_type is not None:
            request_body["taxInvoiceKeyType"] = _serialize_b2b_tax_invoice_key_type(tax_invoice_key_type),
        request_body["taxInvoice"] = _serialize_b2b_tax_invoice_input(tax_invoice),
        if modification is not None:
            request_body["modification"] = _serialize_b2b_tax_invoice_modification_update_body(modification),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "PUT",
            f"{self._base_url}/b2b/tax-invoices/draft",
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
            if error_type == "B2B_CANNOT_CHANGE_TAX_TYPE":
                raise errors.B2BCannotChangeTaxTypeError(_deserialize_b2b_cannot_change_tax_type_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_ID_ALREADY_EXISTS":
                raise errors.B2bIdAlreadyExistsError(_deserialize_b2b_id_already_exists_error(error_response))
            if error_type == "B2B_MODIFICATION_NOT_PROVIDED":
                raise errors.B2bModificationNotProvidedError(_deserialize_b2b_modification_not_provided_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bOriginalTaxInvoiceNotFoundError(_deserialize_b2b_original_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_RECIPIENT_NOT_FOUND":
                raise errors.B2bRecipientNotFoundError(_deserialize_b2b_recipient_not_found_error(error_response))
            if error_type == "B2B_SUPPLIER_NOT_FOUND":
                raise errors.B2bSupplierNotFoundError(_deserialize_b2b_supplier_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_DRAFTED_STATUS":
                raise errors.B2bTaxInvoiceNotDraftedStatusError(_deserialize_b2b_tax_invoice_not_drafted_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_RECIPIENT_DOCUMENT_KEY_ALREADY_USED":
                raise errors.B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError(_deserialize_b2b_tax_invoice_recipient_document_key_already_used_error(error_response))
            if error_type == "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED":
                raise errors.B2BTaxInvoiceStatusNotSendingCompletedError(_deserialize_b2b_tax_invoice_status_not_sending_completed_error(error_response))
            if error_type == "B2B_TAX_INVOICE_SUPPLIER_DOCUMENT_KEY_ALREADY_USED":
                raise errors.B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError(_deserialize_b2b_tax_invoice_supplier_document_key_already_used_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_update_b2b_tax_invoice_draft_response(response.json())
    async def update_b2b_tax_invoice_draft_async(
        self,
        *,
        test: Optional[bool] = None,
        brn: Optional[str] = None,
        tax_invoice_key: str,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        tax_invoice: B2bTaxInvoiceInput,
        modification: Optional[B2bTaxInvoiceModificationUpdateBody] = None,
        memo: Optional[str] = None,
    ) -> UpdateB2bTaxInvoiceDraftResponse:
        """세금계산서 임시저장 수정

        임시 저장된 세금계산서를 수정합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            brn (str, optional):
                사업자등록번호

                taxInvoiceKeyType이 TAX_INVOICE_ID가 아닌 경우 필수 값입니다.
            tax_invoice_key (str):
                세금계산서 문서 번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
            tax_invoice (B2bTaxInvoiceInput):
                세금계산서 임시저장 수정 정보
            modification (B2bTaxInvoiceModificationUpdateBody, optional):
                수정 세금계산서 입력 정보
            memo (str, optional):
                메모


        Raises:
            B2BCannotChangeTaxTypeError: 세금계산서 과세 유형을 수정할 수 없는 경우
                세금계산서 과세 유형을 수정할 수 없는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bIdAlreadyExistsError: ID가 이미 사용중인 경우
                ID가 이미 사용중인 경우
            B2bModificationNotProvidedError: 세금계산서 수정 입력 정보를 찾을 수 없는 경우
                세금계산서 수정 입력 정보를 찾을 수 없는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bOriginalTaxInvoiceNotFoundError: 원본 세금계산서가 존재하지 않은 경우
                원본 세금계산서가 존재하지 않은 경우
            B2bRecipientNotFoundError: 공급받는자가 존재하지 않은 경우
                공급받는자가 존재하지 않은 경우
            B2bSupplierNotFoundError: 공급자가 존재하지 않은 경우
                공급자가 존재하지 않은 경우
            B2bTaxInvoiceNotDraftedStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError: 세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
                세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
            B2BTaxInvoiceStatusNotSendingCompletedError: 원본 세금계산서가 전송완료 상태가 아닌 경우
                원본 세금계산서가 전송완료 상태가 아닌 경우
            B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError: 세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
                세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
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
        if brn is not None:
            request_body["brn"] = brn,
        request_body["taxInvoiceKey"] = tax_invoice_key,
        if tax_invoice_key_type is not None:
            request_body["taxInvoiceKeyType"] = _serialize_b2b_tax_invoice_key_type(tax_invoice_key_type),
        request_body["taxInvoice"] = _serialize_b2b_tax_invoice_input(tax_invoice),
        if modification is not None:
            request_body["modification"] = _serialize_b2b_tax_invoice_modification_update_body(modification),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "PUT",
            f"{self._base_url}/b2b/tax-invoices/draft",
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
            if error_type == "B2B_CANNOT_CHANGE_TAX_TYPE":
                raise errors.B2BCannotChangeTaxTypeError(_deserialize_b2b_cannot_change_tax_type_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_ID_ALREADY_EXISTS":
                raise errors.B2bIdAlreadyExistsError(_deserialize_b2b_id_already_exists_error(error_response))
            if error_type == "B2B_MODIFICATION_NOT_PROVIDED":
                raise errors.B2bModificationNotProvidedError(_deserialize_b2b_modification_not_provided_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bOriginalTaxInvoiceNotFoundError(_deserialize_b2b_original_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_RECIPIENT_NOT_FOUND":
                raise errors.B2bRecipientNotFoundError(_deserialize_b2b_recipient_not_found_error(error_response))
            if error_type == "B2B_SUPPLIER_NOT_FOUND":
                raise errors.B2bSupplierNotFoundError(_deserialize_b2b_supplier_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_DRAFTED_STATUS":
                raise errors.B2bTaxInvoiceNotDraftedStatusError(_deserialize_b2b_tax_invoice_not_drafted_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_RECIPIENT_DOCUMENT_KEY_ALREADY_USED":
                raise errors.B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError(_deserialize_b2b_tax_invoice_recipient_document_key_already_used_error(error_response))
            if error_type == "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED":
                raise errors.B2BTaxInvoiceStatusNotSendingCompletedError(_deserialize_b2b_tax_invoice_status_not_sending_completed_error(error_response))
            if error_type == "B2B_TAX_INVOICE_SUPPLIER_DOCUMENT_KEY_ALREADY_USED":
                raise errors.B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError(_deserialize_b2b_tax_invoice_supplier_document_key_already_used_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_update_b2b_tax_invoice_draft_response(response.json())
    def draft_b2b_tax_invoice(
        self,
        *,
        test: Optional[bool] = None,
        tax_invoice: B2bTaxInvoiceInput,
        modification: Optional[B2bTaxInvoiceModificationCreateBody] = None,
        memo: Optional[str] = None,
    ) -> DraftB2bTaxInvoiceResponse:
        """세금계산서 임시 저장

        세금계산서 임시 저장을 요청합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            tax_invoice (B2bTaxInvoiceInput):
                세금계산서 생성 요청 정보
            modification (B2bTaxInvoiceModificationCreateBody, optional):
                수정 세금계산서 입력 정보
            memo (str, optional):
                메모


        Raises:
            B2BCannotChangeTaxTypeError: 세금계산서 과세 유형을 수정할 수 없는 경우
                세금계산서 과세 유형을 수정할 수 없는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bIdAlreadyExistsError: ID가 이미 사용중인 경우
                ID가 이미 사용중인 경우
            B2bModificationNotProvidedError: 세금계산서 수정 입력 정보를 찾을 수 없는 경우
                세금계산서 수정 입력 정보를 찾을 수 없는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bOriginalTaxInvoiceNotFoundError: 원본 세금계산서가 존재하지 않은 경우
                원본 세금계산서가 존재하지 않은 경우
            B2bRecipientNotFoundError: 공급받는자가 존재하지 않은 경우
                공급받는자가 존재하지 않은 경우
            B2bSupplierNotFoundError: 공급자가 존재하지 않은 경우
                공급자가 존재하지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError: 세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
                세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
            B2BTaxInvoiceStatusNotSendingCompletedError: 원본 세금계산서가 전송완료 상태가 아닌 경우
                원본 세금계산서가 전송완료 상태가 아닌 경우
            B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError: 세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
                세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
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
        request_body["taxInvoice"] = _serialize_b2b_tax_invoice_input(tax_invoice),
        if modification is not None:
            request_body["modification"] = _serialize_b2b_tax_invoice_modification_create_body(modification),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/draft",
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
            if error_type == "B2B_CANNOT_CHANGE_TAX_TYPE":
                raise errors.B2BCannotChangeTaxTypeError(_deserialize_b2b_cannot_change_tax_type_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_ID_ALREADY_EXISTS":
                raise errors.B2bIdAlreadyExistsError(_deserialize_b2b_id_already_exists_error(error_response))
            if error_type == "B2B_MODIFICATION_NOT_PROVIDED":
                raise errors.B2bModificationNotProvidedError(_deserialize_b2b_modification_not_provided_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bOriginalTaxInvoiceNotFoundError(_deserialize_b2b_original_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_RECIPIENT_NOT_FOUND":
                raise errors.B2bRecipientNotFoundError(_deserialize_b2b_recipient_not_found_error(error_response))
            if error_type == "B2B_SUPPLIER_NOT_FOUND":
                raise errors.B2bSupplierNotFoundError(_deserialize_b2b_supplier_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_RECIPIENT_DOCUMENT_KEY_ALREADY_USED":
                raise errors.B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError(_deserialize_b2b_tax_invoice_recipient_document_key_already_used_error(error_response))
            if error_type == "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED":
                raise errors.B2BTaxInvoiceStatusNotSendingCompletedError(_deserialize_b2b_tax_invoice_status_not_sending_completed_error(error_response))
            if error_type == "B2B_TAX_INVOICE_SUPPLIER_DOCUMENT_KEY_ALREADY_USED":
                raise errors.B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError(_deserialize_b2b_tax_invoice_supplier_document_key_already_used_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_draft_b2b_tax_invoice_response(response.json())
    async def draft_b2b_tax_invoice_async(
        self,
        *,
        test: Optional[bool] = None,
        tax_invoice: B2bTaxInvoiceInput,
        modification: Optional[B2bTaxInvoiceModificationCreateBody] = None,
        memo: Optional[str] = None,
    ) -> DraftB2bTaxInvoiceResponse:
        """세금계산서 임시 저장

        세금계산서 임시 저장을 요청합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            tax_invoice (B2bTaxInvoiceInput):
                세금계산서 생성 요청 정보
            modification (B2bTaxInvoiceModificationCreateBody, optional):
                수정 세금계산서 입력 정보
            memo (str, optional):
                메모


        Raises:
            B2BCannotChangeTaxTypeError: 세금계산서 과세 유형을 수정할 수 없는 경우
                세금계산서 과세 유형을 수정할 수 없는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bIdAlreadyExistsError: ID가 이미 사용중인 경우
                ID가 이미 사용중인 경우
            B2bModificationNotProvidedError: 세금계산서 수정 입력 정보를 찾을 수 없는 경우
                세금계산서 수정 입력 정보를 찾을 수 없는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bOriginalTaxInvoiceNotFoundError: 원본 세금계산서가 존재하지 않은 경우
                원본 세금계산서가 존재하지 않은 경우
            B2bRecipientNotFoundError: 공급받는자가 존재하지 않은 경우
                공급받는자가 존재하지 않은 경우
            B2bSupplierNotFoundError: 공급자가 존재하지 않은 경우
                공급자가 존재하지 않은 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError: 세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
                세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우
            B2BTaxInvoiceStatusNotSendingCompletedError: 원본 세금계산서가 전송완료 상태가 아닌 경우
                원본 세금계산서가 전송완료 상태가 아닌 경우
            B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError: 세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
                세금계산서에 공급자 문서 번호가 이미 사용 중인 경우
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
        request_body["taxInvoice"] = _serialize_b2b_tax_invoice_input(tax_invoice),
        if modification is not None:
            request_body["modification"] = _serialize_b2b_tax_invoice_modification_create_body(modification),
        if memo is not None:
            request_body["memo"] = memo,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/draft",
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
            if error_type == "B2B_CANNOT_CHANGE_TAX_TYPE":
                raise errors.B2BCannotChangeTaxTypeError(_deserialize_b2b_cannot_change_tax_type_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_ID_ALREADY_EXISTS":
                raise errors.B2bIdAlreadyExistsError(_deserialize_b2b_id_already_exists_error(error_response))
            if error_type == "B2B_MODIFICATION_NOT_PROVIDED":
                raise errors.B2bModificationNotProvidedError(_deserialize_b2b_modification_not_provided_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bOriginalTaxInvoiceNotFoundError(_deserialize_b2b_original_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_RECIPIENT_NOT_FOUND":
                raise errors.B2bRecipientNotFoundError(_deserialize_b2b_recipient_not_found_error(error_response))
            if error_type == "B2B_SUPPLIER_NOT_FOUND":
                raise errors.B2bSupplierNotFoundError(_deserialize_b2b_supplier_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_RECIPIENT_DOCUMENT_KEY_ALREADY_USED":
                raise errors.B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError(_deserialize_b2b_tax_invoice_recipient_document_key_already_used_error(error_response))
            if error_type == "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED":
                raise errors.B2BTaxInvoiceStatusNotSendingCompletedError(_deserialize_b2b_tax_invoice_status_not_sending_completed_error(error_response))
            if error_type == "B2B_TAX_INVOICE_SUPPLIER_DOCUMENT_KEY_ALREADY_USED":
                raise errors.B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError(_deserialize_b2b_tax_invoice_supplier_document_key_already_used_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_draft_b2b_tax_invoice_response(response.json())
    def request_b2b_tax_invoice(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> RequestB2bTaxInvoiceResponse:
        """세금계산서 역발행 요청

        임시저장(REGISTERED) 상태의 역발행 세금계산서를 공급자에게 발행 요청합니다. 요청이 완료되면 (역)발행대기 상태로 전환됩니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2BCannotChangeTaxTypeError: 세금계산서 과세 유형을 수정할 수 없는 경우
                세금계산서 과세 유형을 수정할 수 없는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bModificationNotProvidedError: 세금계산서 수정 입력 정보를 찾을 수 없는 경우
                세금계산서 수정 입력 정보를 찾을 수 없는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bOriginalTaxInvoiceNotFoundError: 원본 세금계산서가 존재하지 않은 경우
                원본 세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotDraftedStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNoRecipientDocumentKeyError: 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
                세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
            B2BTaxInvoiceStatusNotSendingCompletedError: 원본 세금계산서가 전송완료 상태가 아닌 경우
                원본 세금계산서가 전송완료 상태가 아닌 경우
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/request",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_CANNOT_CHANGE_TAX_TYPE":
                raise errors.B2BCannotChangeTaxTypeError(_deserialize_b2b_cannot_change_tax_type_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MODIFICATION_NOT_PROVIDED":
                raise errors.B2bModificationNotProvidedError(_deserialize_b2b_modification_not_provided_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bOriginalTaxInvoiceNotFoundError(_deserialize_b2b_original_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_DRAFTED_STATUS":
                raise errors.B2bTaxInvoiceNotDraftedStatusError(_deserialize_b2b_tax_invoice_not_drafted_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoRecipientDocumentKeyError(_deserialize_b2b_tax_invoice_no_recipient_document_key_error(error_response))
            if error_type == "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED":
                raise errors.B2BTaxInvoiceStatusNotSendingCompletedError(_deserialize_b2b_tax_invoice_status_not_sending_completed_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_request_b2b_tax_invoice_response(response.json())
    async def request_b2b_tax_invoice_async(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> RequestB2bTaxInvoiceResponse:
        """세금계산서 역발행 요청

        임시저장(REGISTERED) 상태의 역발행 세금계산서를 공급자에게 발행 요청합니다. 요청이 완료되면 (역)발행대기 상태로 전환됩니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.


        Raises:
            B2BCannotChangeTaxTypeError: 세금계산서 과세 유형을 수정할 수 없는 경우
                세금계산서 과세 유형을 수정할 수 없는 경우
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bModificationNotProvidedError: 세금계산서 수정 입력 정보를 찾을 수 없는 경우
                세금계산서 수정 입력 정보를 찾을 수 없는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bOriginalTaxInvoiceNotFoundError: 원본 세금계산서가 존재하지 않은 경우
                원본 세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNotDraftedStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
            B2bTaxInvoiceNoRecipientDocumentKeyError: 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
                세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
            B2BTaxInvoiceStatusNotSendingCompletedError: 원본 세금계산서가 전송완료 상태가 아닌 경우
                원본 세금계산서가 전송완료 상태가 아닌 경우
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/request",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "B2B_CANNOT_CHANGE_TAX_TYPE":
                raise errors.B2BCannotChangeTaxTypeError(_deserialize_b2b_cannot_change_tax_type_error(error_response))
            if error_type == "B2B_EXTERNAL_SERVICE":
                raise errors.B2bExternalServiceError(_deserialize_b2b_external_service_error(error_response))
            if error_type == "B2B_MODIFICATION_NOT_PROVIDED":
                raise errors.B2bModificationNotProvidedError(_deserialize_b2b_modification_not_provided_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bOriginalTaxInvoiceNotFoundError(_deserialize_b2b_original_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_DRAFTED_STATUS":
                raise errors.B2bTaxInvoiceNotDraftedStatusError(_deserialize_b2b_tax_invoice_not_drafted_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY":
                raise errors.B2bTaxInvoiceNoRecipientDocumentKeyError(_deserialize_b2b_tax_invoice_no_recipient_document_key_error(error_response))
            if error_type == "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED":
                raise errors.B2BTaxInvoiceStatusNotSendingCompletedError(_deserialize_b2b_tax_invoice_status_not_sending_completed_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_request_b2b_tax_invoice_response(response.json())
    def create_b2b_file_upload_url(
        self,
        *,
        test: Optional[bool] = None,
        file_name: str,
    ) -> CreateB2bFileUploadUrlPayload:
        """파일 업로드 URL 생성

        S3 파일 업로드를 위한 URL을 생성합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            file_name (str):
                파일 이름


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
        request_body = {}
        request_body["fileName"] = file_name,
        query = []
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b/file-upload-url",
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
        return _deserialize_create_b2b_file_upload_url_payload(response.json())
    async def create_b2b_file_upload_url_async(
        self,
        *,
        test: Optional[bool] = None,
        file_name: str,
    ) -> CreateB2bFileUploadUrlPayload:
        """파일 업로드 URL 생성

        S3 파일 업로드를 위한 URL을 생성합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            file_name (str):
                파일 이름


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
        request_body = {}
        request_body["fileName"] = file_name,
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b/file-upload-url",
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
        return _deserialize_create_b2b_file_upload_url_payload(response.json())
    def attach_b2b_tax_invoice_file(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
        file_id: str,
    ) -> None:
        """세금계산서 파일 첨부

        세금계산서에 파일을 첨부합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            file_id (str):
                파일 아이디


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bFileNotFoundError: 업로드한 파일을 찾을 수 없는 경우
                업로드한 파일을 찾을 수 없는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotDraftedStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
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
        request_body["fileId"] = file_id,
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/attach-file",
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
            if error_type == "B2B_FILE_NOT_FOUND":
                raise errors.B2bFileNotFoundError(_deserialize_b2b_file_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_DRAFTED_STATUS":
                raise errors.B2bTaxInvoiceNotDraftedStatusError(_deserialize_b2b_tax_invoice_not_drafted_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
    async def attach_b2b_tax_invoice_file_async(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
        file_id: str,
    ) -> None:
        """세금계산서 파일 첨부

        세금계산서에 파일을 첨부합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
            test (bool, optional):
                테스트 모드 여부

                true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
            file_id (str):
                파일 아이디


        Raises:
            B2bExternalServiceError: 외부 서비스에서 에러가 발생한 경우
                외부 서비스에서 에러가 발생한 경우
            B2bFileNotFoundError: 업로드한 파일을 찾을 수 없는 경우
                업로드한 파일을 찾을 수 없는 경우
            B2bNotEnabledError: B2B 기능이 활성화되지 않은 경우
                B2B 기능이 활성화되지 않은 경우
            B2bTaxInvoiceNotDraftedStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
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
        request_body["fileId"] = file_id,
        query = []
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/attach-file",
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
            if error_type == "B2B_FILE_NOT_FOUND":
                raise errors.B2bFileNotFoundError(_deserialize_b2b_file_not_found_error(error_response))
            if error_type == "B2B_NOT_ENABLED":
                raise errors.B2bNotEnabledError(_deserialize_b2b_not_enabled_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_DRAFTED_STATUS":
                raise errors.B2bTaxInvoiceNotDraftedStatusError(_deserialize_b2b_tax_invoice_not_drafted_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
    def get_b2b_tax_invoice_attachments(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoiceAttachmentsResponse:
        """세금계산서 첨부파일 목록 조회

        세금계산서에 첨부된 파일 목록을 조회합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "GET",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/attachments",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_attachments_response(response.json())
    async def get_b2b_tax_invoice_attachments_async(
        self,
        *,
        tax_invoice_key: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> GetB2bTaxInvoiceAttachmentsResponse:
        """세금계산서 첨부파일 목록 조회

        세금계산서에 첨부된 파일 목록을 조회합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/attachments",
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
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_b2b_tax_invoice_attachments_response(response.json())
    def delete_b2b_tax_invoice_attachment(
        self,
        *,
        tax_invoice_key: str,
        attachment_id: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> None:
        """세금계산서 첨부파일 삭제

        세금계산서 첨부파일을 삭제합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            attachment_id (str):
                첨부파일 아이디
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
            B2bTaxInvoiceNotDraftedStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/attachments/{attachment_id}",
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
            if error_type == "B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND":
                raise errors.B2bTaxInvoiceAttachmentNotFoundError(_deserialize_b2b_tax_invoice_attachment_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_DRAFTED_STATUS":
                raise errors.B2bTaxInvoiceNotDraftedStatusError(_deserialize_b2b_tax_invoice_not_drafted_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
    async def delete_b2b_tax_invoice_attachment_async(
        self,
        *,
        tax_invoice_key: str,
        attachment_id: str,
        brn: Optional[str] = None,
        tax_invoice_key_type: Optional[B2bTaxInvoiceKeyType] = None,
        test: Optional[bool] = None,
    ) -> None:
        """세금계산서 첨부파일 삭제

        세금계산서 첨부파일을 삭제합니다.

        Args:
            tax_invoice_key (str):
                세금계산서 문서 번호
            attachment_id (str):
                첨부파일 아이디
            brn (str, optional):
                사업자등록번호
            tax_invoice_key_type (B2bTaxInvoiceKeyType, optional):
                문서 번호 유형

                query 파라미터로 전달된 문서번호 유형. 기본 값은 TAX_INVOICE_ID이며 SUPPLIER, RECIPIENT, TAX_INVOICE_ID을 지원합니다.
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
            B2bTaxInvoiceNotDraftedStatusError: 세금계산서가 임시저장 상태가 아닌 경우
                세금계산서가 임시저장 상태가 아닌 경우
            B2bTaxInvoiceNotFoundError: 세금계산서가 존재하지 않은 경우
                세금계산서가 존재하지 않은 경우
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
        if brn is not None:
            query.append(("brn", brn))
        if tax_invoice_key_type is not None:
            query.append(("taxInvoiceKeyType", tax_invoice_key_type))
        if test is not None:
            query.append(("test", test))
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/b2b/tax-invoices/{tax_invoice_key}/attachments/{attachment_id}",
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
            if error_type == "B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND":
                raise errors.B2bTaxInvoiceAttachmentNotFoundError(_deserialize_b2b_tax_invoice_attachment_not_found_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_DRAFTED_STATUS":
                raise errors.B2bTaxInvoiceNotDraftedStatusError(_deserialize_b2b_tax_invoice_not_drafted_status_error(error_response))
            if error_type == "B2B_TAX_INVOICE_NOT_FOUND":
                raise errors.B2bTaxInvoiceNotFoundError(_deserialize_b2b_tax_invoice_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
