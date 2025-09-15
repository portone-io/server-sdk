package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서가 존재하지 않은 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_NOT_FOUND")
internal data class B2bTaxInvoiceNotFoundError(
  override val message: String? = null,
) : AttachB2bTaxInvoiceFileError.Recognized, CancelB2bTaxInvoiceIssuanceError.Recognized, CancelB2bTaxInvoiceRequestError.Recognized, DeleteB2bTaxInvoiceAttachmentError.Recognized, DeleteB2bTaxInvoiceError.Recognized, DraftB2bTaxInvoiceError.Recognized, GetB2bTaxInvoiceAttachmentsError.Recognized, GetB2bTaxInvoiceError.Recognized, GetB2bTaxInvoicePdfDownloadUrlError.Recognized, GetB2bTaxInvoicePopupUrlError.Recognized, GetB2bTaxInvoicePrintUrlError.Recognized, GetB2bTaxInvoicesError.Recognized, IssueB2bTaxInvoiceError.Recognized, IssueB2bTaxInvoiceImmediatelyError.Recognized, RefuseB2bTaxInvoiceRequestError.Recognized, RequestB2bTaxInvoiceReverseIssuanceError.Recognized, SendToNtsB2bTaxInvoiceError.Recognized, UpdateB2bTaxInvoiceDraftError.Recognized, requestB2bTaxInvoiceError.Recognized


