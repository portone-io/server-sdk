package io.portone.sdk.server.b2b.taxinvoice

import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 프린트 URL 성공 응답 */
@Serializable
public data class GetB2bTaxInvoicePrintUrlResponse(
  /** 세금계산서 프린트 URL */
  val url: String,
)


