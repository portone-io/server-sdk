package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우 */
@Serializable
@SerialName("B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY")
internal data class B2bTaxInvoiceNoRecipientDocumentKeyError(
  override val message: String? = null,
) : CancelB2bTaxInvoiceRequestError.Recognized, requestB2bTaxInvoiceError.Recognized


