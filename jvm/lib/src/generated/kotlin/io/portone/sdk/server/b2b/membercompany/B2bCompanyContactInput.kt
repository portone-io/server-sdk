package io.portone.sdk.server.b2b.membercompany

import kotlin.String
import kotlinx.serialization.Serializable

/** 담당자 관련 입력 정보 */
@Serializable
public data class B2bCompanyContactInput(
  /** 담당자 성명 */
  val name: String,
  /** 담당자 핸드폰 번호 */
  val phoneNumber: String,
  /** 담당자 이메일 */
  val email: String,
  /**
   * 담당자 계정 ID
   *
   * 팝빌 로그인 계정으로 사용됩니다.
   * 값을 입력하지 않을 경우 자동 채번됩니다.
   */
  val loginId: String? = null,
  /**
   * 비밀번호
   *
   * 값을 입력하지 않을 경우 자동 채번됩니다.
   */
  val password: String? = null,
)
