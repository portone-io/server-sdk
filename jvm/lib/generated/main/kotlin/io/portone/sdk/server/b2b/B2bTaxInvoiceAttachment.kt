package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 세금계산서 첨부파일 */
@Serializable
public data class B2bTaxInvoiceAttachment(
  /** 첨부 파일 아이디 */
  val id: String,
  /** 첨부 파일명 */
  val name: String,
  /** 첨부 일시 */
  val attachedAt: Instant,
)
