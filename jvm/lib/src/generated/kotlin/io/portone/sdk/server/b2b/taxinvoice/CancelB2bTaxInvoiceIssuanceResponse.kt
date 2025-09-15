package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoice
import kotlinx.serialization.Serializable

/** 세금계산서 취소 응답 */
@Serializable
public data class CancelB2bTaxInvoiceIssuanceResponse(
  val taxInvoice: B2bTaxInvoice,
)


