package io.portone.sdk.server.b2b.taxinvoice

import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 역발행 요청 거부 정보 */
@Serializable
internal data class RefuseB2bTaxInvoiceRequestBody(
  /** 메모 */
  val memo: String? = null,
)
