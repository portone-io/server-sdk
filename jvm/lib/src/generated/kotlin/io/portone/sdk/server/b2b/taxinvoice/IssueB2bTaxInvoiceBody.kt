package io.portone.sdk.server.b2b.taxinvoice

import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 발행 승인 정보 */
@Serializable
internal data class IssueB2bTaxInvoiceBody(
  /** 메모 */
  val memo: String? = null,
  /** 이메일 제목 */
  val emailSubject: String? = null,
)


