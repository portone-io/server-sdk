package io.portone.sdk.server.b2b.taxinvoice

import kotlin.String
import kotlinx.serialization.Serializable

/** 추가 담당자 */
@Serializable
public data class B2bTaxInvoiceAdditionalContact(
  /** 이메일 */
  val email: String,
  /**
   * 성명
   *
   * 최대 100자
   */
  val name: String? = null,
)
