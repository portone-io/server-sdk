package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서 수정 입력 정보를 찾을 수 없는 경우 */
@Serializable
@SerialName("B2B_MODIFICATION_NOT_PROVIDED")
internal data class B2bModificationNotProvidedError(
  override val message: String? = null,
) : DraftB2bTaxInvoiceError.Recognized, IssueB2bTaxInvoiceImmediatelyError.Recognized, RequestB2bTaxInvoiceReverseIssuanceError.Recognized, UpdateB2bTaxInvoiceDraftError.Recognized, requestB2bTaxInvoiceError.Recognized


