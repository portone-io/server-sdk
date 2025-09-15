package io.portone.sdk.server.b2b.taxinvoice

import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 팝업 URL 성공 응답 */
@Serializable
public data class GetB2bTaxInvoicePopupUrlResponse(
  /** 세금계산서 팝업 URL */
  val url: String,
)


