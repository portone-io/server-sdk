package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.Serializable

/** 담당자 정보 수정 요청 */
@Serializable
internal data class UpdateB2bMemberCompanyContactBody(
  /** 비밀번호 */
  val password: String? = null,
  /** 담당자 성명 */
  val name: String? = null,
  /** 담당자 핸드폰 번호 */
  val phoneNumber: String? = null,
  /** 담당자 이메일 */
  val email: String? = null,
)
