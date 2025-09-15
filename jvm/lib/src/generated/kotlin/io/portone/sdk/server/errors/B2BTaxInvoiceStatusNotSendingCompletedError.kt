package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 원본 세금계산서가 전송완료 상태가 아닌 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED")
internal data class B2BTaxInvoiceStatusNotSendingCompletedError(
  override val message: String? = null,
) : DraftB2bTaxInvoiceError.Recognized, IssueB2bTaxInvoiceImmediatelyError.Recognized, RequestB2bTaxInvoiceReverseIssuanceError.Recognized, UpdateB2bTaxInvoiceDraftError.Recognized, requestB2bTaxInvoiceError.Recognized


