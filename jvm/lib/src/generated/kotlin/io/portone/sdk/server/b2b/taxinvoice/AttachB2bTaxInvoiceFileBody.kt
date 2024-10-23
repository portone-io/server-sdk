package io.portone.sdk.server.b2b.taxinvoice

import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 파일 첨부 정보 */
@Serializable
internal data class AttachB2bTaxInvoiceFileBody(
  /** 파일 아이디 */
  val fileId: String,
)
