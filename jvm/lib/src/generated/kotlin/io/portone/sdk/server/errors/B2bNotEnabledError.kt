package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.AttachB2bTaxInvoiceFileError
import io.portone.sdk.server.errors.CancelB2bTaxInvoiceIssuanceError
import io.portone.sdk.server.errors.CancelB2bTaxInvoiceRequestError
import io.portone.sdk.server.errors.CreateB2bTaxInvoiceFileUploadLinkCreateError
import io.portone.sdk.server.errors.DeleteB2bTaxInvoiceAttachmentError
import io.portone.sdk.server.errors.DeleteB2bTaxInvoiceError
import io.portone.sdk.server.errors.GetB2bAccountHolderError
import io.portone.sdk.server.errors.GetB2bCertificateError
import io.portone.sdk.server.errors.GetB2bCertificateRegistrationUrlError
import io.portone.sdk.server.errors.GetB2bCompanyStateError
import io.portone.sdk.server.errors.GetB2bMemberCompanyContactError
import io.portone.sdk.server.errors.GetB2bMemberCompanyError
import io.portone.sdk.server.errors.GetB2bTaxInvoiceAttachmentsError
import io.portone.sdk.server.errors.GetB2bTaxInvoiceError
import io.portone.sdk.server.errors.GetB2bTaxInvoicePdfDownloadUrlError
import io.portone.sdk.server.errors.GetB2bTaxInvoicePopupUrlError
import io.portone.sdk.server.errors.GetB2bTaxInvoicePrintUrlError
import io.portone.sdk.server.errors.GetB2bTaxInvoicesError
import io.portone.sdk.server.errors.IssueB2bTaxInvoiceError
import io.portone.sdk.server.errors.RefuseB2bTaxInvoiceRequestError
import io.portone.sdk.server.errors.RegisterB2bMemberCompanyError
import io.portone.sdk.server.errors.RequestB2bTaxInvoiceRegisterError
import io.portone.sdk.server.errors.RequestB2bTaxInvoiceReverseIssuanceError
import io.portone.sdk.server.errors.UpdateB2bMemberCompanyContactError
import io.portone.sdk.server.errors.UpdateB2bMemberCompanyError
import io.portone.sdk.server.errors.getB2bContactIdExistenceError
import io.portone.sdk.server.errors.requestB2bTaxInvoiceError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** B2B 기능이 활성화되지 않은 경우 */
@Serializable
@SerialName("B2B_NOT_ENABLED")
@ConsistentCopyVisibility
public data class B2bNotEnabledError internal constructor(
  override val message: String? = null,
): AttachB2bTaxInvoiceFileError,
  CancelB2bTaxInvoiceIssuanceError,
  CancelB2bTaxInvoiceRequestError,
  CreateB2bTaxInvoiceFileUploadLinkCreateError,
  DeleteB2bTaxInvoiceAttachmentError,
  DeleteB2bTaxInvoiceError,
  GetB2bAccountHolderError,
  GetB2bCertificateError,
  GetB2bCertificateRegistrationUrlError,
  GetB2bCompanyStateError,
  GetB2bMemberCompanyContactError,
  GetB2bMemberCompanyError,
  GetB2bTaxInvoiceAttachmentsError,
  GetB2bTaxInvoiceError,
  GetB2bTaxInvoicePdfDownloadUrlError,
  GetB2bTaxInvoicePopupUrlError,
  GetB2bTaxInvoicePrintUrlError,
  GetB2bTaxInvoicesError,
  IssueB2bTaxInvoiceError,
  RefuseB2bTaxInvoiceRequestError,
  RegisterB2bMemberCompanyError,
  RequestB2bTaxInvoiceRegisterError,
  RequestB2bTaxInvoiceReverseIssuanceError,
  UpdateB2bMemberCompanyContactError,
  UpdateB2bMemberCompanyError,
  getB2bContactIdExistenceError,
  requestB2bTaxInvoiceError
