package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서 과세 유형을 수정할 수 없는 경우 */
@Serializable
@SerialName("B2B_CANNOT_CHANGE_TAX_TYPE")
internal data class B2BCannotChangeTaxTypeError(
  override val message: String? = null,
) : DraftB2bTaxInvoiceError.Recognized, IssueB2bTaxInvoiceImmediatelyError.Recognized, RequestB2bTaxInvoiceReverseIssuanceError.Recognized, UpdateB2bTaxInvoiceDraftError.Recognized, requestB2bTaxInvoiceError.Recognized


