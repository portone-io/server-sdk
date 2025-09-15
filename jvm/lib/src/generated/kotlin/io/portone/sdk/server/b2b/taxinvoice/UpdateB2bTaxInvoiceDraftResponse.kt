package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoice
import kotlinx.serialization.Serializable

/** 세금계산서 임시저장 수정 응답 */
@Serializable
public data class UpdateB2bTaxInvoiceDraftResponse(
  val taxInvoice: B2bTaxInvoice,
)


