package io.portone.sdk.server.b2b.taxinvoice

import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 PDF 다운로드 URL 성공 응답 */
@Serializable
public data class GetB2bTaxInvoicePdfDownloadUrlResponse(
  /** 세금계산서 PDF 다운로드 URL */
  val url: String,
)
