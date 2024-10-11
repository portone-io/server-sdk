package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.Serializable

/** 연동 사업자 정보 수정 요청 */
@Serializable
public data class UpdateB2bMemberCompanyBody(
  /** 회사명 */
  val name: String? = null,
  /** 대표자 성명 */
  val ceoName: String? = null,
  /** 회사 주소 */
  val address: String? = null,
  /** 업태 */
  val businessType: String? = null,
  /** 업종 */
  val businessClass: String? = null,
)
