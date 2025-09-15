package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoice
import kotlinx.serialization.Serializable

/** 세금계산서 국세청 즉시 전송 응답 */
@Serializable
public data class SendToNtsB2bTaxInvoiceResponse(
  val taxInvoice: B2bTaxInvoice,
)


