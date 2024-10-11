package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class B2bMemberCompany(
  /**
   * 사업자등록번호
   *
   * `-` 없이 숫자로만 구성됩니다.
   */
  val brn: String,
  /** 회사명 */
  val name: String,
  /** 대표자 성명 */
  val ceoName: String,
  /** 회사 주소 */
  val address: String,
  /** 업태 */
  val businessType: String,
  /** 업종 */
  val businessClass: String,
)
