package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class B2bCompanyContactInput(
  /**
   * 담당자 ID
   *
   * 팝빌 로그인 계정으로 사용됩니다.
   */
  val id: String,
  /** 비밀번호 */
  val password: String,
  /** 담당자 성명 */
  val name: String,
  /** 담당자 핸드폰 번호 */
  val phoneNumber: String,
  /** 담당자 이메일 */
  val email: String,
)
