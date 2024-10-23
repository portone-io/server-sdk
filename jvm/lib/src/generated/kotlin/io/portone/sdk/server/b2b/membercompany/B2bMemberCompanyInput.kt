package io.portone.sdk.server.b2b.membercompany

import kotlin.String
import kotlinx.serialization.Serializable

/** 사업자 입력 정보 */
@Serializable
public data class B2bMemberCompanyInput(
  /** 사업자등록번호 */
  val brn: String,
  /** 회사명 */
  val companyName: String,
  /** 대표자 성명 */
  val representativeName: String,
  /** 회사 주소 */
  val address: String,
  /** 업태 */
  val businessType: String,
  /** 업종 */
  val businessClass: String,
)
