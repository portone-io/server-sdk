package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서가 역발행 대기 상태가 아닌 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_NOT_REQUESTED_STATUS")
internal data class B2bTaxInvoiceNotRequestedStatusError(
  override val message: String? = null,
) : CancelB2bTaxInvoiceRequestError.Recognized, IssueB2bTaxInvoiceError.Recognized, RefuseB2bTaxInvoiceRequestError.Recognized


