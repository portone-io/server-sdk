package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.AttachB2bTaxInvoiceFileError
import io.portone.sdk.server.errors.CancelB2bTaxInvoiceIssuanceError
import io.portone.sdk.server.errors.CancelB2bTaxInvoiceRequestError
import io.portone.sdk.server.errors.CreateB2bFileUploadUrlError
import io.portone.sdk.server.errors.DeleteB2bTaxInvoiceAttachmentError
import io.portone.sdk.server.errors.DeleteB2bTaxInvoiceError
import io.portone.sdk.server.errors.DraftB2bTaxInvoiceError
import io.portone.sdk.server.errors.GetB2bAccountHolderError
import io.portone.sdk.server.errors.GetB2bCertificateError
import io.portone.sdk.server.errors.GetB2bCertificateRegistrationUrlError
import io.portone.sdk.server.errors.GetB2bCompanyStateError
import io.portone.sdk.server.errors.GetB2bContactError
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
import io.portone.sdk.server.errors.RequestB2bTaxInvoiceReverseIssuanceError
import io.portone.sdk.server.errors.SendToNtsB2bTaxInvoiceError
import io.portone.sdk.server.errors.UpdateB2bContactError
import io.portone.sdk.server.errors.UpdateB2bMemberCompanyError
import io.portone.sdk.server.errors.UpdateB2bTaxInvoiceDraftError
import io.portone.sdk.server.errors.ValidateB2bCertificateError
import io.portone.sdk.server.errors.getB2bContactIdExistenceError
import io.portone.sdk.server.errors.requestB2bTaxInvoiceError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 외부 서비스에서 에러가 발생한 경우 */
@Serializable
@SerialName("B2B_EXTERNAL_SERVICE")
@ConsistentCopyVisibility
public data class B2bExternalServiceError internal constructor(
  override val message: String? = null,
): AttachB2bTaxInvoiceFileError,
  CancelB2bTaxInvoiceIssuanceError,
  CancelB2bTaxInvoiceRequestError,
  CreateB2bFileUploadUrlError,
  DeleteB2bTaxInvoiceAttachmentError,
  DeleteB2bTaxInvoiceError,
  DraftB2bTaxInvoiceError,
  GetB2bAccountHolderError,
  GetB2bCertificateError,
  GetB2bCertificateRegistrationUrlError,
  GetB2bCompanyStateError,
  GetB2bContactError,
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
  RequestB2bTaxInvoiceReverseIssuanceError,
  SendToNtsB2bTaxInvoiceError,
  UpdateB2bContactError,
  UpdateB2bMemberCompanyError,
  UpdateB2bTaxInvoiceDraftError,
  ValidateB2bCertificateError,
  getB2bContactIdExistenceError,
  requestB2bTaxInvoiceError
