package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoice
import kotlinx.serialization.Serializable

/** 세금계산서 임시 저장 응답 */
@Serializable
public data class DraftB2bTaxInvoiceResponse(
  val taxInvoice: B2bTaxInvoice,
)
