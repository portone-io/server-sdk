package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

@Serializable
public data class B2bCompanyContact(
  /**
   * 담당자 ID
   *
   * 팝빌 로그인 계정으로 사용됩니다.
   */
  val id: String,
  /** 담당자 성명 */
  val name: String,
  /** 담당자 핸드폰 번호 */
  val phoneNumber: String,
  /** 담당자 이메일 */
  val email: String,
  /** 등록 일시 */
  val registeredAt: Instant,
  /**
   * 관리자 여부
   *
   * true일 경우 관리자, false일 경우 담당자입니다.
   */
  val isManager: Boolean,
)
