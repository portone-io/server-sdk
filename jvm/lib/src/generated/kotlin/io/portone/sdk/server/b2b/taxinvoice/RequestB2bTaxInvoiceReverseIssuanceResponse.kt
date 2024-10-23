package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoice
import kotlinx.serialization.Serializable

/** 세금계산서 역발행 즉시 요청 응답 */
@Serializable
public data class RequestB2bTaxInvoiceReverseIssuanceResponse(
  val taxInvoice: B2bTaxInvoice,
)
