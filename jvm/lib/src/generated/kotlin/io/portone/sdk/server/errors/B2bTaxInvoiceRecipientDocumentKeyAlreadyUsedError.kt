package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_RECIPIENT_DOCUMENT_KEY_ALREADY_USED")
internal data class B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError(
  override val message: String? = null,
) : DraftB2bTaxInvoiceError.Recognized, IssueB2bTaxInvoiceImmediatelyError.Recognized, RequestB2bTaxInvoiceReverseIssuanceError.Recognized, UpdateB2bTaxInvoiceDraftError.Recognized


