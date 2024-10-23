package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceContact
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class B2bTaxInvoiceCompany(
  /**
   * 사업자등록번호
   *
   * `-`를 제외한 10자리
   */
  val brn: String,
  /**
   * 종사업자 식별 번호
   *
   * 4자리 고정
   */
  val taxRegistrationId: String? = null,
  /**
   * 상호명
   *
   * 최대 200자
   */
  val name: String? = null,
  /**
   * 대표자 성명
   *
   * 최대 100자
   */
  val representativeName: String? = null,
  /**
   * 주소
   *
   * 최대 300자
   */
  val address: String? = null,
  /**
   * 업태
   *
   * 최대 100자
   */
  val businessType: String? = null,
  /**
   * 종목
   *
   * 최대 100자
   */
  val businessClass: String? = null,
  /** 담당자 */
  val contact: B2bTaxInvoiceContact? = null,
)
