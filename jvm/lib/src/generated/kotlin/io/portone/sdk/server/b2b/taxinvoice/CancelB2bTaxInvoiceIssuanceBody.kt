package io.portone.sdk.server.b2b.taxinvoice

import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 역발행 취소 정보 */
@Serializable
internal data class CancelB2bTaxInvoiceIssuanceBody(
  /** 메모 */
  val memo: String? = null,
)
