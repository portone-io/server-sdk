package io.portone.sdk.server.b2b.taxinvoice

import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 담당자 */
@Serializable
public data class B2bTaxInvoiceContact(
  /** 성명 */
  val name: String? = null,
  /** 부서 */
  val department: String? = null,
  /** 전화번호 */
  val phoneNumber: String? = null,
  /** 휴대전화번호 */
  val mobilePhoneNumber: String? = null,
  /** 이메일 */
  val email: String? = null,
)
