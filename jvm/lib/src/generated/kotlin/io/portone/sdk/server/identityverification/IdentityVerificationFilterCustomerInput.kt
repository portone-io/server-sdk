package io.portone.sdk.server.identityverification

import io.portone.sdk.server.common.Gender
import kotlin.String
import kotlinx.serialization.Serializable

/** 본인인증 다건 조회를 위한 고객 정보 입력 정보 */
@Serializable
public data class IdentityVerificationFilterCustomerInput(
  /** 이름 */
  val name: String? = null,
  /** 출생 연도 */
  val birthYear: String? = null,
  /** 출생월 */
  val birthMonth: String? = null,
  /** 출생일 */
  val birthDay: String? = null,
  /**
   * 전화번호
   *
   * 특수 문자(-) 없이 숫자로만 이루어진 번호 형식입니다.
   */
  val phoneNumber: String? = null,
  /** 성별 */
  val gender: Gender? = null,
)


