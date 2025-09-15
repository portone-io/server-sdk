package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서가 임시저장 완료 상태가 아닌 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_NOT_DRAFTED_STATUS")
internal data class B2bTaxInvoiceNotDraftedStatusError(
  override val message: String? = null,
) : AttachB2bTaxInvoiceFileError.Recognized, DeleteB2bTaxInvoiceAttachmentError.Recognized, IssueB2bTaxInvoiceError.Recognized, UpdateB2bTaxInvoiceDraftError.Recognized, requestB2bTaxInvoiceError.Recognized


