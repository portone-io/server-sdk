package io.portone.sdk.server.identityverification

import kotlin.String
import kotlinx.serialization.Serializable

/** 요청 시 고객 정보 */
@Serializable
public data class IdentityVerificationRequestedCustomer(
  /** 식별 아이디 */
  val id: String? = null,
  /** 이름 */
  val name: String? = null,
  /**
   * 전화번호
   *
   * 특수 문자(-) 없이 숫자로만 이루어진 번호 형식입니다.
   */
  val phoneNumber: String? = null,
  /** 출생연도 */
  val birthYear: String? = null,
  /** 출생월 */
  val birthMonth: String? = null,
  /** 출생일 */
  val birthDay: String? = null,
)


