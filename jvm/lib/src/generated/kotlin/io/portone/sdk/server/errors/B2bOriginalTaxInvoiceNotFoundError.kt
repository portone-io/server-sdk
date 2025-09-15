package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 원본 세금계산서가 존재하지 않은 경우 */
@Serializable
@SerialName("B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND")
internal data class B2bOriginalTaxInvoiceNotFoundError(
  override val message: String? = null,
) : DraftB2bTaxInvoiceError.Recognized, IssueB2bTaxInvoiceImmediatelyError.Recognized, RequestB2bTaxInvoiceReverseIssuanceError.Recognized, UpdateB2bTaxInvoiceDraftError.Recognized, requestB2bTaxInvoiceError.Recognized


