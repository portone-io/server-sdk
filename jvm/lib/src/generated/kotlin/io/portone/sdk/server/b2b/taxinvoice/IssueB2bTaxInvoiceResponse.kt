package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoice
import kotlinx.serialization.Serializable

/** 세금계산서 발행 승인 응답 */
@Serializable
public data class IssueB2bTaxInvoiceResponse(
  val taxInvoice: B2bTaxInvoice,
)


