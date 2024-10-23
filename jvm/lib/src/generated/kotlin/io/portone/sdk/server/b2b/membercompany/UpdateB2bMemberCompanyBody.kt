package io.portone.sdk.server.b2b.membercompany

import kotlin.String
import kotlinx.serialization.Serializable

/** 연동 사업자 정보 수정 요청 */
@Serializable
internal data class UpdateB2bMemberCompanyBody(
  /** 회사명 */
  val companyName: String? = null,
  /** 대표자 성명 */
  val representativeName: String? = null,
  /** 회사 주소 */
  val address: String? = null,
  /** 업태 */
  val businessType: String? = null,
  /** 업종 */
  val businessClass: String? = null,
)
